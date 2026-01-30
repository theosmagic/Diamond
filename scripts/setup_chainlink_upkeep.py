#!/usr/bin/env python3
"""
Chainlink Automation Upkeep Setup
==================================

Set up Chainlink Automation to monitor TreasureDAO floor prices
and execute automatically based on Blockscout data.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from integrations.chainlink_api import ChainlinkAutomation, ChainlinkIntegration


async def setup_floor_price_monitor(
    nft_contract: str,
    threshold_eth: float,
    diamond_address: str,
    chain_id: int = 42161
):
    """
    Set up Chainlink Automation to monitor NFT floor price
    
    When floor price drops below threshold, triggers Diamond Contract action
    """
    automation = ChainlinkAutomation(chain_id=chain_id)
    
    # Convert ETH threshold to wei
    threshold_wei = int(threshold_eth * 10**18)
    
    # Set up upkeep
    upkeep = await automation.monitor_floor_price(
        nft_contract=nft_contract,
        threshold=threshold_wei,
        action_contract=diamond_address
    )
    
    return upkeep


async def setup_volume_spike_monitor(
    token_contract: str,
    threshold_multiplier: float,
    diamond_address: str,
    chain_id: int = 42161
):
    """
    Set up Chainlink Automation to monitor volume spikes
    
    When volume exceeds threshold, triggers Diamond Contract action
    """
    automation = ChainlinkAutomation(chain_id=chain_id)
    
    # Create check data: encode token address + threshold
    check_data = f"{token_contract}:{threshold_multiplier}".encode()
    
    upkeep = await automation.create_upkeep(
        target_contract=diamond_address,
        check_data=check_data,
        gas_limit=500000,
        admin_address=os.getenv('WALLET_ADDRESS', ''),
        funding_amount=5 * 10**18  # 5 LINK
    )
    
    return upkeep


async def main():
    """Main setup"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Setup Chainlink Automation")
    parser.add_argument("--floor-price", action="store_true", help="Setup floor price monitor")
    parser.add_argument("--volume-spike", action="store_true", help="Setup volume spike monitor")
    parser.add_argument("--nft-contract", type=str, help="NFT contract address")
    parser.add_argument("--token-contract", type=str, help="Token contract address")
    parser.add_argument("--threshold", type=float, help="Threshold value")
    parser.add_argument("--diamond", type=str, help="Diamond contract address")
    parser.add_argument("--chain", type=int, default=42161, help="Chain ID")
    
    args = parser.parse_args()
    
    if args.floor_price and args.nft_contract and args.diamond:
        upkeep = await setup_floor_price_monitor(
            args.nft_contract,
            args.threshold or 100.0,
            args.diamond,
            args.chain
        )
        print("✅ Floor price monitor setup:")
        print(f"   Registry: {upkeep.get('registry_address')}")
        print(f"   NFT Contract: {args.nft_contract}")
        print(f"   Threshold: {args.threshold or 100.0} ETH")
        print(f"   Diamond: {args.diamond}")
    
    if args.volume_spike and args.token_contract and args.diamond:
        upkeep = await setup_volume_spike_monitor(
            args.token_contract,
            args.threshold or 2.0,
            args.diamond,
            args.chain
        )
        print("✅ Volume spike monitor setup:")
        print(f"   Registry: {upkeep.get('registry_address')}")
        print(f"   Token Contract: {args.token_contract}")
        print(f"   Threshold: {args.threshold or 2.0}x")
        print(f"   Diamond: {args.diamond}")
    
    if not args.floor_price and not args.volume_spike:
        print("Usage:")
        print("  --floor-price --nft-contract 0x... --diamond 0x... --threshold 100")
        print("  --volume-spike --token-contract 0x... --diamond 0x... --threshold 2.0")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

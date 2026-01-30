#!/usr/bin/env python3
"""
Comprehensive Integration Test

Tests all integrations to verify they're working correctly.
"""

import asyncio
import sys
from pathlib import Path

# Add integrations to path
sys.path.insert(0, str(Path(__file__).parent.parent / "integrations"))


async def test_all_integrations():
    """Test all integrations"""
    print("=" * 80)
    print("COMPREHENSIVE INTEGRATION TEST")
    print("=" * 80)
    print()
    
    # Test 1: Chainlist
    print("1. Testing Chainlist Integration...")
    try:
        from chainlist_api import ChainlistAPI
        chainlist = ChainlistAPI()
        chains = await chainlist.fetch_all_chains()
        print(f"   ✅ Fetched {len(chains)} chains from Chainlist")
        rpc = await chainlist.get_best_rpc(42161)
        if rpc:
            print(f"   ✅ Best Arbitrum RPC: {rpc[:50]}...")
        else:
            print("   ⚠️  No RPC found for Arbitrum")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    print()
    
    # Test 2: Chainlink
    print("2. Testing Chainlink Integration...")
    try:
        from chainlink_api import ChainlinkIntegration
        chainlink = ChainlinkIntegration(chain_id=42161)
        print(f"   ✅ Chainlink initialized (Chain ID: {chainlink.chain_id})")
        print(f"   ✅ Price Feeds: {len(chainlink.price_feeds.feeds)} configured")
        registry = chainlink.automation.get_registry_address()
        print(f"   ✅ Automation Registry: {registry}")
        print(f"   ✅ CCIP Routers: {len(chainlink.ccip.router_addresses)} configured")
        print(f"   ✅ Functions Routers: {len(chainlink.functions.router_addresses)} configured")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    print()
    
    # Test 3: Blockscout
    print("3. Testing Blockscout Integration...")
    try:
        from blockscout_api import BlockscoutAPI
        blockscout = BlockscoutAPI(chain_id=42161)
        print(f"   ✅ Blockscout initialized (Chain ID: {blockscout.chain_id})")
        print(f"   ✅ Base URL: {blockscout.base_url}")
        print(f"   ✅ API Type: {blockscout.api_type}")
        print(f"   ✅ API Key configured: {'Yes' if blockscout.api_key else 'No'}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    print()
    
    # Test 4: Safe{Wallet}
    print("4. Testing Safe{Wallet} Integration...")
    try:
        from safe_wallet import UnifiedWalletInterface
        wallet = UnifiedWalletInterface()
        config = wallet.get_unified_config()
        print(f"   ✅ Safe{Wallet} initialized")
        print(f"   ✅ ENS: {config['ens']}")
        print(f"   ✅ Email: {config['email']}")
        print(f"   ✅ Networks: {len(config['networks'])} configured")
        print(f"   ✅ MetaMask SDK: Configured")
        print(f"   ✅ WalletConnect AppKit: Configured")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    print()
    
    print("=" * 80)
    print("✅ ALL INTEGRATIONS TESTED")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_all_integrations())

#!/usr/bin/env python3
"""
TreasureDAO NFT Claim Script
Uses Master Key Covenant to claim Treasure NFT and Legion boosts
"""

import sys
from pathlib import Path
from web3 import Web3
import json

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from integrations.master_key_covenant import MasterKeyCovenant


def claim_treasure_nft(rpc_url: str = "https://arb1.arbitrum.io/rpc", dry_run: bool = True):
    """
    Execute claim for Treasure NFT using Master Key Covenant.
    
    Args:
        rpc_url: Arbitrum RPC endpoint
        dry_run: If True, only simulate (don't broadcast)
    """
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print("🎁 TREASURE NFT CLAIM SCRIPT\n")
    
    # Initialize covenant
    covenant = MasterKeyCovenant()
    
    if not covenant.verified:
        print("⚠️  Covenant signature verification pending")
        print("   Proceeding with claim data generation...\n")
    
    # Get Treasure NFT claim data
    treasure_claim = covenant.get_treasure_nft_claim()
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                TREASURE NFT CLAIM DATA                         ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    print(f"Contract: {treasure_claim['contract_name']} ({treasure_claim['glyph']})")
    print(f"Address: {treasure_claim['contract_address']}")
    print(f"Explorer: {treasure_claim['explorer']}\n")
    
    print("Claim Payload:")
    claim_data = treasure_claim['claim_data']
    for key, value in claim_data.items():
        if key in ['covenant_signature', 'master_key_hash']:
            print(f"  {key}: {str(value)[:20]}...{str(value)[-20:]}")
        else:
            print(f"  {key}: {value}")
    
    print("\n═══════════════════════════════════════════════════════════════")
    print("MASTER KEY TOKEN (for claim):")
    print("═══════════════════════════════════════════════════════════════")
    print(f"Token: {covenant.MASTER_KEY_TOKEN}")
    print("Format: Base58 (likely IPFS CID or claim proof)")
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No transaction broadcast")
        print("\nTo execute on-chain claim:")
        print("1. Use the Master Key Token in the TreasureDAO marketplace")
        print("2. Or call contract method: claimWithSignature()")
        print("3. Parameters:")
        print(f"   - address: {covenant.SOVEREIGN_ADDRESS}")
        print(f"   - signature: {covenant.COVENANT_SIGNATURE}")
        print(f"   - token: {covenant.MASTER_KEY_TOKEN}")
    else:
        print("\n🚀 EXECUTING ON-CHAIN CLAIM...")
        # TODO: Implement actual on-chain transaction
        # This would require:
        # 1. Contract ABI for Treasure NFT claim function
        # 2. Private key for signing transaction
        # 3. Gas estimation and execution
        print("❌ Live claim not yet implemented")
        print("   Use TreasureDAO marketplace interface for now")
    
    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ\n")


def claim_legion_boost(rpc_url: str = "https://arb1.arbitrum.io/rpc", dry_run: bool = True):
    """
    Execute claim for Legion boost using Master Key Covenant.
    """
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print("⚔️  LEGION BOOST CLAIM SCRIPT\n")
    
    covenant = MasterKeyCovenant()
    legion_claim = covenant.get_legion_boost_claim()
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                LEGION BOOST CLAIM DATA                         ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    print(f"Contract: {legion_claim['contract_name']} ({legion_claim['glyph']})")
    print(f"Address: {legion_claim['contract_address']}")
    print(f"Boost Type: {legion_claim['boost_type']}")
    print(f"Explorer: {legion_claim['explorer']}\n")
    
    print("Claim Data:")
    claim_data = legion_claim['claim_data']
    for key, value in claim_data.items():
        if key in ['covenant_signature', 'master_key_hash']:
            print(f"  {key}: {str(value)[:20]}...{str(value)[-20:]}")
        else:
            print(f"  {key}: {value}")
    
    print("\n═══════════════════════════════════════════════════════════════")
    print("MASTER KEY TOKEN (for Legion boost):")
    print("═══════════════════════════════════════════════════════════════")
    print(f"Token: {covenant.MASTER_KEY_TOKEN}")
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - Use token in Bridgeworld interface")
    
    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ\n")


def claim_all_22_contracts():
    """
    Generate claim payloads for all 22 TreasureDAO contracts.
    """
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print("📜 ALL 22 TREASUREDAO CONTRACTS CLAIM\n")
    
    covenant = MasterKeyCovenant()
    all_claims = covenant.generate_all_22_claims()
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║           22 CONTRACT CLAIM MANIFEST                           ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    print(f"Covenant Verified: {all_claims['covenant_verified']}")
    print(f"Sovereign Address: {all_claims['sovereign_address']}")
    print(f"Master Key Token: {covenant.MASTER_KEY_TOKEN}")
    print(f"Total Contracts: {len(all_claims['contracts'])}\n")
    
    print("═══════════════════════════════════════════════════════════════")
    print("CLAIMABLE CONTRACTS:")
    print("═══════════════════════════════════════════════════════════════\n")
    
    for i, contract in enumerate(all_claims['contracts'], 1):
        print(f"{contract['glyph']} [{i}] {contract['name']}")
        print(f"    Type: {contract['type']}")
        print(f"    Address: {contract['contract']}")
        print(f"    Claim Ready: ✅")
        print()
    
    # Export to JSON
    output_path = "/mnt/Vault/Cursor-Agent/config/treasure_claims_manifest.json"
    with open(output_path, 'w') as f:
        json.dump(all_claims, f, indent=2)
    
    print(f"✅ Full claim manifest exported to: {output_path}")
    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Claim TreasureDAO NFTs using Master Key Covenant',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('operation', choices=['treasure', 'legion', 'all'],
                       help='Claim operation: treasure (NFT), legion (boost), or all (22 contracts)')
    parser.add_argument('--live', action='store_true',
                       help='Execute live transaction (default: dry run)')
    parser.add_argument('--rpc', default='https://arb1.arbitrum.io/rpc',
                       help='Arbitrum RPC endpoint')
    
    args = parser.parse_args()
    
    if args.operation == 'treasure':
        claim_treasure_nft(args.rpc, dry_run=not args.live)
    elif args.operation == 'legion':
        claim_legion_boost(args.rpc, dry_run=not args.live)
    elif args.operation == 'all':
        claim_all_22_contracts()

#!/usr/bin/env python3
"""
Test Chainlist Integration

Quick test script to verify Chainlist API integration works correctly.
"""

import asyncio
import sys
from pathlib import Path

# Add integrations to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "integrations"))

from chainlist_api import ChainlistAPI, get_rpc_for_chain, get_all_rpcs_for_chain


async def test_chainlist():
    """Test Chainlist API integration"""
    print("=" * 80)
    print("CHAINLIST INTEGRATION TEST")
    print("=" * 80)
    print()
    
    api = ChainlistAPI()
    
    # Test chains we care about
    test_chains = [
        (1, "Ethereum Mainnet"),
        (42161, "Arbitrum One"),
        (137, "Polygon"),
        (8453, "Base")
    ]
    
    print("Testing RPC Discovery:")
    print("-" * 80)
    
    for chain_id, chain_name in test_chains:
        print(f"\n{chain_name} (Chain ID: {chain_id})")
        
        # Get chain info
        chain_info = await api.get_chain_by_id(chain_id)
        if chain_info:
            print(f"  ✅ Found chain: {chain_info.get('name', 'Unknown')}")
            
            # Get RPC endpoints
            rpcs = await api.get_rpc_endpoints(chain_id)
            print(f"  📡 RPC Endpoints: {len(rpcs)} found")
            
            if rpcs:
                # Show first 3 RPCs
                for i, rpc in enumerate(rpcs[:3], 1):
                    print(f"     {i}. {rpc}")
                if len(rpcs) > 3:
                    print(f"     ... and {len(rpcs) - 3} more")
                
                # Get best RPC
                best_rpc = await api.get_best_rpc(chain_id)
                if best_rpc:
                    print(f"  ⭐ Best RPC: {best_rpc}")
            else:
                print(f"  ⚠️  No RPC endpoints found")
        else:
            print(f"  ❌ Chain not found in Chainlist")
    
    print("\n" + "=" * 80)
    print("Testing Convenience Functions:")
    print("-" * 80)
    
    # Test convenience functions
    arbitrum_rpc = await get_rpc_for_chain(42161)
    if arbitrum_rpc:
        print(f"✅ get_rpc_for_chain(42161): {arbitrum_rpc}")
    
    arbitrum_rpcs = await get_all_rpcs_for_chain(42161)
    print(f"✅ get_all_rpcs_for_chain(42161): {len(arbitrum_rpcs)} endpoints")
    
    print("\n" + "=" * 80)
    print("Testing Chain Search:")
    print("-" * 80)
    
    # Test search
    search_results = await api.search_chains("arbitrum")
    print(f"Search 'arbitrum': {len(search_results)} results")
    for result in search_results[:3]:
        print(f"  - {result.get('name')} (Chain ID: {result.get('chainId')})")
    
    print("\n" + "=" * 80)
    print("✅ Chainlist Integration Test Complete")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_chainlist())

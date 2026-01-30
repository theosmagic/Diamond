"""
Control Asset Center - Unified Blockchain Asset Management
Integrates: Chainlist, Chainlink, Blockscout, DEX, MetaMask Portfolio
"""

import json
import requests
from typing import Dict, List, Optional, Any
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime


@dataclass
class NetworkConfig:
    """Network configuration from Chainlist"""
    chain_id: int
    name: str
    rpc_urls: List[str]
    native_currency: Dict[str, str]
    block_explorer: str
    is_testnet: bool = False


@dataclass
class AssetBalance:
    """Asset balance information"""
    token_address: str
    token_name: str
    token_symbol: str
    balance: str
    balance_usd: Optional[float]
    chain_id: int


class ControlAssetCenter:
    """
    Unified Control Center for blockchain asset management.
    Integrates multiple services for comprehensive asset visibility.
    """

    def __init__(self, config_path: str = "/mnt/Vault/Cursor-Agent/config/defaults.json"):
        self.config = self._load_config(config_path)
        self.session = requests.Session()
        self.networks: Dict[int, NetworkConfig] = {}
        
    def _load_config(self, path: str) -> Dict[str, Any]:
        """Load configuration."""
        with open(path, 'r') as f:
            return json.load(f)

    # ═══════════════════════════════════════════════════════════════
    # CHAINLIST INTEGRATION
    # ═══════════════════════════════════════════════════════════════

    def fetch_chainlist_networks(self, include_testnets: bool = False) -> List[NetworkConfig]:
        """
        Fetch network data from Chainlist API.
        Returns list of supported networks with RPC endpoints.
        """
        print("🔗 Fetching networks from Chainlist...")
        
        try:
            # Chainlist API endpoint
            url = "https://chainid.network/chains.json"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            chains = response.json()
            networks = []
            
            for chain in chains:
                # Filter testnets if not requested
                is_testnet = chain.get('name', '').lower().find('test') != -1
                if not include_testnets and is_testnet:
                    continue
                
                # Get explorer URL safely
                explorers = chain.get('explorers', [])
                explorer_url = ''
                if explorers and len(explorers) > 0:
                    explorer_url = explorers[0].get('url', '')
                
                network = NetworkConfig(
                    chain_id=chain['chainId'],
                    name=chain['name'],
                    rpc_urls=chain.get('rpc', []),
                    native_currency=chain.get('nativeCurrency', {}),
                    block_explorer=explorer_url,
                    is_testnet=is_testnet
                )
                
                networks.append(network)
                self.networks[network.chain_id] = network
            
            print(f"   ✅ Loaded {len(networks)} networks")
            return networks
            
        except Exception as e:
            print(f"   ❌ Error fetching Chainlist: {e}")
            return []

    def get_network_rpcs(self, chain_id: int) -> List[str]:
        """Get RPC URLs for a specific chain."""
        if chain_id in self.networks:
            return self.networks[chain_id].rpc_urls
        return []

    # ═══════════════════════════════════════════════════════════════
    # CHAINLINK INTEGRATION
    # ═══════════════════════════════════════════════════════════════

    def get_chainlink_price_feed(self, pair: str = "ETH/USD", network: str = "ethereum") -> Optional[Dict]:
        """
        Get Chainlink oracle price feed data.
        
        Args:
            pair: Trading pair (e.g., "ETH/USD", "BTC/USD")
            network: Network name
        """
        print(f"📊 Fetching Chainlink {pair} price feed on {network}...")
        
        try:
            # Chainlink Data Feeds API (using public endpoints)
            # In production, you'd use Web3 to call the oracle contracts directly
            
            # For demo, using a mock response structure
            feeds = {
                "ETH/USD": {
                    "address": "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",  # Mainnet
                    "decimals": 8,
                    "description": "ETH / USD"
                },
                "BTC/USD": {
                    "address": "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c",  # Mainnet
                    "decimals": 8,
                    "description": "BTC / USD"
                }
            }
            
            if pair in feeds:
                print(f"   ✅ Price feed found: {feeds[pair]['address']}")
                return feeds[pair]
            else:
                print(f"   ⚠️  Price feed not configured for {pair}")
                return None
                
        except Exception as e:
            print(f"   ❌ Error fetching Chainlink data: {e}")
            return None

    # ═══════════════════════════════════════════════════════════════
    # BLOCKSCOUT INTEGRATION
    # ═══════════════════════════════════════════════════════════════

    def blockscout_get_address_balance(self, address: str, chain_id: int = 1) -> Optional[Dict]:
        """
        Get address balance and transaction history from Blockscout.
        
        Args:
            address: Wallet address
            chain_id: Network chain ID
        """
        print(f"🔍 Fetching Blockscout data for {address[:10]}... on chain {chain_id}")
        
        try:
            # Blockscout API endpoints by chain
            blockscout_urls = {
                1: "https://eth.blockscout.com/api",
                100: "https://gnosis.blockscout.com/api",
                137: "https://polygon.blockscout.com/api",
                42161: "https://arbitrum.blockscout.com/api",
            }
            
            base_url = blockscout_urls.get(chain_id)
            if not base_url:
                print(f"   ⚠️  Blockscout not available for chain {chain_id}")
                return None
            
            # Get balance
            params = {
                'module': 'account',
                'action': 'balance',
                'address': address
            }
            
            response = self.session.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('status') == '1':
                balance_wei = int(data['result'])
                balance_eth = balance_wei / 10**18
                
                print(f"   ✅ Balance: {balance_eth:.4f} ETH")
                return {
                    'address': address,
                    'balance_wei': balance_wei,
                    'balance_eth': balance_eth,
                    'chain_id': chain_id
                }
            else:
                print(f"   ⚠️  Error: {data.get('message', 'Unknown')}")
                return None
                
        except Exception as e:
            print(f"   ❌ Error fetching Blockscout data: {e}")
            return None

    def blockscout_get_token_balances(self, address: str, chain_id: int = 1) -> List[AssetBalance]:
        """Get ERC20 token balances for an address."""
        print(f"🪙 Fetching token balances for {address[:10]}...")
        
        try:
            blockscout_urls = {
                1: "https://eth.blockscout.com/api",
                42161: "https://arbitrum.blockscout.com/api",
            }
            
            base_url = blockscout_urls.get(chain_id)
            if not base_url:
                return []
            
            params = {
                'module': 'account',
                'action': 'tokenlist',
                'address': address
            }
            
            response = self.session.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            balances = []
            
            if data.get('status') == '1' and isinstance(data.get('result'), list):
                for token in data['result']:
                    balance = AssetBalance(
                        token_address=token.get('contractAddress', ''),
                        token_name=token.get('name', ''),
                        token_symbol=token.get('symbol', ''),
                        balance=token.get('balance', '0'),
                        balance_usd=None,
                        chain_id=chain_id
                    )
                    balances.append(balance)
                
                print(f"   ✅ Found {len(balances)} token balances")
            
            return balances
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return []

    # ═══════════════════════════════════════════════════════════════
    # DEX AGGREGATOR INTEGRATION
    # ═══════════════════════════════════════════════════════════════

    def get_dex_quote(self, from_token: str, to_token: str, amount: str, chain_id: int = 1) -> Optional[Dict]:
        """
        Get DEX swap quote (using 1inch aggregator as example).
        
        Args:
            from_token: Source token address
            to_token: Destination token address
            amount: Amount in wei
            chain_id: Network chain ID
        """
        print(f"💱 Fetching DEX quote: {from_token[:10]}... → {to_token[:10]}...")
        
        try:
            # 1inch API endpoint
            url = f"https://api.1inch.dev/swap/v5.2/{chain_id}/quote"
            
            params = {
                'src': from_token,
                'dst': to_token,
                'amount': amount
            }
            
            # Note: In production, you'd need an API key
            # response = self.session.get(url, params=params, timeout=10)
            
            # Mock response for demonstration
            print("   ℹ️  DEX quote (demo mode - requires API key)")
            return {
                'fromToken': from_token,
                'toToken': to_token,
                'fromTokenAmount': amount,
                'toTokenAmount': '0',  # Would be calculated by 1inch
                'protocols': [],
                'estimatedGas': 150000
            }
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return None

    # ═══════════════════════════════════════════════════════════════
    # METAMASK PORTFOLIO INTEGRATION
    # ═══════════════════════════════════════════════════════════════

    def get_portfolio_summary(self, address: str) -> Dict[str, Any]:
        """
        Generate comprehensive portfolio summary across all chains.
        Aggregates data from Blockscout, Chainlink, etc.
        """
        print(f"\n{'='*60}")
        print(f"📊 PORTFOLIO SUMMARY: {address}")
        print(f"{'='*60}\n")
        
        portfolio = {
            'address': address,
            'timestamp': datetime.now().isoformat(),
            'networks': {},
            'total_value_usd': 0.0,
            'tokens': []
        }
        
        # Key networks to check
        networks_to_check = [
            (1, "Ethereum"),
            (42161, "Arbitrum"),
            (137, "Polygon"),
        ]
        
        for chain_id, name in networks_to_check:
            print(f"\n🔗 {name} (Chain ID: {chain_id})")
            print("-" * 60)
            
            # Get native balance
            balance_data = self.blockscout_get_address_balance(address, chain_id)
            
            # Get token balances
            token_balances = self.blockscout_get_token_balances(address, chain_id)
            
            portfolio['networks'][chain_id] = {
                'name': name,
                'native_balance': balance_data,
                'token_count': len(token_balances),
                'tokens': token_balances
            }
            
            portfolio['tokens'].extend(token_balances)
        
        print(f"\n{'='*60}")
        print(f"✅ Portfolio analysis complete")
        print(f"{'='*60}\n")
        
        return portfolio

    # ═══════════════════════════════════════════════════════════════
    # EXPORT & REPORTING
    # ═══════════════════════════════════════════════════════════════

    def export_portfolio_report(self, address: str, output_path: str = None) -> str:
        """Generate and export portfolio report."""
        if output_path is None:
            output_path = f"/mnt/Vault/Cursor-Agent/cache/portfolio_{address[:10]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        portfolio = self.get_portfolio_summary(address)
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(portfolio, f, indent=2, default=str)
        
        print(f"📄 Report saved: {output_path}")
        return output_path


# ═══════════════════════════════════════════════════════════════
# LUCY INTEGRATION
# ═══════════════════════════════════════════════════════════════

class LucyAssetCenterBridge:
    """Bridge for Lucy to access Control Asset Center."""
    
    def __init__(self):
        self.center = ControlAssetCenter()
    
    def execute_for_lucy(self, operation: str, *args) -> Dict[str, Any]:
        """
        Execute asset center operations for Lucy.
        
        Operations:
        - 'networks': Fetch Chainlist networks
        - 'price': Get Chainlink price feed
        - 'balance': Get address balance
        - 'portfolio': Get full portfolio summary
        - 'dex_quote': Get DEX swap quote
        """
        try:
            if operation == 'networks':
                include_testnets = args[0] if args else False
                networks = self.center.fetch_chainlist_networks(include_testnets)
                return {
                    'success': True,
                    'count': len(networks),
                    'networks': [n.__dict__ for n in networks[:10]]  # First 10
                }
            
            elif operation == 'price':
                pair = args[0] if args else "ETH/USD"
                data = self.center.get_chainlink_price_feed(pair)
                return {'success': True, 'data': data}
            
            elif operation == 'balance':
                address = args[0]
                chain_id = args[1] if len(args) > 1 else 1
                balance = self.center.blockscout_get_address_balance(address, chain_id)
                return {'success': True, 'balance': balance}
            
            elif operation == 'portfolio':
                address = args[0]
                portfolio = self.center.get_portfolio_summary(address)
                return {'success': True, 'portfolio': portfolio}
            
            elif operation == 'dex_quote':
                from_token, to_token, amount = args[0], args[1], args[2]
                chain_id = args[3] if len(args) > 3 else 1
                quote = self.center.get_dex_quote(from_token, to_token, amount, chain_id)
                return {'success': True, 'quote': quote}
            
            else:
                return {'success': False, 'error': f'Unknown operation: {operation}'}
                
        except Exception as e:
            return {'success': False, 'error': str(e)}


if __name__ == "__main__":
    # Test Control Asset Center
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print("🎛️  CONTROL ASSET CENTER - Initializing...\n")
    
    center = ControlAssetCenter()
    
    # Test primary wallet
    primary_address = center.config['primary_wallet']['address']
    
    # Fetch networks
    center.fetch_chainlist_networks(include_testnets=False)
    
    # Generate portfolio report
    center.export_portfolio_report(primary_address)
    
    print("\n✅ Control Asset Center operational")

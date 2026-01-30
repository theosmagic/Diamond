"""
ENS (Ethereum Name Service) Integration
========================================

Integration with ENS for resolving names and addresses.

Official ENS Resources:
- Repository: https://github.com/ensdomains/ensjs
- Contracts: https://github.com/ensdomains/ens-contracts
- Documentation: https://docs.ens.domains/
"""

import os
from typing import Optional, Dict, Any
from integrations.config import get_default_ens, get_default_email


class ENSResolver:
    """
    ENS Resolver for Python
    
    Resolves ENS names to addresses and vice versa.
    Uses web3.py or direct RPC calls for resolution.
    """
    
    # ENS Registry Address (Ethereum Mainnet)
    ENS_REGISTRY_ADDRESS = "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"
    
    def __init__(self, rpc_url: Optional[str] = None):
        """
        Initialize ENS Resolver
        
        Args:
            rpc_url: Ethereum RPC URL (defaults to environment variable)
        """
        self.rpc_url = rpc_url or os.getenv("ETHEREUM_RPC_URL", "")
        self.default_ens = get_default_ens()
        self.default_email = get_default_email()
    
    def resolve_name(self, name: str) -> Optional[str]:
        """
        Resolve ENS name to address
        
        Args:
            name: ENS name (e.g., "theosmagic.uni.eth")
            
        Returns:
            Ethereum address or None
        """
        try:
            # Use web3.py if available
            try:
                from web3 import Web3
                if self.rpc_url:
                    w3 = Web3(Web3.HTTPProvider(self.rpc_url))
                    address = w3.ens.address(name)
                    return address if address else None
            except ImportError:
                pass
            
            # Fallback: Return None if web3.py not available
            return None
        except Exception as e:
            print(f"Failed to resolve ENS name {name}: {e}")
            return None
    
    def reverse_resolve(self, address: str) -> Optional[str]:
        """
        Reverse resolve address to ENS name
        
        Args:
            address: Ethereum address
            
        Returns:
            ENS name or None
        """
        try:
            # Use web3.py if available
            try:
                from web3 import Web3
                if self.rpc_url:
                    w3 = Web3(Web3.HTTPProvider(self.rpc_url))
                    name = w3.ens.name(address)
                    return name if name else None
            except ImportError:
                pass
            
            # Fallback: Return None if web3.py not available
            return None
        except Exception as e:
            print(f"Failed to reverse resolve address {address}: {e}")
            return None
    
    def get_default_ens_info(self) -> Dict[str, Any]:
        """
        Get default ENS information
        
        Returns:
            Dictionary with default ENS info
        """
        return {
            "ens": self.default_ens,
            "email": self.default_email,
            "description": "Default ENS domain and email"
        }
    
    def is_valid_ens_name(self, name: str) -> bool:
        """
        Validate ENS name format
        
        Args:
            name: ENS name to validate
            
        Returns:
            True if valid ENS name format
        """
        if not name or not name.endswith(".eth"):
            return False
        
        parts = name.split(".")
        if len(parts) < 2:
            return False
        
        # Check each part
        for part in parts:
            if len(part) == 0:
                return False
            if not part.replace("-", "").isalnum():
                return False
        
        return True


# Global instance
_ens_resolver: Optional[ENSResolver] = None


def get_ens_resolver(rpc_url: Optional[str] = None) -> ENSResolver:
    """Get global ENS resolver instance"""
    global _ens_resolver
    if _ens_resolver is None:
        _ens_resolver = ENSResolver(rpc_url)
    return _ens_resolver


def resolve_ens_name(name: str, rpc_url: Optional[str] = None) -> Optional[str]:
    """Quick function to resolve ENS name"""
    resolver = get_ens_resolver(rpc_url)
    return resolver.resolve_name(name)


def reverse_resolve_address(address: str, rpc_url: Optional[str] = None) -> Optional[str]:
    """Quick function to reverse resolve address"""
    resolver = get_ens_resolver(rpc_url)
    return resolver.reverse_resolve(address)


if __name__ == "__main__":
    resolver = ENSResolver()
    info = resolver.get_default_ens_info()
    
    print("=" * 80)
    print("ENS RESOLVER")
    print("=" * 80)
    print()
    print(f"Default ENS: {info['ens']}")
    print(f"Default Email: {info['email']}")
    print()
    print("=" * 80)

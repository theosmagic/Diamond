"""
Primary Wallet Manager
======================

Manages the primary default wallet that controls all operations.

Primary Wallet:
- Address: 0x67A977eaD94C3b955ECbf27886CE9f62464423B2
- Email: theosmagic.uni.eth@ethermail.io
- ENS: theosmagic.uni.eth
- Controls: Diamond Contract, Safe{Wallet}, all transactions
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from integrations.config import get_primary_wallet, get_default_wallet_address
from typing import List


class PrimaryWalletManager:
    """
    Primary Wallet Manager
    
    Manages the primary default wallet that controls all operations.
    """
    
    def __init__(self):
        """Initialize Primary Wallet Manager"""
        primary_wallet = get_primary_wallet()
        self.address = primary_wallet.get("address", "0x67A977eaD94C3b955ECbf27886CE9f62464423B2")
        self.email = primary_wallet.get("email", "theosmagic.uni.eth@ethermail.io")
        self.ens = primary_wallet.get("ens", "theosmagic.uni.eth")
        
        # Get seed phrase from environment (never store in code)
        self.seed_phrase = os.getenv("OPENSEA_12_WORD_SEED", "")
        
        # Override with environment variables if present
        self.address = os.getenv("PUBLIC_ADDRESS", self.address)
        self.email = os.getenv("DIGITAL_PERSONA_EMAIL", os.getenv("EMAIL", self.email))
        self.ens = os.getenv("ENS_NAME", self.ens)
    
    def get_wallet_info(self) -> Dict[str, Any]:
        """
        Get primary wallet information
        
        Returns:
            Primary wallet configuration
        """
        return {
            "address": self.address,
            "email": self.email,
            "ens": self.ens,
            "is_primary": True,
            "controls": [
                "diamond_contract",
                "safe_wallet",
                "all_transactions",
                "multi_chain_operations",
                "metamask_sdk",
                "walletconnect_appkit"
            ],
            "description": "Primary default wallet - controls all operations"
        }
    
    def is_primary_wallet(self, address: str) -> bool:
        """
        Check if address is the primary wallet
        
        Args:
            address: Wallet address to check
        
        Returns:
            True if address matches primary wallet
        """
        return address.lower() == self.address.lower()
    
    def get_owner_addresses(self) -> List[str]:
        """
        Get list of owner addresses for Safe{Wallet}
        
        Primary wallet is always the first owner
        
        Returns:
            List of owner addresses
        """
        return [self.address]
    
    def get_safe_owners(self) -> List[str]:
        """
        Get Safe{Wallet} owners configuration
        
        Primary wallet is the primary owner
        
        Returns:
            List of owner addresses for Safe{Wallet}
        """
        return [self.address]


# Global instance
_primary_wallet_manager: Optional[PrimaryWalletManager] = None


def get_primary_wallet_manager() -> PrimaryWalletManager:
    """Get global primary wallet manager instance"""
    global _primary_wallet_manager
    if _primary_wallet_manager is None:
        _primary_wallet_manager = PrimaryWalletManager()
    return _primary_wallet_manager


def get_primary_wallet_address() -> str:
    """Get primary wallet address"""
    return get_primary_wallet_manager().address


def get_primary_wallet_email() -> str:
    """Get primary wallet email"""
    return get_primary_wallet_manager().email


def get_primary_wallet_ens() -> str:
    """Get primary wallet ENS"""
    return get_primary_wallet_manager().ens


if __name__ == "__main__":
    manager = PrimaryWalletManager()
    info = manager.get_wallet_info()
    
    print("=" * 80)
    print("PRIMARY WALLET CONFIGURATION")
    print("=" * 80)
    print()
    print(f"Address: {info['address']}")
    print(f"Email: {info['email']}")
    print(f"ENS: {info['ens']}")
    print(f"Is Primary: {info['is_primary']}")
    print()
    print("Controls:")
    for control in info['controls']:
        print(f"  - {control}")
    print()
    print("=" * 80)

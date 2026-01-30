"""
Ethereum Signature Verification
================================

Verifies Ethereum signed messages for authentication and ownership proof.

Primary Wallet Signature:
- Message: "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds its beginning."
- Address: 0x67A977eaD94C3b955ECbf27886CE9f62464423B2
- Signature: 0x7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c
"""

from typing import Optional, Tuple
from eth_account import Account
from eth_account.messages import encode_defunct, _hash_eip191_message
from eth_utils import to_checksum_address
import hashlib


class EthereumSignatureVerifier:
    """
    Ethereum Signature Verifier
    
    Verifies Ethereum signed messages for authentication.
    """
    
    # Primary wallet signature
    PRIMARY_WALLET_MESSAGE = "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds its beginning."
    PRIMARY_WALLET_ADDRESS = "0x67A977eaD94C3b955ECbf27886CE9f62464423B2"
    PRIMARY_WALLET_SIGNATURE = "0x7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c"
    
    def __init__(self):
        """Initialize Ethereum Signature Verifier"""
        self.account = Account()
    
    def verify_signature(self, message: str, signature: str, expected_address: str) -> Tuple[bool, Optional[str]]:
        """
        Verify an Ethereum signed message
        
        Args:
            message: The message that was signed
            signature: The signature hex string (0x...)
            expected_address: The expected signer address
        
        Returns:
            Tuple of (is_valid, recovered_address)
        """
        try:
            # Encode the message in EIP-191 format
            message_hash = encode_defunct(text=message)
            
            # Recover the address from the signature
            recovered_address = self.account.recover_message(message_hash, signature=signature)
            
            # Normalize addresses for comparison
            recovered_address = to_checksum_address(recovered_address)
            expected_address = to_checksum_address(expected_address)
            
            is_valid = recovered_address.lower() == expected_address.lower()
            
            return is_valid, recovered_address
        except Exception as e:
            return False, None
    
    def verify_primary_wallet_signature(self) -> Tuple[bool, Optional[str]]:
        """
        Verify the primary wallet signature
        
        Returns:
            Tuple of (is_valid, recovered_address)
        """
        return self.verify_signature(
            self.PRIMARY_WALLET_MESSAGE,
            self.PRIMARY_WALLET_SIGNATURE,
            self.PRIMARY_WALLET_ADDRESS
        )
    
    def sign_message(self, message: str, private_key: str) -> str:
        """
        Sign a message with a private key
        
        Args:
            message: The message to sign
            private_key: The private key hex string (0x...)
        
        Returns:
            The signature hex string
        """
        message_hash = encode_defunct(text=message)
        signed_message = self.account.sign_message(message_hash, private_key=private_key)
        return signed_message.signature.hex()
    
    def get_signature_data(self) -> dict:
        """
        Get primary wallet signature data
        
        Returns:
            Dictionary with signature information
        """
        is_valid, recovered_address = self.verify_primary_wallet_signature()
        
        return {
            "message": self.PRIMARY_WALLET_MESSAGE,
            "address": self.PRIMARY_WALLET_ADDRESS,
            "signature": self.PRIMARY_WALLET_SIGNATURE,
            "is_valid": is_valid,
            "recovered_address": recovered_address,
            "verification_status": "verified" if is_valid else "invalid"
        }
    
    def create_signed_message_format(self, message: str, address: str, signature: str) -> str:
        """
        Create Ethereum Signed Message format string
        
        Args:
            message: The message
            address: The signer address
            signature: The signature
        
        Returns:
            Formatted signed message string
        """
        return f"""# -----BEGIN ETHEREUM SIGNED MESSAGE-----
# {message}
# -----ADDRESS-----#######
# {address}
# -----END ETHEREUM SIGNED MESSAGE-----
# {signature}"""


# Global instance
_verifier: Optional[EthereumSignatureVerifier] = None


def get_signature_verifier() -> EthereumSignatureVerifier:
    """Get global signature verifier instance"""
    global _verifier
    if _verifier is None:
        _verifier = EthereumSignatureVerifier()
    return _verifier


def verify_primary_wallet_signature() -> Tuple[bool, Optional[str]]:
    """Verify primary wallet signature"""
    return get_signature_verifier().verify_primary_wallet_signature()


if __name__ == "__main__":
    verifier = EthereumSignatureVerifier()
    data = verifier.get_signature_data()
    
    print("=" * 80)
    print("ETHEREUM SIGNATURE VERIFICATION")
    print("=" * 80)
    print()
    print(f"Message: {data['message']}")
    print(f"Address: {data['address']}")
    print(f"Signature: {data['signature']}")
    print(f"Verification Status: {data['verification_status']}")
    print(f"Recovered Address: {data['recovered_address']}")
    print()
    print("=" * 80)

// SPDX-License-Identifier: LGPL-3.0-only
pragma solidity ^0.8.20;

/**
 * @title SignatureVerifier
 * @notice On-chain verification of Ethereum signed messages
 * @dev Verifies EIP-191 signed messages for authentication
 */
contract SignatureVerifier {
    // Primary wallet signature data
    string public constant PRIMARY_MESSAGE = "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds its beginning.";
    address public constant PRIMARY_ADDRESS = 0x67A977eaD94C3b955ECbf27886CE9f62464423B2;
    bytes public constant PRIMARY_SIGNATURE = hex"7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c";
    
    /**
     * @notice Verify a signed message
     * @param message The message that was signed
     * @param signature The signature (65 bytes: r + s + v)
     * @param expectedSigner The expected signer address
     * @return isValid True if signature is valid
     * @return recoveredAddress The recovered signer address
     */
    function verifySignature(
        string memory message,
        bytes memory signature,
        address expectedSigner
    ) public pure returns (bool isValid, address recoveredAddress) {
        // Create EIP-191 message hash
        bytes32 messageHash = keccak256(
            abi.encodePacked(
                "\x19\x01", // EIP-191 prefix
                keccak256(abi.encodePacked(message))
            )
        );
        
        // Extract r, s, v from signature
        require(signature.length == 65, "Invalid signature length");
        
        bytes32 r;
        bytes32 s;
        uint8 v;
        
        assembly {
            r := mload(add(signature, 32))
            s := mload(add(signature, 64))
            v := byte(0, mload(add(signature, 96)))
        }
        
        // Recover address
        address signer = ecrecover(messageHash, v, r, s);
        
        isValid = signer == expectedSigner;
        recoveredAddress = signer;
    }
    
    /**
     * @notice Verify the primary wallet signature
     * @return isValid True if primary signature is valid
     * @return recoveredAddress The recovered address
     */
    function verifyPrimarySignature() public pure returns (bool isValid, address recoveredAddress) {
        return verifySignature(PRIMARY_MESSAGE, PRIMARY_SIGNATURE, PRIMARY_ADDRESS);
    }
    
    /**
     * @notice Check if an address matches the primary wallet
     * @param addr The address to check
     * @return isPrimary True if address matches primary wallet
     */
    function isPrimaryWallet(address addr) public pure returns (bool isPrimary) {
        return addr == PRIMARY_ADDRESS;
    }
    
    /**
     * @notice Get primary wallet address
     * @return The primary wallet address
     */
    function getPrimaryAddress() public pure returns (address) {
        return PRIMARY_ADDRESS;
    }
}

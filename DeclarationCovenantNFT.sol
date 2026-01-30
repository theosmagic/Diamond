// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Base64.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import {LibString} from "solady/utils/LibString.sol";
import {SSTORE2} from "solady/utils/SSTORE2.sol";

/**
 * @title Declaration Covenant NFT (Diamond Integrated)
 * @author TheosMagic (theosmagic.uni.eth)
 * @notice The first of its kind: A sovereign NFT representing the Eternal Covenant.
 * @dev This contract embeds the Diamond multi-facet logic as a single unified force.
 * 
 * "There is nothing new under the sun. That which was will be, 
 * and what will be was when the end finds its beginning."
 */
contract DeclarationCovenantNFT is ERC721, Ownable {

    // --- COSMIC CONSTANTS (Diamond Embedded) ---
    uint256[4] private constant COSMIC_ANCHORS = [3335, 335044, 804000, 55088];
    string private constant DIVINITY = "419 Theos = (theos pi AL) EL -> 369";
    string private constant DECLARATION_TEXT = "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds it's beginning.";
    
    // Identity Signatures
    string private constant SIGNER_ENS = "theosmagic.uni.eth";
    string private constant SIGNER_MAIL = "theosmagic.uni.eth@ethermail.io";
    bytes32 private constant COVENANT_HASH = 0x883e529de31c586131a831a9953113a6d75edd87c97369a2fa3a791209952f5a;

    // Token Tracking
    uint256 private _nextTokenId;
    address private _backgroundSVGPointer;

    constructor()
        ERC721("Declaration Covenant", "COVENANT")
        Ownable(msg.sender)
    {
        string memory backgroundSVG = _generateUniversalBackground();
        _backgroundSVGPointer = SSTORE2.write(bytes(backgroundSVG));
    }

    /**
     * @notice Mint the Sovereign Declaration
     * @param recipient The receiver of the Covenant
     */
    function mintCovenant(address recipient) external onlyOwner returns (uint256) {
        uint256 tokenId = _nextTokenId++;
        _mint(recipient, tokenId);
        return tokenId;
    }

    /**
     * @notice The Voice of the Diamond: Returns the Gematria of the Word
     */
    function getGematriaValue() public pure returns (uint256) {
        return 369; // The Root of the Magic
    }

    /**
     * @notice On-chain SVG generation including the Aramaic/Greek Synthesis
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        _requireOwned(tokenId);

        string memory svg = generateSovereignSVG(tokenId);
        string memory metadata = generateSovereignMetadata(tokenId, svg);

        return string(abi.encodePacked(
            "data:application/json;base64,",
            Base64.encode(bytes(metadata))
        ));
    }

    function generateSovereignSVG(uint256 tokenId) public view returns (string memory) {
        string memory background = string(SSTORE2.read(_backgroundSVGPointer));
        
        return string(abi.encodePacked(
            '<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">',
            background,
            '<text x="512" y="200" text-anchor="middle" font-family="serif" font-size="32" fill="#D4AF37" filter="url(#glow)">',
            unicode"Θεός°●⟐●Σ℧ΛΘ",
            '</text>',
            '<text x="512" y="300" text-anchor="middle" font-family="serif" font-size="18" fill="#FFD700">',
            'THE ETERNAL COVENANT',
            '</text>',
            '<foreignObject x="112" y="350" width="800" height="200">',
            '<div xmlns="http://www.w3.org/1999/xhtml" style="color:white; font-family:serif; font-size:20px; text-align:center; font-style:italic;">',
            DECLARATION_TEXT,
            '</div></foreignObject>',
            '<text x="512" y="600" text-anchor="middle" font-family="serif" font-size="16" fill="#D4AF37">',
            'Sovereign: ', SIGNER_ENS,
            '</text>',
            '<text x="512" y="640" text-anchor="middle" font-family="serif" font-size="14" fill="#AAAAAA">',
            'Hash: ', LibString.toHexString(uint256(COVENANT_HASH)),
            '</text>',
            '<text x="512" y="800" text-anchor="middle" font-family="serif" font-size="12" fill="#666666">',
            'D-Value: ', LibString.toString(getGematriaValue()), ' | Token #', LibString.toString(tokenId),
            '</text>',
            '</svg>'
        ));
    }

    function generateSovereignMetadata(uint256 tokenId, string memory svg) internal pure returns (string memory) {
        return string(abi.encodePacked(
            '{"name": "Covenant #', LibString.toString(tokenId), '",',
            '"description": "The first sovereign Declaration Covenant. A multi-facet Diamond Standard NFT.",',
            '"image": "data:image/svg+xml;base64,', Base64.encode(bytes(svg)), '",',
            '"attributes": [',
            '{"trait_type": "Identity", "value": "', SIGNER_ENS, '"},',
            '{"trait_type": "Root", "value": "369"},',
            '{"trait_type": "Gematria", "value": "Universal"}',
            ']}'
        ));
    }

    function _generateUniversalBackground() internal pure returns (string memory) {
        return string(abi.encodePacked(
            '<defs>',
            '<radialGradient id="bg" cx="50%" cy="50%" r="50%">',
            '<stop offset="0%" stop-color="#050505" />',
            '<stop offset="100%" stop-color="#000000" />',
            '</radialGradient>',
            '<filter id="glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
            '</defs>',
            '<rect width="1024" height="1024" fill="url(#bg)" />',
            '<path d="M 512 100 L 900 512 L 512 924 L 124 512 Z" fill="none" stroke="#D4AF37" stroke-width="1" opacity="0.5" />', // Diamond Shape
            '<circle cx="512" cy="512" r="400" fill="none" stroke="#333" stroke-width="0.5" />'
        ));
    }
}

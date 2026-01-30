// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DiamondCutFacet
 * @notice Facet that enables diamond upgrades
 * @dev This is the ONLY way to modify the diamond structure
 * 
 * Core Principle: Single address, evolving structure
 * - Add new facets
 * - Replace existing facets  
 * - Remove facets
 * - All without changing the proxy address
 */

import {IDiamondCut} from "../interfaces/IDiamondCut.sol";
import {LibDiamond} from "../libraries/LibDiamond.sol";

contract DiamondCutFacet is IDiamondCut {
    /// @notice Add/replace/remove any number of functions and optionally execute
    ///         a function with delegatecall
    /// @param _diamondCut Contains the facet addresses and function selectors
    /// @param _init The address of the contract or facet to execute _calldata
    /// @param _calldata A function call, including function selector and arguments
    ///                  _calldata is executed with delegatecall on _init
    function diamondCut(
        FacetCut[] calldata _diamondCut,
        address _init,
        bytes calldata _calldata
    ) external override {
        LibDiamond.enforceIsContractOwner();
        LibDiamond.diamondCut(_diamondCut, _init, _calldata);
    }
}

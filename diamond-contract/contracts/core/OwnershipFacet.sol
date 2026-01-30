// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title OwnershipFacet
 * @notice Manages contract ownership
 * @dev Only owner can perform diamond cuts
 */

import {LibDiamond} from "../libraries/LibDiamond.sol";

contract OwnershipFacet {
    /// @notice Get the owner of the contract
    /// @return owner_ The address of the owner
    function owner() external view returns (address owner_) {
        owner_ = LibDiamond.contractOwner();
    }

    /// @notice Transfer ownership to a new address
    /// @param _newOwner The address of the new owner
    function transferOwnership(address _newOwner) external {
        LibDiamond.enforceIsContractOwner();
        LibDiamond.setContractOwner(_newOwner);
    }
}

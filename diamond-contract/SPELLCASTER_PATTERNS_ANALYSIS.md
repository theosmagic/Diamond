# 🔍 Spellcaster-Facets Pattern Analysis

## Overview

Analysis of Treasure's spellcaster-facets Diamond implementation to understand patterns for bridgeworld.lol integration and multi-chain expansion.

## Key Patterns Identified

### 1. Storage Pattern ✅

**Pattern**: Separate storage contracts with `layout()` function

```solidity
// Example: PaymentsStorage.sol
library PaymentsStorage {
    bytes32 constant PAYMENTS_STORAGE_POSITION = keccak256("payments.storage");
    
    struct PaymentsStorageStruct {
        // Storage variables
    }
    
    function layout() internal pure returns (PaymentsStorageStruct storage ds) {
        bytes32 position = PAYMENTS_STORAGE_POSITION;
        assembly {
            ds.slot := position
        }
    }
}
```

**Why**: 
- Prevents storage collisions
- Clean separation of concerns
- Easy to upgrade facets without touching storage

**Our Implementation**: ✅ Already using `LibDiamond` storage pattern

### 2. Library Pattern ✅

**Pattern**: Libraries interact with storage, facets call libraries

```solidity
// Example: LibPayments.sol
library LibPayments {
    function getERC20Info(address _erc20Addr) internal view returns (ERC20Info storage info_) {
        info_ = PaymentsStorage.layout().erc20ToInfo[_erc20Addr];
    }
    
    function setMagicAddress(address _magicAddress) internal {
        PaymentsStorage.layout().magicAddress = _magicAddress;
    }
}
```

**Why**:
- Reusable logic
- Clean facet code
- Centralized storage access

**Our Implementation**: ✅ Using `LibDiamond` library pattern

### 3. Facet Initialization Pattern ✅

**Pattern**: Facets use `FacetInitializable` for one-time initialization

```solidity
// Example: PaymentsFacet.sol
contract PaymentsFacet is PaymentsV1, PaymentsV2 {
    function PaymentsFacet_init(
        address _gasTokenUSDPriceFeed,
        address _magicAddress
    ) public facetInitializer(keccak256("PaymentsFacet_init")) {
        LibPayments.setGasTokenUSDPriceFeed(_gasTokenUSDPriceFeed);
        LibPayments.setMagicAddress(_magicAddress);
    }
}
```

**Why**:
- Prevents re-initialization
- Clean setup
- Can be called during diamondCut

**Our Implementation**: ⏳ Need to add initialization pattern

### 4. Payment System Pattern ✅

**Pattern**: Multi-token payment system with price feeds

**Features**:
- Supports ERC20 tokens (MAGIC, USDC, USDT)
- Supports gas tokens (ETH, MATIC, etc.)
- Price feeds for conversions (Chainlink)
- Multiple price types (STATIC, PRICED_IN_ERC20, PRICED_IN_USD, PRICED_IN_GAS_TOKEN)

**Key Functions**:
- `makeStaticERC20Payment()` - Direct ERC20 payment
- `makeStaticGasTokenPayment()` - Direct gas token payment
- `makeERC20PaymentByPriceType()` - Payment with conversion
- `calculatePaymentAmountByPriceType()` - Price calculation

**Our Implementation**: ⏳ Need to integrate payment system

### 5. Access Control Pattern ✅

**Pattern**: Role-based access control with collection-level permissions

**Features**:
- Owner (contract owner)
- Collection admins (per collection)
- Role-based functions

**Our Implementation**: ✅ Have `OwnershipFacet`, need collection-level access

### 6. Interface Pattern ✅

**Pattern**: Clear interfaces for each facet

**Example**:
- `IPayments.sol` - Payment interface
- `ISimpleCrafting.sol` - Crafting interface
- `IGuildManager.sol` - Guild interface

**Our Implementation**: ✅ Have interfaces, need to expand

### 7. Versioning Pattern ✅

**Pattern**: V1/V2 pattern for upgrades

**Example**:
- `PaymentsV1.sol` - Version 1
- `PaymentsV2.sol` - Version 2
- `PaymentsFacet.sol` - Combines both

**Why**:
- Backward compatibility
- Gradual migration
- Feature additions

**Our Implementation**: ⏳ Need versioning strategy

## Key Facets in Spellcaster

### Core Facets
1. **DiamondCutFacet** - Upgrade mechanism ✅
2. **DiamondLoupeFacet** - Query interface ✅
3. **OwnershipFacet** - Access control ✅

### Functional Facets
1. **PaymentsFacet** - Multi-token payments
2. **SimpleCraftingFacet** - Crafting system
3. **GuildManagerFacet** - Guild management
4. **GuildTokenFacet** - Guild tokens
5. **OrganizationFacet** - Organization management
6. **AccessControlFacet** - Role-based access
7. **CollectionAccessControlFacet** - Collection-level access
8. **PausableFacet** - Pause functionality
9. **MetaTxFacet** - Meta-transactions
10. **EmitterFacet** - Event emission
11. **ERC1155Facet** - ERC1155 functionality
12. **OffchainAssetVaultFacet** - Off-chain asset management

## Storage Libraries

- `LibDiamond` - Core diamond storage ✅
- `LibPayments` - Payment storage
- `LibSimpleCrafting` - Crafting storage
- `LibGuildManager` - Guild storage
- `LibGuildToken` - Guild token storage
- `LibOrganizationManager` - Organization storage
- `LibAccessControlRoles` - Access control storage
- `LibMeta` - Meta-transaction utilities
- `LibUtilities` - Utility functions

## Integration Points for Bridgeworld.lol

### 1. Payment System
- **Use**: PaymentsFacet pattern
- **Expand**: Add SAND, MANA support
- **Multi-chain**: Support different gas tokens per chain

### 2. Marketplace Integration
- **Use**: Collection access control pattern
- **Expand**: OpenSea, Magic Eden integration
- **Multi-chain**: Cross-chain marketplace

### 3. Crafting System
- **Use**: SimpleCrafting pattern
- **Expand**: Bridgeworld-specific crafting
- **Multi-chain**: Cross-chain crafting

### 4. Access Control
- **Use**: AccessControlFacet pattern
- **Expand**: Bridgeworld-specific roles
- **Multi-chain**: Cross-chain permissions

## Multi-Chain Considerations

### Current Implementation
- **Single Chain**: Arbitrum One (primary)
- **Payment Tokens**: MAGIC, USDC, USDT
- **Gas Token**: ETH (via Arbitrum)

### Expansion Needed
- **Multiple Chains**: Ethereum, Arbitrum, Polygon, Base
- **Multiple Tokens**: MAGIC, SAND, MANA, plus existing
- **Multiple Gas Tokens**: ETH, MATIC, etc.
- **Cross-Chain**: Bridge functionality

## Recommendations

### 1. Adopt Storage Pattern ✅
- Use separate storage contracts
- Use libraries for storage access
- Prevent storage collisions

### 2. Implement Facet Initialization ⏳
- Add `FacetInitializable` pattern
- One-time initialization
- Clean setup

### 3. Integrate Payment System ⏳
- Use PaymentsFacet pattern
- Expand to SAND, MANA
- Multi-chain support

### 4. Add Access Control ⏳
- Collection-level access
- Role-based permissions
- Multi-chain permissions

### 5. Versioning Strategy ⏳
- V1/V2 pattern
- Backward compatibility
- Gradual migration

## Next Steps

1. ✅ Understand patterns
2. ⏳ Implement storage pattern for our facets
3. ⏳ Add facet initialization
4. ⏳ Integrate payment system
5. ⏳ Add access control
6. ⏳ Plan multi-chain expansion

---

**Status**: Pattern analysis complete ✅  
**Next**: Multi-chain expansion plan

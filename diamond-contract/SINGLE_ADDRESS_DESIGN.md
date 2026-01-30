# 💎 Single Address Design - Core Foundation

## The Principle

**"ONE Address, Evolving Forever"**

The Diamond Contract maintains a **single contract address** that never changes, while its structure evolves through facet upgrades.

## Architecture

```
┌─────────────────────────────────────────────┐
│     Diamond Proxy (SINGLE ADDRESS)         │
│     ───────────────────────────────        │
│     Address: 0x... (NEVER CHANGES)         │
│                                             │
│     ┌─────────────────────────────────┐    │
│     │  Function Registry              │    │
│     │  ─────────────────────          │    │
│     │  function → facet mapping       │    │
│     └─────────────────────────────────┘    │
│                                             │
│     ┌─────────────────────────────────┐    │
│     │  Facet Registry                  │    │
│     │  ─────────────────────          │    │
│     │  List of all active facets       │    │
│     └─────────────────────────────────┘    │
└──────────────┬──────────────────────────────┘
               │
               │ delegatecall
               │
       ┌───────┴────────┐
       │                │
   ┌───▼───┐      ┌─────▼─────┐
   │ Facet │      │  Facet    │
   │  #1   │      │   #2      │
   │       │      │           │
   │ Trading│     │  Cosmic   │
   └───────┘      └───────────┘
```

## How It Works

### 1. Single Proxy Address
- **Diamond.sol** is deployed once
- Address is **permanent** and **never changes**
- All interactions use this same address

### 2. Facet-Based Evolution
- Facets are separate contracts
- Added via `diamondCut` function
- Removed/replaced via `diamondCut` function
- **Proxy address stays the same**

### 3. Function Routing
- Proxy receives function call
- Looks up function selector in registry
- Routes to appropriate facet via delegatecall
- Returns result to caller

### 4. Market Evolution
- New market needs? → Deploy new facet → Add via diamondCut
- Old feature obsolete? → Remove facet via diamondCut
- Feature needs update? → Replace facet via diamondCut
- **Address never changes**

## Core Contracts

### 1. Diamond.sol (Proxy)
- **Single address** - deployed once
- Handles all function calls
- Routes to facets
- Never changes

### 2. DiamondCutFacet.sol
- Enables upgrades
- Only owner can call
- Adds/removes/replaces facets
- Maintains registry

### 3. DiamondLoupeFacet.sol
- Query interface
- See installed facets
- See function mappings
- Transparency

### 4. OwnershipFacet.sol
- Manages ownership
- Controls diamond cuts
- Transfer ownership

### 5. DiamondTrading.sol (Facet)
- Trading functionality
- Added as a facet
- Can be upgraded independently
- Uses same proxy address

## Evolution Example

### Initial Deployment
```
Diamond Proxy: 0x1234...
Facets: [DiamondCutFacet, DiamondLoupeFacet, OwnershipFacet]
```

### Add Trading (Market Need)
```
diamondCut([
  {
    facetAddress: DiamondTradingFacet,
    action: Add,
    functionSelectors: [listDiamond, buyDiamond, ...]
  }
])

Diamond Proxy: 0x1234... (SAME ADDRESS)
Facets: [DiamondCutFacet, DiamondLoupeFacet, OwnershipFacet, DiamondTradingFacet]
```

### Update Trading (Market Change)
```
diamondCut([
  {
    facetAddress: DiamondTradingFacetV2,
    action: Replace,
    functionSelectors: [listDiamond, buyDiamond, ...]
  }
])

Diamond Proxy: 0x1234... (SAME ADDRESS)
Facets: [DiamondCutFacet, DiamondLoupeFacet, OwnershipFacet, DiamondTradingFacetV2]
```

### Remove Old Feature
```
diamondCut([
  {
    facetAddress: address(0),
    action: Remove,
    functionSelectors: [oldFunction]
  }
])

Diamond Proxy: 0x1234... (SAME ADDRESS)
Facets: [Updated list without old feature]
```

## Key Points

✅ **Single Address**: One proxy address, never changes  
✅ **Evolving Structure**: Facets can be added/removed/replaced  
✅ **Market Responsive**: Adapts to market needs without redeployment  
✅ **Self-Evolving**: Can upgrade based on conditions  
✅ **Live Contract**: Continuously upgradable  

## Integration with Trading

DiamondTrading integrates as a **facet**:
- Deployed separately
- Added to Diamond via diamondCut
- Uses same proxy address
- Can be upgraded independently
- Evolves with market needs

## Implementation Status

- ✅ Diamond.sol - Core proxy
- ✅ DiamondCutFacet.sol - Upgrade mechanism
- ✅ DiamondLoupeFacet.sol - Query interface
- ✅ OwnershipFacet.sol - Access control
- ✅ LibDiamond.sol - Storage library
- ✅ DiamondTrading.sol - Trading facet (needs integration)

## Next Steps

1. Integrate DiamondTrading as a facet
2. Create deployment script
3. Test upgrade mechanism
4. Deploy to testnet
5. Verify single address principle

---

**Remember**: The Diamond Contract is a **single address that evolves**. The proxy address is permanent, the facets are flexible. This is the core design principle that must never be broken.

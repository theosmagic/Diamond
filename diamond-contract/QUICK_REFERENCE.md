# 📚 Diamond Contract - Quick Reference

## Core Principle
**Single Address, Single Proxy, Evolving Structure**

## Key Documents

1. **CORE_DESIGN.md** - Core design principles
2. **SINGLE_ADDRESS_DESIGN.md** - Single address architecture
3. **THE_BIGGER_PICTURE.md** - Full ecosystem overview
4. **SPELLCASTER_PATTERNS_ANALYSIS.md** - Treasure's patterns
5. **MULTI_CHAIN_EXPANSION_PLAN.md** - Multi-chain strategy
6. **ALPHA_BETA_STRATEGY.md** - Fine-tuning strategy
7. **HOW_IT_WILL_FUNCTION.md** - Functionality guide
8. **22_CONTRACTS_MAPPING.md** - Contract to facet mapping

## Quick Commands

### Deploy Diamond
```solidity
Diamond diamond = new Diamond(owner, facets, initializations);
// Result: Single address that never changes
```

### Add Facet
```solidity
diamond.diamondCut([{
    facetAddress: newFacet,
    action: Add,
    functionSelectors: [...]
}], address(0), "");
```

### Replace Facet
```solidity
diamond.diamondCut([{
    facetAddress: newFacet,
    action: Replace,
    functionSelectors: [...]
}], address(0), "");
```

### Query Facets
```solidity
Facet[] memory facets = diamond.facets();
address facet = diamond.facetAddress(functionSelector);
```

## Networks

- **Arbitrum One** (42161) - Primary ✅
- **Ethereum** (1) - To deploy ⏳
- **Polygon** (137) - To deploy ⏳
- **Base** (8453) - To deploy ⏳

## Tokens

- **MAGIC** ✅ (Arbitrum)
- **SAND** ⏳ (Ethereum, Polygon)
- **MANA** ⏳ (Ethereum, Polygon)
- **USDC** ✅ (All chains)
- **USDT** ✅ (All chains)

## Marketplaces

- **OpenSea** ⏳ (All chains)
- **Magic Eden** ⏳ (Ethereum, Polygon)

## Status

- ✅ Core foundation complete
- ✅ Pattern analysis complete
- ⏳ Facet development in progress
- ⏳ Multi-chain expansion planned

---

**For detailed information, see individual documentation files.**

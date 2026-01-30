# 🌐 Multi-Chain Expansion Plan - Alpha/Pre-Beta

## Overview

Expansion plan for Diamond Contract across multiple chains, tokens, and marketplaces for bridgeworld.lol + TreasureDAO ecosystem.

## Target Networks

### Primary Networks
1. **Ethereum** (Mainnet)
   - Chain ID: 1
   - Gas Token: ETH
   - Status: ⏳ To deploy
   - Priority: High

2. **Arbitrum One** (Primary)
   - Chain ID: 42161
   - Gas Token: ETH (via Arbitrum)
   - Status: ✅ Current focus
   - Priority: Highest

3. **Polygon**
   - Chain ID: 137
   - Gas Token: MATIC
   - Status: ⏳ To deploy
   - Priority: High

4. **Base** (Coinbase)
   - Chain ID: 8453
   - Gas Token: ETH
   - Status: ⏳ To deploy (X402 contract already there)
   - Priority: High

## Target Tokens

### Native Tokens
1. **MAGIC** ✅
   - Network: Arbitrum One
   - Address: `0x539bdE0d7Dbd336b79148AA742883198BBF60342`
   - Status: Already integrated in spellcaster-facets
   - Priority: Highest

2. **SAND** (The Sandbox)
   - Network: Ethereum, Polygon
   - Status: ⏳ To integrate
   - Priority: High

3. **MANA** (Decentraland)
   - Network: Ethereum, Polygon
   - Status: ⏳ To integrate
   - Priority: High

### Stablecoins
- **USDC** ✅ (Already in spellcaster-facets)
- **USDT** ✅ (Already in spellcaster-facets)

## Target Marketplaces

### 1. OpenSea
- **Networks**: Ethereum, Arbitrum, Polygon, Base
- **Status**: ⏳ To integrate
- **Priority**: Highest
- **Features**:
  - ERC-721 support
  - ERC-1155 support
  - Royalty configuration
  - Collection verification

### 2. Magic Eden
- **Networks**: Ethereum, Polygon, Solana (future)
- **Status**: ⏳ To integrate
- **Priority**: High
- **Features**:
  - Multi-chain support
  - Collection management
  - Royalty system

## Architecture: Multi-Chain Diamond

### Option 1: Single Diamond Per Chain (Recommended for Alpha)
```
Ethereum Diamond (Address A)
    ↓
Facets: [Core, Trading, Payments, ...]

Arbitrum Diamond (Address B)
    ↓
Facets: [Core, Trading, Payments, ...]

Polygon Diamond (Address C)
    ↓
Facets: [Core, Trading, Payments, ...]

Base Diamond (Address D)
    ↓
Facets: [Core, Trading, Payments, ...]
```

**Pros**:
- Independent evolution per chain
- Chain-specific optimizations
- Easier deployment
- Lower risk

**Cons**:
- Different addresses per chain
- Cross-chain complexity

### Option 2: Cross-Chain Diamond (Future)
```
Diamond Proxy (Single Address Concept)
    ↓
Chain Router Facet
    ↓
┌───┴───┬───┴───┬───┴───┐
│ Eth  │ Arb  │ Poly │ Base │
└──────┴──────┴──────┴──────┘
```

**Pros**:
- Unified interface
- Cross-chain operations
- Single address concept

**Cons**:
- Complex implementation
- Bridge dependencies
- Higher risk

## Implementation Strategy: Alpha/Pre-Beta

### Phase 1: Single Chain (Arbitrum) ✅ IN PROGRESS
- **Goal**: Get Diamond working on Arbitrum
- **Status**: Foundation complete
- **Next**: Deploy and test

### Phase 2: Multi-Chain Deployment
- **Goal**: Deploy Diamond to each chain
- **Approach**: Same Diamond code, different addresses
- **Networks**: Ethereum, Polygon, Base
- **Timeline**: After Arbitrum stable

### Phase 3: Multi-Token Support
- **Goal**: Support MAGIC, SAND, MANA
- **Approach**: Extend PaymentsFacet pattern
- **Integration**: Price feeds, conversions
- **Timeline**: Parallel with Phase 2

### Phase 4: Marketplace Integration
- **Goal**: OpenSea + Magic Eden
- **Approach**: Marketplace facets
- **Features**: Listing, buying, royalties
- **Timeline**: After Phase 2-3

### Phase 5: Cross-Chain Bridge (Future)
- **Goal**: Unified cross-chain operations
- **Approach**: Bridge facets
- **Timeline**: Post-beta

## Facet Structure for Multi-Chain

### Core Facets (All Chains)
- DiamondCutFacet ✅
- DiamondLoupeFacet ✅
- OwnershipFacet ✅
- PaymentsFacet (Multi-token) ⏳

### Chain-Specific Facets
- **EthereumFacet** - Ethereum-specific functions
- **ArbitrumFacet** - Arbitrum-specific functions
- **PolygonFacet** - Polygon-specific functions
- **BaseFacet** - Base-specific functions

### Token Facets
- **MagicTokenFacet** - MAGIC token operations ✅
- **SandTokenFacet** - SAND token operations ⏳
- **ManaTokenFacet** - MANA token operations ⏳

### Marketplace Facets
- **OpenSeaFacet** - OpenSea integration ⏳
- **MagicEdenFacet** - Magic Eden integration ⏳
- **TradingFacet** - General trading (DiamondTrading) ✅

## Payment System Expansion

### Current (spellcaster-facets)
```solidity
// Supports:
- MAGIC token ✅
- USDC ✅
- USDT ✅
- Gas tokens (ETH, MATIC) ✅
- Price feeds (Chainlink) ✅
```

### Expansion Needed
```solidity
// Add support for:
- SAND token ⏳
- MANA token ⏳
- Chain-specific tokens ⏳
- Cross-chain price feeds ⏳
```

### Implementation
```solidity
// Extend PaymentsFacet
contract PaymentsFacetV2 is PaymentsV1 {
    // Add SAND support
    function initializeSAND(address _sandAddress, address _priceFeed) external;
    
    // Add MANA support
    function initializeMANA(address _manaAddress, address _priceFeed) external;
    
    // Multi-chain price feeds
    function setChainPriceFeed(uint256 _chainId, address _priceFeed) external;
}
```

## Marketplace Integration Strategy

### OpenSea Integration

**Requirements**:
- ERC-721 compliance
- ERC-1155 compliance
- Royalty standard (EIP-2981)
- Collection metadata

**Facet Structure**:
```solidity
contract OpenSeaFacet {
    // OpenSea-specific functions
    function setOpenSeaProxy(address _proxy) external;
    function setRoyaltyInfo(uint256 _tokenId, address _recipient, uint256 _feeBps) external;
    function getRoyaltyInfo(uint256 _tokenId) external view returns (address, uint256);
}
```

### Magic Eden Integration

**Requirements**:
- Multi-chain support
- Collection management
- Royalty system

**Facet Structure**:
```solidity
contract MagicEdenFacet {
    // Magic Eden-specific functions
    function setMagicEdenRegistry(address _registry) external;
    function registerCollection(uint256 _chainId, address _collection) external;
    function getCollectionInfo(uint256 _chainId, address _collection) external view returns (CollectionInfo memory);
}
```

## Fine-Tuning Strategy (Alpha/Pre-Beta)

### 1. Monitoring & Analytics
- **Track**: Facet usage, gas costs, errors
- **Tools**: Events, subgraphs, analytics
- **Goal**: Identify optimization opportunities

### 2. Iterative Upgrades
- **Process**: Deploy → Monitor → Upgrade → Repeat
- **Frequency**: Weekly/bi-weekly during alpha
- **Method**: diamondCut for upgrades

### 3. A/B Testing
- **Approach**: Deploy multiple facet versions
- **Compare**: Performance, gas costs, user experience
- **Select**: Best performing version

### 4. User Feedback
- **Collect**: User feedback on functionality
- **Prioritize**: High-impact improvements
- **Implement**: Via facet upgrades

### 5. Gas Optimization
- **Monitor**: Gas costs per function
- **Optimize**: Storage, loops, external calls
- **Upgrade**: Replace facets with optimized versions

## Deployment Checklist

### Per Chain Deployment
- [ ] Deploy Diamond proxy
- [ ] Deploy core facets (Cut, Loupe, Ownership)
- [ ] Deploy PaymentsFacet with chain-specific tokens
- [ ] Deploy TradingFacet
- [ ] Deploy marketplace facets (OpenSea, Magic Eden)
- [ ] Initialize facets
- [ ] Verify contracts
- [ ] Test functionality
- [ ] Monitor performance

### Multi-Token Setup
- [ ] Configure MAGIC token (Arbitrum)
- [ ] Configure SAND token (Ethereum, Polygon)
- [ ] Configure MANA token (Ethereum, Polygon)
- [ ] Set up price feeds (Chainlink)
- [ ] Test conversions
- [ ] Monitor prices

### Marketplace Setup
- [ ] Configure OpenSea (all chains)
- [ ] Configure Magic Eden (Ethereum, Polygon)
- [ ] Set royalty standards
- [ ] Register collections
- [ ] Test listings
- [ ] Test purchases

## Network-Specific Configurations

### Ethereum Mainnet
- **Gas Token**: ETH
- **Tokens**: SAND, MANA, USDC, USDT
- **Marketplaces**: OpenSea, Magic Eden
- **RPC**: Infura/Alchemy
- **Explorer**: Etherscan

### Arbitrum One
- **Gas Token**: ETH (via Arbitrum)
- **Tokens**: MAGIC, USDC, USDT
- **Marketplaces**: OpenSea
- **RPC**: Arbitrum RPC
- **Explorer**: Arbiscan

### Polygon
- **Gas Token**: MATIC
- **Tokens**: SAND, MANA, USDC, USDT
- **Marketplaces**: OpenSea, Magic Eden
- **RPC**: Polygon RPC
- **Explorer**: Polygonscan

### Base
- **Gas Token**: ETH
- **Tokens**: USDC (native), others
- **Marketplaces**: OpenSea
- **RPC**: Base RPC
- **Explorer**: Basescan

## Alpha/Pre-Beta Timeline

### Week 1-2: Arbitrum Foundation
- Deploy Diamond on Arbitrum
- Test core functionality
- Monitor performance

### Week 3-4: Multi-Token Support
- Add SAND support
- Add MANA support
- Test conversions

### Week 5-6: Multi-Chain Deployment
- Deploy to Ethereum
- Deploy to Polygon
- Deploy to Base

### Week 7-8: Marketplace Integration
- OpenSea integration
- Magic Eden integration
- Test listings/purchases

### Week 9+: Fine-Tuning
- Monitor all chains
- Optimize gas costs
- Iterate based on feedback

## Success Metrics

### Technical
- ✅ Single address per chain maintained
- ✅ Facet upgrades working
- ✅ Multi-token payments functional
- ✅ Marketplace integrations working
- ✅ Gas costs optimized

### Business
- ✅ Trading volume > 0
- ✅ Multiple chains active
- ✅ Multiple tokens supported
- ✅ Marketplace listings live
- ✅ User adoption growing

---

**Status**: Planning phase  
**Next**: Implement multi-token payment system  
**Focus**: Alpha/pre-beta fine-tuning capability

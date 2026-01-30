# 📋 22 Core Contracts → Diamond Facets Mapping

## Overview

The 22 TreasureDAO contracts mapped to Aramaic glyphs (𐡀 to 𐡕) will become Diamond facets, maintaining the single address principle while enabling evolution.

## Foundation Layer (𐡀-𐡄) - The Root

### 𐡀 Aleph - MAGIC Token Facet
- **Contract**: MAGIC Token (ERC-20)
- **Address**: `0x539bdE0d7Dbd336b79148AA742883198BBF60342`
- **Function**: Core ecosystem token, The Source
- **Facet Functions**:
  - `transfer()`, `approve()`, `balanceOf()`, `totalSupply()`
- **Status**: ⏳ To be created

### 𐡁 Beth - Treasure NFT Facet
- **Contract**: Treasure NFT (ERC-721)
- **Address**: `0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18326`
- **Function**: Core NFT collection, The House
- **Facet Functions**:
  - `mint()`, `transfer()`, `ownerOf()`, `tokenURI()`
- **Status**: ⏳ To be created

### 𐡂 Gimel - TreasureFarm Facet
- **Contract**: TreasureFarm (Staking)
- **Address**: `0x83a19AE12B07D82Df1b7AB63E2b0a75EaAfC9c97`
- **Function**: Staking mechanism, The Will
- **Facet Functions**:
  - `stake()`, `unstake()`, `getStake()`, `claimRewards()`
- **Status**: ⏳ To be created

### 𐡃 Daleth - MagicPool2 Facet
- **Contract**: MagicPool2 (Liquidity)
- **Address**: `0xB0A5e5D09C91D6F2B1ac3d5B9e3e486a3A0E0B4A`
- **Function**: Liquidity pool, The Force
- **Facet Functions**:
  - `addLiquidity()`, `removeLiquidity()`, `swap()`
- **Status**: ⏳ To be created

### 𐡄 He - TreasureUnraveler Facet
- **Contract**: TreasureUnraveler (NFT)
- **Address**: `0x1C3D5c2e2b5c0e6e5c5b5c0e6e5c5b5c0e6e5c5b`
- **Function**: NFT unraveling, Life/Breath
- **Facet Functions**:
  - `unravel()`, `getUnraveled()`, `reconstruct()`
- **Status**: ⏳ To be created

## Operational Layer (𐡅-𐡍) - The Heart

### 𐡅 Vav - MagicClaim Facet
- **Contract**: MagicClaim (Claiming)
- **Function**: Token claiming, The Hook
- **Facet Functions**:
  - `claim()`, `getClaimable()`, `setClaimable()`
- **Status**: ⏳ To be created

### 𐡆 Zayin - Cards Facet
- **Contract**: Cards (ERC-721)
- **Function**: Card NFTs, Flow
- **Facet Functions**:
  - `mintCard()`, `playCard()`, `getCard()`
- **Status**: ⏳ To be created

### 𐡇 Heth - MagicWhitelist Facet
- **Contract**: MagicWhitelist (Access Control)
- **Function**: Access control, Will
- **Facet Functions**:
  - `addToWhitelist()`, `removeFromWhitelist()`, `isWhitelisted()`
- **Status**: ⏳ To be created

### 𐡈 Teth - TreasureMarketplace Facet ⭐
- **Contract**: TreasureMarketplace (Diamond)
- **Address**: `0x09986B4e255B3c548041a30A2Ee312Fe176731c2`
- **Function**: Main marketplace, Force
- **Status**: ✅ Already a Diamond - Integrate as facet
- **Note**: This is the existing Diamond marketplace

### 𐡉 Yodh - MarketplaceBuyer Facet
- **Contract**: MarketplaceBuyer (Facet)
- **Function**: Buyer facet, Demand
- **Facet Functions**:
  - `buy()`, `makeOffer()`, `cancelOffer()`
- **Status**: ⏳ To be created

### 𐡊 Kaph - MarketplaceSeller Facet
- **Contract**: MarketplaceSeller (Facet)
- **Function**: Seller facet, Supply
- **Facet Functions**:
  - `list()`, `updateListing()`, `cancelListing()`
- **Status**: ⏳ To be created

### 𐡋 Lamedh - MagicswapV2Router Facet
- **Contract**: MagicswapV2Router (AMM Router)
- **Address**: `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`
- **Function**: AMM router, BALANCE
- **Facet Functions**:
  - `swapExactTokensForTokens()`, `addLiquidity()`, `removeLiquidity()`
- **Status**: ⏳ To be created

### 𐡌 Mem - MagicswapV2Factory Facet
- **Contract**: MagicswapV2Factory (AMM Factory)
- **Function**: AMM factory, Void
- **Facet Functions**:
  - `createPair()`, `getPair()`, `allPairs()`
- **Status**: ⏳ To be created

### 𐡍 Nun - MagicswapV2Pair Facet
- **Contract**: MagicswapV2Pair (Trading Pair)
- **Function**: Trading pairs, Market
- **Facet Functions**:
  - `getReserves()`, `swap()`, `sync()`
- **Status**: ⏳ To be created

## Game Layer (𐡎-𐡑) - The Play

### 𐡎 Samekh - Legion Facet
- **Contract**: Legion (ERC-721)
- **Address**: `0xfE8c1ac365bA6780AEc5a985D989b327C27670A1`
- **Function**: Character NFTs, Work
- **Facet Functions**:
  - `mintLegion()`, `getLegion()`, `upgradeLegion()`
- **Status**: ⏳ To be created

### 𐡏 Ayin - Consumable Facet
- **Contract**: Consumable (ERC-1155)
- **Address**: `0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18327`
- **Function**: In-game items, Harvest
- **Facet Functions**:
  - `mint()`, `burn()`, `balanceOf()`, `safeTransferFrom()`
- **Status**: ⏳ To be created

### 𐡐 Pe - Harvester Facet
- **Contract**: Harvester (Resource Gathering)
- **Function**: Resource gathering, Seal
- **Facet Functions**:
  - `harvest()`, `getHarvestable()`, `claimHarvest()`
- **Status**: ⏳ To be created

### 𐡑 Sadhe - Extractor Facet
- **Contract**: Extractor (Resource Extraction)
- **Function**: Resource extraction, Return
- **Facet Functions**:
  - `extract()`, `getExtractable()`, `processExtraction()`
- **Status**: ⏳ To be created

## Governance Layer (𐡒-𐡕) - The Crown

### 𐡒 Qoph - BalancerCrystal Facet
- **Contract**: BalancerCrystal (Game Balance)
- **Function**: Game balance, The Holder
- **Facet Functions**:
  - `balance()`, `adjustBalance()`, `getBalance()`
- **Status**: ⏳ To be created

### 𐡓 Resh - gMAGIC Facet
- **Contract**: gMAGIC (Governance Token)
- **Function**: Governance token, Meta-layer
- **Facet Functions**:
  - `delegate()`, `getVotes()`, `transfer()`
- **Status**: ⏳ To be created

### 𐡔 Shin - TreasureDAO Facet
- **Contract**: TreasureDAO (Governance)
- **Function**: DAO governance, Sovereign
- **Facet Functions**:
  - `propose()`, `vote()`, `execute()`, `getProposal()`
- **Status**: ⏳ To be created

### 𐡕 Taw - ZKStackBridge Facet
- **Contract**: ZKStackBridge (Bridge)
- **Function**: ZKsync bridge, Completion
- **Facet Functions**:
  - `bridge()`, `claim()`, `getBridgeStatus()`
- **Status**: ⏳ To be created

## Integration Plan

### Step 1: Create Facet Contracts
- Convert each of 22 contracts to facet format
- Implement IDiamondCut compatible interfaces
- Map function selectors

### Step 2: Diamond Cut Operations
- Deploy facets
- Add to Diamond via diamondCut
- Maintain single address

### Step 3: Testing
- Test each facet independently
- Test facet interactions
- Test upgrade mechanism

### Step 4: Integration
- Connect bridgeworld.lol
- Integrate with Treasure ecosystem
- Connect 65 repos

## Current Status

- ✅ Diamond foundation complete
- ✅ Core contracts identified
- ⏳ Facet contracts to be created
- ⏳ Integration pending

---

**All 22 contracts will become facets of the single Diamond Contract, maintaining one address while enabling evolution.**

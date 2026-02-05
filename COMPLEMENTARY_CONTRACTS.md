# Complementary Contracts for Diamond System

Contracts that would enhance the existing Diamond infrastructure across Arbitrum, Ethereum, and Polygon.

---

## 1. ARBITRUM CORE INFRASTRUCTURE

### Bridge & Cross-Chain (L1 → Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| L1 Gateway Router | `0x72Ce9c846789fdB6fC1f34aC4AD25Dd9ef7031ef` | Token bridge routing |
| L1 ERC20 Gateway | `0xa3A7B6F88361F48403514059F1F16C8E78d60EeC` | Standard token bridge |
| L1 Custom Gateway | `0xcEe284F754E854890e311e3280b767F80797180d` | Custom token bridge |
| L1 WETH Gateway | `0xd92023E9d9911199a6711321D1277285e6d4e2db` | ETH bridging |
| Delayed Inbox | `0x4Dbd4fc535Ac27206064B68FfCf827b0A60BAB3f` | L1→L2 messaging |
| Bridge | `0x8315177aB297bA92A06054cE80a67Ed4DBd7ed3a` | Core bridge |
| Outbox | `0x0B9857ae2D4A3DBe74ffE1d7DF045bb7F96E4840` | L2→L1 messaging |

### Arbitrum L2 Contracts

| Contract | Address | Purpose |
|----------|---------|---------|
| L2 Gateway Router | `0x5288c571Fd7aD117beA99bF60FE0846C4E84F933` | L2 token routing |
| L2 ERC20 Gateway | `0x09e9222E96E7B4AE2a407B98d48e330053351EEe` | L2 token gateway |
| L2 WETH | `0x82aF49447D8a07e3bd95BD0d56f35241523fBab1` | Wrapped ETH on Arb |
| L2 Multicall | `0x842eC2c7D803033Edf55E478F461FC547Bc54EB2` | Batch calls |

### Arbitrum Precompiles (System Contracts)

| Contract | Address | Purpose |
|----------|---------|---------|
| ArbSys | `0x0000000000000000000000000000000000000064` | System info |
| ArbInfo | `0x0000000000000000000000000000000000000065` | Block info |
| ArbAddressTable | `0x0000000000000000000000000000000000000066` | Address compression |
| ArbGasInfo | `0x000000000000000000000000000000000000006C` | Gas pricing |
| ArbRetryableTx | `0x000000000000000000000000000000000000006E` | Retryable tickets |
| ArbOwner | `0x0000000000000000000000000000000000000070` | Chain owner |
| ArbWasm | `0x0000000000000000000000000000000000000071` | Stylus WASM |
| NodeInterface | `0x00000000000000000000000000000000000000C8` | Node queries |

---

## 2. TOP DEFI TOKENS (Arbitrum)

### Stablecoins

| Token | Address | Market Cap |
|-------|---------|------------|
| USDC (Native) | `0xaf88d065e77c8cc2239327c5edb3a432268e5831` | $4.29B |
| USDC.e (Bridged) | `0xff970a61a04b1ca14834a43f5de4533ebddb5cc8` | $115M |
| USDT (USD₮0) | `0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9` | $827M |
| DAI | `0xda10009cbd5d07dd0cecc66161fc93d7c9000da1` | $20.9M |
| FRAX | `0x17fc002b466eec40dae837fc4be5c67993ddbd6f` | $16.5M |
| USDe | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` | $2.18M |
| GHO (Aave) | `0x7dff72693f6a4149b17e7c6314655f6a9f7c8b33` | $897K |
| crvUSD | `0x498bf2b1e120fed3ad3d42ea2165e9b73f99c1e5` | $4.56M |

### Governance & Utility

| Token | Address | Purpose |
|-------|---------|---------|
| ARB | `0x912ce59144191c1204e64559fe8253a0e49e6548` | Arbitrum governance |
| LINK | `0xf97f4df75117a78c1a5a0dbb814af92458539fb4` | Chainlink oracle |
| UNI | `0xfa7f8980b0f1e64a2062791cc3b0871572f1f7f0` | Uniswap governance |
| GRT | `0x9623063377ad1b27544c965ccd7342f7ea7e88c7` | The Graph indexing |
| LDO | `0x13ad51ed4f1b7e9dc168d8a00cb3f4ddd85efa60` | Lido governance |
| CRV | `0x11cdb42b0eb46d95f990bedd4695a6e3fa034978` | Curve governance |
| PENDLE | `0x0c880f6761f1af8d9aa9c466984b80dab9a8c9e8` | Yield trading |
| ZRO | `0x6985884c4392d348587b19cb9eaaf157f13271cd` | LayerZero |
| GNO | `0xa0b862f60edef4452f25b4160f177db44deb6cf1` | Gnosis/Safe |
| ENA | `0x58538e6a46e07434d7e7375bc268d3cb839c0133` | Ethena |

### Wrapped/Staked Assets

| Token | Address | Purpose |
|-------|---------|---------|
| WETH | `0x82af49447d8a07e3bd95bd0d56f35241523fbab1` | Wrapped ETH |
| WBTC | `0x2f2a2543b76a4166549f7aab2e75bef0aefc5b0f` | Wrapped BTC |
| wstETH | `0x0fBcbaEA96Ce0cF7Ee00A8c19c3ab6f5Dc8E1921` | Lido staked ETH |
| ezETH | `0x2416092f143378750bb29b79ed961ab195cceea5` | Renzo restaked ETH |
| weETH | `0x35751007a407ca6feffe80b3cb397736d2cf4dbe` | ether.fi wrapped |
| cbBTC | `0xcbb7c0000ab88b473b1f5afd9ef808440eed33bf` | Coinbase BTC |
| tBTC | `0x6c84a8f1c29108F47a79964b5Fe888D4f4D0dE40` | Threshold BTC |
| SolvBTC | `0x3647c54c4c2c65bc7a2d63c0da2809b399dbbdc0` | Solv BTC |

---

## 3. DEFI PROTOCOLS

### Aave V3 (Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| Pool | `0x794a61358D6845594F94dc1DB02A252b5b4814aD` | Main lending pool |
| PoolDataProvider | `0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654` | Pool data |
| Oracle | `0xb56c2F0B653B2e0b10C9b928C8580Ac5Df02C7C7` | Price oracle |
| aArbGHO | `0xebe517846d0f36eced99c735cbf6131e1feb775d` | GHO aToken |

### Uniswap V3 (Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| Factory | `0x1F98431c8aD98523631AE4a59f267346ea31F984` | Pool factory |
| SwapRouter | `0xE592427A0AEce92De3Edee1F18E0157C05861564` | Swap router |
| SwapRouter02 | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` | Router v2 |
| QuoterV2 | `0x61fFE014bA17989E743c5F6cB21bF9697530B21e` | Price quotes |
| PositionsNFT | `0xC36442b4a4522E871399CD717aBDD847Ab11FE88` | LP positions |

### GMX (Arbitrum Native)

| Contract | Address | Purpose |
|----------|---------|---------|
| Vault | `0x489ee077994B6658eAfA855C308275EAd8097C4A` | GMX vault |
| Router | `0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064` | Trading router |
| GLP | `0x4277f8F2c384827B5273592FF7CeBd9f2C1ac258` | GLP token |
| GMX | `0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a` | GMX token |

### Curve Finance (Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| AddressProvider | `0x0000000022D53366457F9d5E68Ec105046FC4383` | Registry |
| Router | `0xF0d4c12A5768D806021F80a262B4d39d26C58b8D` | Swap router |
| crvUSD Controller | `0x498bf2b1e120fed3ad3d42ea2165e9b73f99c1e5` | crvUSD |

### Pendle Finance

| Contract | Address | Purpose |
|----------|---------|---------|
| Router | `0x00000000005BBB0EF59571E58418F9a4357b68A0` | Main router |
| MarketFactory | `0x2FCb47B58350cD377f94d3821e7373Df60bD9Ced` | Market creation |

---

## 4. NFT & GAMING INFRASTRUCTURE

### OpenSea / Seaport

| Contract | Address | Network | Purpose |
|----------|---------|---------|---------|
| Seaport 1.5 | `0x00000000000000ADc04C56Bf30aC9d3c0aAF14dC` | Multi | NFT exchange |
| Seaport 1.6 | `0x0000000000000068F116a894984e2DB1123eB395` | Multi | Latest exchange |
| ConduitController | `0x00000000F9490004C11Cef243f5400493c00Ad63` | Multi | Approvals |

### Reservoir (NFT Aggregator)

| Contract | Address | Purpose |
|----------|---------|---------|
| Router | `0x7C9F4C87d911613FE9ca58b579f737911AAD2D43` | NFT routing |
| SeaportModule | `0x00000000004DA12f1A193A0C56C01E8F24F8A2c6` | Seaport integration |

### Treasure Ecosystem (Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| Bridgeworld Legions | `0xfe8c1ac365ba6780aec5a985d989b327c27670a1` | Legion NFTs |
| MAGIC Token | `0x539bdE0d7Dbd336b79148AA742883198BBF60342` | MAGIC governance |
| TreasureMarketplace | `0x2E3b85F85628301a0Bce300Dee3A6B04195A15Ee` | NFT marketplace |
| Atlas Mine | `0xA0A89db1C899c49F98E6326b764BAFcf167fC2CE` | Staking |

---

## 5. ORACLES & DATA

### Chainlink (Arbitrum)

| Contract | Address | Purpose |
|----------|---------|---------|
| ETH/USD | `0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612` | Price feed |
| BTC/USD | `0x6ce185860a4963106506C203335A5812f87eCa5b` | Price feed |
| LINK/USD | `0x86E53CF1B870786351Da77A57575e79CB55812CB` | Price feed |
| ARB/USD | `0xb2A824043730FE05F3DA2efaFa1CBbe83fa548D6` | Price feed |
| Automation Registry | `0x75c0530885F385721fddA23C539AF3701d6183D4` | Keepers |
| VRF Coordinator | `0x41034678D6C633D8a95c75e1138A360a28bA15d1` | Randomness |

### The Graph

| Contract | Address | Purpose |
|----------|---------|---------|
| GRT Token | `0x9623063377ad1b27544c965ccd7342f7ea7e88c7` | Graph token |
| Staking | `0x00669A4CF01450B64E8A2A20E9b1FCB71E61eF03` | GRT staking |

### Pyth Network

| Contract | Address | Purpose |
|----------|---------|---------|
| Pyth | `0xff1a0f4744e8582DF1aE09D5611b887B6a12925C` | Price feeds |
| PYTH Token | `0xE4D5c6aE46ADFAF04313081e8C0052A30b6Dd724` | Governance |

---

## 6. CROSS-CHAIN & BRIDGES

### Coinweb (12-Point Star Routing)

| Component | Chain/ID | Role |
|-----------|----------|------|
| Ethereum | `1` | APEX_CONSTANT - The Source |
| Arbitrum | `42161` | SOVEREIGN_BRIDGE - The Execution |
| Polygon | `137` | DATA_STABILIZER - The Witness |
| Base | `8453` | LIQUIDITY_FOUNDATION - The Flow |
| CoinWeb L2 | TBD | ADMINISTRATIVE_ADULT - The Control |
| Cosmos/Evmos | `9001` | INTERCHAIN_HARMONY - IBC Interop |
| Gnosis | `100` | CROSS_CHAIN_SAFE - Security |
| Enjin | `1110` | NFT_MATRIX_ANCHOR - NFT Infrastructure |

**Coinweb Features:**
- **Gas Abstraction**: Pay once in CWEB token, abstracted across all chains
- **Multi-Chain Routing**: 12-point star system (6 clockwise, 6 counter-clockwise)
- **Identity Binding**: Covenant-based cross-chain identity continuity
- **Universal Routing**: Optimal path calculation through star topology
- **Cosmos/IBC**: Full Cosmos ecosystem access via Axelar gateway
- **Enjin NFTs**: Native NFT bridging to Enjin Matrixchain

| Contract | Address | Purpose |
|----------|---------|---------|
| CWEB Token | `0x505b5eda5e25a67e1c24a2bf1a527ed9eb88bf04` | Coinweb governance (ETH) |
| LayerZero Endpoint | `0x3c2269811836af69497E5F486A85D7316753cf62` | Cross-chain messaging |
| Stargate Router | `0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614` | Token bridging |
| Across SpokePool | `0xe35e9842fceaCA96570B734083f4a58e8F7C5f2A` | Fast bridging |
| Axelar Gateway | `0xe432150cce91c13a887f7D836923d5597adD8E31` | Cosmos/IBC bridge |
| Axelar Gas Service | `0x2d5d7d31F671F86C782533cc367F14109a082712` | Cross-chain gas |
| Enjin Bridge | `0x3E5A2A2741B3F4DfB3e1F85E81fC3A76F0A4DE8c` | Enjin Matrixchain |
| ENJ Token | `0x7A58c0Be72BE218B41C608b7Fe7C5bB630736C71` | ENJ on Arbitrum |

### LayerZero

| Contract | Address | Purpose |
|----------|---------|---------|
| Endpoint | `0x3c2269811836af69497E5F486A85D7316753cf62` | LZ endpoint |
| ZRO Token | `0x6985884c4392d348587b19cb9eaaf157f13271cd` | LZ governance |
| OFT | Various | Omnichain tokens |

### Stargate

| Contract | Address | Purpose |
|----------|---------|---------|
| Router | `0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614` | Bridge router |
| Factory | `0x55bDb4164D28FBaF0898e0eF14a589ac09Ac9970` | Pool factory |

### Across Protocol

| Contract | Address | Purpose |
|----------|---------|---------|
| SpokePool | `0xe35e9842fceaCA96570B734083f4a58e8F7C5f2A` | Arbitrum spoke |
| HubPool | `0xc186fA914353c44b2E33eBE05f21846F1048bEda` | Main hub |

### Synapse

| Contract | Address | Purpose |
|----------|---------|---------|
| Bridge | `0x6F4e8eBa4D337f874Ab57478AcC2Cb5BACdc19c9` | Synapse bridge |
| Router | `0x7E7A0e201FD38d3ADAA9523Da6C109a07118C96a` | Swap router |

---

## 7. ACCOUNT ABSTRACTION & WALLETS

### Safe (Gnosis Safe)

| Contract | Address | Purpose |
|----------|---------|---------|
| SafeProxyFactory | `0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2` | Create Safes |
| SafeSingleton | `0xd9Db270c1B5E3Bd161E8c8503c55cEABeE709552` | Safe logic |
| MultiSend | `0xA238CBeb142c10Ef7Ad8442C6D1f9E89e07e7761` | Batch txs |
| FallbackHandler | `0xf48f2B2d2a534e402487b3ee7C18c33Aec0Fe5e4` | Fallback |

### ERC-4337 (Account Abstraction)

| Contract | Address | Purpose |
|----------|---------|---------|
| EntryPoint | `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789` | AA entrypoint |
| SimpleAccountFactory | `0x9406Cc6185a346906296840746125a0E44976454` | Account factory |

### Ambire Smart Wallet

| Contract | Address | Purpose |
|----------|---------|---------|
| Ambire Factory | `0xBf07a0Df119Ca234634588fbDb5625594E2a5BCA` | Wallet deployment |
| Ambire Paymaster | `0x942f9CE5D9a33a82F88D233AEb3292E680230348` | Gas sponsorship |
| WALLET Token | `0x0e5F21bf1166Fb663a7B5EBe00E9C9F937a67294` | Governance token |

**Ambire Features:**
- **Smart Contract Wallet**: Upgradeable, recoverable, multi-sig capable
- **Gas Abstraction**: Pay gas in any token via paymaster
- **Batch Transactions**: Execute multiple calls in single tx
- **Privilege System**: Granular permission control
- **ERC-4337 Compatible**: Native account abstraction support

---

## 8. GOVERNANCE & DAO

### Arbitrum DAO

| Contract | Address | Purpose |
|----------|---------|---------|
| ARB Token | `0x912ce59144191c1204e64559fe8253a0e49e6548` | Governance token |
| Governor | `0x789fC99093B09aD01C34DC7251D0C89ce743e5a4` | Core governor |
| Timelock | `0x34d45e99f7D8c45ed05B5cA72D54bbD1fb3F98f0` | Execution delay |
| Treasury | `0xF3FC178157fb3c87548bAA86F9d24BA38E649B58` | DAO treasury |

### Snapshot (Off-chain)

| Integration | Purpose |
|-------------|---------|
| Snapshot.org | Off-chain voting |
| ENS Integration | Identity |

---

## 9. YIELD & STAKING

### Lido (Liquid Staking)

| Contract | Address | Purpose |
|----------|---------|---------|
| wstETH | `0x0fBcbaEA96Ce0cF7Ee00A8c19c3ab6f5Dc8E1921` | Wrapped stETH |
| LDO | `0x13ad51ed4f1b7e9dc168d8a00cb3f4ddd85efa60` | Governance |

### Rocket Pool

| Contract | Address | Purpose |
|----------|---------|---------|
| rETH | `0xEC70Dcb4A1EFa46b8F2D97C310C9c4790ba5ffA8` | Rocket ETH |

### EigenLayer

| Contract | Address | Purpose |
|----------|---------|---------|
| StrategyManager | `0x858646372CC42E1A627fcE94aa7A7033e7CF075A` | Restaking |
| EigenPod | Various | Validator pods |

---

## 10. RECOMMENDED INTEGRATION PRIORITY

### High Priority (Direct Value)

1. **Coinweb** - 10-point star cross-chain routing, gas abstraction
2. **Uniswap V3** - Swap/liquidity for MAGIC, ETH, stables
3. **Aave V3** - Lending/borrowing integration
4. **Chainlink** - Price feeds for all assets
5. **LayerZero** - Cross-chain messaging for multi-chain Diamond
6. **Safe** - Multisig for treasury management

### Medium Priority (Ecosystem)

7. **Treasure Marketplace** - NFT trading for Legions/Treasures
8. **GMX** - Perpetuals and GLP yield
9. **Pendle** - Yield tokenization
10. **Curve** - Stable swaps and crvUSD
11. **Arbitrum Bridge** - L1↔L2 asset movement

### Lower Priority (Future)

12. **EigenLayer** - Restaking integration
13. **Account Abstraction** - Gasless transactions
14. **The Graph** - Indexing for Diamond data
15. **Pyth** - Alternative oracle data

---

## Quick Reference: Key Addresses

```solidity
// Arbitrum Core
address constant ARB_TOKEN = 0x912ce59144191c1204e64559fe8253a0e49e6548;
address constant WETH = 0x82aF49447D8a07e3bd95BD0d56f35241523fBab1;
address constant USDC = 0xaf88d065e77c8cc2239327c5edb3a432268e5831;

// DeFi
address constant UNISWAP_ROUTER = 0xE592427A0AEce92De3Edee1F18E0157C05861564;
address constant AAVE_POOL = 0x794a61358D6845594F94dc1DB02A252b5b4814aD;

// Oracles
address constant CHAINLINK_ETH_USD = 0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612;
address constant CHAINLINK_REGISTRY = 0x75c0530885F385721fddA23C539AF3701d6183D4;

// Gaming
address constant MAGIC_TOKEN = 0x539bdE0d7Dbd336b79148AA742883198BBF60342;
address constant BRIDGEWORLD_LEGIONS = 0xfe8c1ac365ba6780aec5a985d989b327c27670a1;

// Cross-Chain (Coinweb 10-Point Star)
address constant LZ_ENDPOINT = 0x3c2269811836af69497E5F486A85D7316753cf62;
address constant STARGATE_ROUTER = 0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614;
address constant ACROSS_SPOKE_POOL = 0xe35e9842fceaCA96570B734083f4a58e8F7C5f2A;
bytes32 constant COVENANT_HASH = 0x883e529de31c586131a831a9953113a6d75edd87c97369a2fa3a791209952f5a;

// Infrastructure
address constant SAFE_FACTORY = 0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2;
address constant ENTRYPOINT_4337 = 0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789;
```

---

*Compiled for Diamond System Enhancement*
*Chain: Arbitrum One (42161)*
*Last Updated: 2026-02-05*

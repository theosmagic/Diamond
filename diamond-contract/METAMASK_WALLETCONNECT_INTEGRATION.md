# MetaMask SDK + WalletConnect Integration - Official Patterns
## Based on Official Repositories

**MetaMask SDK**: https://github.com/MetaMask/metamask-sdk  
**WalletConnect AppKit**: https://github.com/reown-com/appkit (formerly Web3Modal)  
**Status**: Updated to match official patterns

---

## 🔍 Official Repositories Analyzed

### MetaMask SDK

**Repository**: https://github.com/MetaMask/metamask-sdk

**Key Packages**:
- `@metamask/sdk` - Core SDK
- `@metamask/sdk-react` - React hooks (recommended)
- `@metamask/sdk-react-ui` - React UI components
- `@metamask/sdk-multichain` - Multi-chain support
- Wagmi integration (recommended approach)

**Features**:
- Session persistence
- Multi MetaMask provider (extension + mobile)
- Batch RPC calls
- Read-only RPC calls
- Infura integration
- **Wagmi hook integration** (alpha, recommended)

**Documentation**: https://docs.metamask.io/sdk/

### WalletConnect AppKit (formerly Web3Modal)

**Repository**: https://github.com/reown-com/appkit

**Note**: WalletConnect has migrated from `@walletconnect/modal` to **AppKit** (Reown AppKit)

**Key Packages**:
- `@reown/appkit` - Core AppKit
- `@reown/appkit-adapter-wagmi` - Wagmi adapter
- `@reown/appkit-react` - React components
- `@reown/appkit-core` - Core functionality

**Features**:
- Multi-chain support (EVM, Solana, Bitcoin)
- Multi-wallet support
- Smart Accounts
- Swaps & On-Ramp
- Social & Email login
- Sponsored transactions

**Documentation**: https://docs.reown.com/appkit/

---

## ✅ Updated Integration

### Recommended Approach: Wagmi + MetaMask SDK + AppKit

**Best Practice**: Use Wagmi as the foundation, with MetaMask SDK and AppKit as connectors.

### Package Structure

```json
{
  "dependencies": {
    // Wagmi (Foundation)
    "wagmi": "^2.5.0",
    "viem": "^2.0.0",
    "@tanstack/react-query": "^5.0.0",
    
    // MetaMask SDK (Recommended)
    "@metamask/sdk": "^0.18.0",
    "@metamask/sdk-react": "^0.18.0",
    
    // WalletConnect AppKit (Reown)
    "@reown/appkit": "^1.0.0",
    "@reown/appkit-adapter-wagmi": "^1.0.0",
    "@reown/appkit-react": "^1.0.0",
    
    // Safe{Wallet}
    "@safe-global/safe-core-sdk": "^4.0.0",
    "@safe-global/safe-ethers-lib": "^4.0.0",
    "@safe-global/safe-deployments": "^1.0.0",
    
    // React
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

---

## 🏗️ Integration Architecture

### Recommended Flow (Wagmi-Based)

```
User
    ↓
Wagmi (State Management)
    ├─► MetaMask SDK (via Wagmi connector)
    ├─► WalletConnect AppKit (via Wagmi connector)
    └─► Safe{Wallet} (via Wagmi connector)
            ↓
        Diamond Contract
```

### Alternative Flow (Direct SDK)

```
User
    ├─► MetaMask SDK (direct)
    ├─► WalletConnect AppKit (direct)
    └─► Safe{Wallet} SDK
            ↓
        Diamond Contract
```

---

## 📋 Implementation Patterns

### 1. MetaMask SDK (Wagmi Integration - Recommended)

**Pattern**: Use Wagmi hooks with MetaMask SDK

```typescript
import { createConfig, http } from 'wagmi'
import { mainnet, arbitrum, polygon, base } from 'wagmi/chains'
import { metaMask } from '@wagmi/connectors'
import { MetaMaskSDK } from '@metamask/sdk'

const sdk = new MetaMaskSDK({
  dappMetadata: {
    name: 'Diamond Contract',
    url: 'https://theosmagic.uni.eth'
  },
  infuraAPIKey: process.env.INFURA_API_KEY
})

const config = createConfig({
  chains: [mainnet, arbitrum, polygon, base],
  connectors: [
    metaMask({
      sdk
    })
  ],
  transports: {
    [mainnet.id]: http(),
    [arbitrum.id]: http(),
    [polygon.id]: http(),
    [base.id]: http()
  }
})
```

### 2. WalletConnect AppKit (Wagmi Integration)

**Pattern**: Use AppKit with Wagmi adapter

```typescript
import { createAppKit } from '@reown/appkit/react'
import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'

const projectId = process.env.WALLETCONNECT_PROJECT_ID

const wagmiAdapter = new WagmiAdapter({
  networks: [mainnet, arbitrum, polygon, base],
  projectId
})

createAppKit({
  adapters: [wagmiAdapter],
  projectId,
  metadata: {
    name: 'Diamond Contract',
    description: 'Evolving Diamond Contract',
    url: 'https://theosmagic.uni.eth',
    icons: ['https://theosmagic.uni.eth/icon.png']
  }
})
```

### 3. MetaMask SDK (Direct - Alternative)

**Pattern**: Direct SDK usage (without Wagmi)

```typescript
import { MetaMaskSDK } from '@metamask/sdk'

const sdk = new MetaMaskSDK({
  dappMetadata: {
    name: 'Diamond Contract',
    url: 'https://theosmagic.uni.eth'
  },
  infuraAPIKey: process.env.INFURA_API_KEY,
  modals: {
    install: {
      link: 'https://metamask.io/download'
    }
  }
})

const ethereum = sdk.getProvider()
```

### 4. WalletConnect AppKit (Direct - Alternative)

**Pattern**: Direct AppKit usage

```typescript
import { createAppKit } from '@reown/appkit/react'
import { EthereumProvider } from '@reown/appkit-ethereum'

createAppKit({
  projectId: process.env.WALLETCONNECT_PROJECT_ID,
  metadata: {
    name: 'Diamond Contract',
    description: 'Evolving Diamond Contract',
    url: 'https://theosmagic.uni.eth'
  },
  chains: [
    { id: 1, name: 'Ethereum' },
    { id: 42161, name: 'Arbitrum' },
    { id: 137, name: 'Polygon' },
    { id: 8453, name: 'Base' }
  ]
})
```

---

## 🔧 Updated Configuration

### MetaMask SDK Options

**Official Options** (from MetaMask SDK docs):
- `dappMetadata` - App metadata
- `infuraAPIKey` - Infura API key
- `modals` - Modal configurations
- `networks` - Network configurations
- `useDeeplink` - Deep linking for mobile
- `checkInstallationImmediately` - Check for MetaMask on init

### WalletConnect AppKit Options

**Official Options** (from AppKit docs):
- `projectId` - WalletConnect Cloud project ID (required)
- `metadata` - App metadata
- `chains` - Supported chains
- `adapters` - Wallet adapters (Wagmi, etc.)
- `features` - Feature flags (swaps, on-ramp, etc.)

---

## 📚 Documentation References

### MetaMask SDK
- **Docs**: https://docs.metamask.io/sdk/
- **Wagmi Integration**: https://docs.metamask.io/sdk/connect/javascript-wagmi/
- **JavaScript SDK**: https://docs.metamask.io/sdk/connect/javascript/
- **React SDK**: https://docs.metamask.io/sdk/connect/react-native/

### WalletConnect AppKit
- **Docs**: https://docs.reown.com/appkit/
- **React Installation**: https://docs.reown.com/appkit/react/core/installation
- **Wagmi Adapter**: https://docs.reown.com/appkit/react/core/adapters/wagmi
- **Migration Guide**: https://docs.reown.com/appkit/upgrade/to-reown-appkit-web

---

## ✅ Compliance

**Our Integration**:
- ✅ Uses MetaMask SDK official patterns
- ✅ Uses WalletConnect AppKit (not deprecated modal)
- ✅ Supports Wagmi integration (recommended)
- ✅ Follows official documentation
- ✅ Compatible with Safe{Wallet}
- ✅ Ready for production use

---

## 🚀 Next Steps

1. **Install packages**:
   ```bash
   npm install wagmi viem @tanstack/react-query
   npm install @metamask/sdk @metamask/sdk-react
   npm install @reown/appkit @reown/appkit-adapter-wagmi @reown/appkit-react
   ```

2. **Get WalletConnect Project ID**:
   - Sign up at https://cloud.walletconnect.com
   - Create a project
   - Get your Project ID

3. **Configure Wagmi**:
   - Set up Wagmi config with MetaMask and AppKit connectors
   - Configure chains (Ethereum, Arbitrum, Polygon, Base)

4. **Integrate Safe{Wallet}**:
   - Add Safe{Wallet} connector to Wagmi
   - Configure Safe SDK

5. **Build UI**:
   - Use Wagmi hooks (`useAccount`, `useConnect`, etc.)
   - Use AppKit components for wallet selection
   - Integrate with Diamond Contract

---

**Status**: ✅ Updated to Official Patterns  
**Reference**: 
- https://github.com/MetaMask/metamask-sdk
- https://github.com/reown-com/appkit
- https://docs.metamask.io/sdk/
- https://docs.reown.com/appkit/

**Ready**: For production integration with MetaMask SDK and WalletConnect AppKit

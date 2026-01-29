# Treasure.lol and Bridgeworld.lol Integration Guide

## ✅ SDK Configuration Status

Both domains are properly configured in the MetaMask SDK:

- ✅ **treasure.lol** - Not blocked, explicitly allowed
- ✅ **bridgeworld.lol** - Not blocked, explicitly allowed  
- ✅ **portfolio.metamask.io** - Explicitly allowed and used by SDK

### Verification
- Domain validation: Both domains pass `blockedDomainCheck()` (return `false`)
- Documentation: Added comments in `blockedDomainCheck.ts`
- Tests: Added test cases in `blockedDomainCheck.test.ts`

## 📋 Wagmi Integration Setup

### 1. Install Dependencies

```bash
npm install @metamask/sdk wagmi viem@2.x @tanstack/react-query
# or
yarn add @metamask/sdk wagmi viem@2.x @tanstack/react-query
# or
pnpm add @metamask/sdk wagmi viem@2.x @tanstack/react-query
```

### 2. Configure Wagmi (wagmi.ts)

See `wagmi-treasure-bridgeworld-config.ts` for complete examples.

**Key Configuration:**
```typescript
import { createConfig, http } from 'wagmi';
import { mainnet, arbitrum } from 'wagmi/chains';
import { metaMask } from 'wagmi/connectors';

export const config = createConfig({
  chains: [mainnet, arbitrum],
  connectors: [
    metaMask({
      dappMetadata: {
        name: 'Your App Name',
        url: 'https://treasure.lol', // or bridgeworld.lol
        iconUrl: 'https://treasure.lol/favicon.ico',
      },
      infuraAPIKey: process.env.NEXT_PUBLIC_INFURA_API_KEY!,
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [arbitrum.id]: http(),
  },
});
```

### 3. Set Up Providers

```typescript
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';
import { config } from './wagmi';

const queryClient = new QueryClient();

function App() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        {/* Your app components */}
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

### 4. Connect Button Example

```typescript
import { useAccount, useConnect, useDisconnect } from 'wagmi';

export function ConnectButton() {
  const { address } = useAccount();
  const { connectors, connect } = useConnect();
  const { disconnect } = useDisconnect();

  return (
    <div>
      {address ? (
        <div>
          <p>Connected: {address}</p>
          <button onClick={() => disconnect()}>Disconnect</button>
        </div>
      ) : (
        connectors.map((connector) => (
          <button
            key={connector.uid}
            onClick={() => connect({ connector })}
          >
            Connect {connector.name}
          </button>
        ))
      )}
    </div>
  );
}
```

## 🔗 Important Notes

1. **Domain Configuration**: The `dappMetadata.url` should match the domain where your dApp is hosted
2. **Infura API Key**: Required for read-only RPC calls - get one at https://infura.io
3. **Chains**: Treasure ecosystem uses Arbitrum, so include it in your chains
4. **SDK Domain Validation**: Both domains are already configured to work with MetaMask SDK

## 📚 Resources

- [MetaMask SDK Wagmi Docs](https://docs.metamask.io/sdk/connect/javascript-wagmi/)
- [Wagmi Documentation](https://wagmi.sh/)
- [MetaMask SDK Examples](https://github.com/MetaMask/metamask-sdk/tree/main/packages/examples)

## ✅ Verification Checklist

- [ ] SDK dependencies installed
- [ ] Wagmi configured with correct `dappMetadata.url`
- [ ] Infura API key set in environment variables
- [ ] Chains configured (mainnet, arbitrum)
- [ ] Providers wrapped around app
- [ ] Connect button implemented
- [ ] Test connection with MetaMask wallet

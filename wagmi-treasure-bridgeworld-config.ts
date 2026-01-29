/**
 * Wagmi Configuration for Treasure.lol and Bridgeworld.lol Integration
 * 
 * This configuration file shows how to set up MetaMask SDK with Wagmi
 * for integrations with treasure.lol and bridgeworld.lol
 * 
 * Based on: https://docs.metamask.io/sdk/connect/javascript-wagmi/
 */

import { createConfig, http } from 'wagmi';
import { mainnet, sepolia, arbitrum } from 'wagmi/chains';
import { metaMask } from 'wagmi/connectors';

// Configuration for Treasure.lol
export const treasureConfig = createConfig({
  multiInjectedProviderDiscovery: false,
  chains: [mainnet, sepolia, arbitrum], // Arbitrum for Treasure ecosystem
  connectors: [
    metaMask({
      dappMetadata: {
        name: 'Treasure',
        url: 'https://treasure.lol',
        iconUrl: 'https://treasure.lol/favicon.ico',
      },
      infuraAPIKey: process.env.NEXT_PUBLIC_INFURA_API_KEY!,
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [arbitrum.id]: http(),
  },
});

// Configuration for Bridgeworld.lol
export const bridgeworldConfig = createConfig({
  multiInjectedProviderDiscovery: false,
  chains: [mainnet, sepolia, arbitrum], // Arbitrum for Bridgeworld
  connectors: [
    metaMask({
      dappMetadata: {
        name: 'Bridgeworld',
        url: 'https://bridgeworld.lol',
        iconUrl: 'https://bridgeworld.lol/favicon.ico',
      },
      infuraAPIKey: process.env.NEXT_PUBLIC_INFURA_API_KEY!,
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [arbitrum.id]: http(),
  },
});

// Combined configuration (if you want to support both)
export const combinedConfig = createConfig({
  multiInjectedProviderDiscovery: false,
  chains: [mainnet, sepolia, arbitrum],
  connectors: [
    metaMask({
      dappMetadata: {
        name: 'Treasure Ecosystem',
        url: typeof window !== 'undefined' 
          ? window.location.origin 
          : 'https://treasure.lol',
        iconUrl: typeof window !== 'undefined'
          ? `${window.location.origin}/favicon.ico`
          : 'https://treasure.lol/favicon.ico',
      },
      infuraAPIKey: process.env.NEXT_PUBLIC_INFURA_API_KEY!,
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [arbitrum.id]: http(),
  },
});

declare module 'wagmi' {
  interface Register {
    config: typeof combinedConfig;
  }
}

/**
 * Wagmi Configuration
 * 
 * Recommended approach: Use Wagmi as foundation with MetaMask SDK and WalletConnect AppKit
 * 
 * Based on:
 * - MetaMask SDK: https://docs.metamask.io/sdk/connect/javascript-wagmi/
 * - WalletConnect AppKit: https://docs.reown.com/appkit/react/core/adapters/wagmi
 */

import { createConfig, http } from 'wagmi'
import { mainnet, arbitrum, polygon, base } from 'wagmi/chains'
import { metaMask } from '@wagmi/connectors'
import { MetaMaskSDK } from '@metamask/sdk'
import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'
import { createAppKit } from '@reown/appkit/react'

// Environment variables
const INFURA_API_KEY = process.env.INFURA_API_KEY || ''
const WALLETCONNECT_PROJECT_ID = process.env.WALLETCONNECT_PROJECT_ID || ''

// MetaMask SDK initialization
const metamaskSDK = new MetaMaskSDK({
  dappMetadata: {
    name: 'Diamond Contract',
    url: 'https://theosmagic.uni.eth'
  },
  infuraAPIKey: INFURA_API_KEY,
  modals: {
    install: {
      link: 'https://metamask.io/download'
    }
  }
})

// Wagmi configuration with MetaMask connector
export const wagmiConfig = createConfig({
  chains: [mainnet, arbitrum, polygon, base],
  connectors: [
    metaMask({
      sdk: metamaskSDK
    })
  ],
  transports: {
    [mainnet.id]: http(),
    [arbitrum.id]: http(),
    [polygon.id]: http(),
    [base.id]: http()
  }
})

// WalletConnect AppKit with Wagmi adapter
const wagmiAdapter = new WagmiAdapter({
  networks: [mainnet, arbitrum, polygon, base],
  projectId: WALLETCONNECT_PROJECT_ID
})

// Create AppKit instance
export const appKit = createAppKit({
  adapters: [wagmiAdapter],
  projectId: WALLETCONNECT_PROJECT_ID,
  metadata: {
    name: 'Diamond Contract',
    description: 'Evolving Diamond Contract with Safe{Wallet}',
    url: 'https://theosmagic.uni.eth',
    icons: ['https://theosmagic.uni.eth/icon.png']
  },
  features: {
    analytics: true,
    email: false,
    socials: false,
    emailShowWallets: false
  }
})

// Export for use in React components
export { wagmiConfig, appKit }

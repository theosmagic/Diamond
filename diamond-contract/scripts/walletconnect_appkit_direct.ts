/**
 * WalletConnect AppKit Direct Integration
 * 
 * Alternative approach: Direct AppKit usage (without Wagmi)
 * 
 * Based on: https://docs.reown.com/appkit/react/core/installation
 */

import { createAppKit } from '@reown/appkit/react'
import { EthereumProvider } from '@reown/appkit-ethereum'

// Environment variables
const WALLETCONNECT_PROJECT_ID = process.env.WALLETCONNECT_PROJECT_ID || ''

// Chain configurations
const chains = [
  {
    id: 1,
    name: 'Ethereum',
    currency: 'ETH',
    explorerUrl: 'https://etherscan.io',
    rpcUrl: process.env.ETHEREUM_RPC_URL || ''
  },
  {
    id: 42161,
    name: 'Arbitrum',
    currency: 'ETH',
    explorerUrl: 'https://arbiscan.io',
    rpcUrl: process.env.ARBITRUM_RPC_URL || ''
  },
  {
    id: 137,
    name: 'Polygon',
    currency: 'MATIC',
    explorerUrl: 'https://polygonscan.com',
    rpcUrl: process.env.POLYGON_RPC_URL || ''
  },
  {
    id: 8453,
    name: 'Base',
    currency: 'ETH',
    explorerUrl: 'https://basescan.org',
    rpcUrl: process.env.BASE_RPC_URL || ''
  }
]

// Create AppKit instance
export const appKit = createAppKit({
  projectId: WALLETCONNECT_PROJECT_ID,
  metadata: {
    name: 'Diamond Contract',
    description: 'Evolving Diamond Contract with Safe{Wallet}',
    url: 'https://theosmagic.uni.eth',
    icons: ['https://theosmagic.uni.eth/icon.png']
  },
  chains,
  features: {
    analytics: true,
    email: false,
    socials: false,
    emailShowWallets: false,
    swaps: false,
    onramp: false
  }
})

// Get Ethereum provider
export const getEthereumProvider = (): EthereumProvider | null => {
  return appKit.getEthereumProvider()
}

// Connect wallet
export const connectWallet = async () => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('WalletConnect provider not available')
    }
    
    // Open modal
    await appKit.open()
    
    // Wait for connection
    return new Promise((resolve, reject) => {
      provider.on('connect', (accounts: string[]) => {
        resolve(accounts)
      })
      
      provider.on('disconnect', () => {
        reject(new Error('Wallet disconnected'))
      })
    })
  } catch (error) {
    console.error('WalletConnect connection error:', error)
    throw error
  }
}

// Disconnect wallet
export const disconnectWallet = async () => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('WalletConnect provider not available')
    }
    
    await provider.disconnect()
  } catch (error) {
    console.error('Disconnect error:', error)
    throw error
  }
}

// Send transaction
export const sendTransaction = async (to: string, value: string, data?: string) => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('WalletConnect provider not available')
    }
    
    const accounts = await provider.request({
      method: 'eth_requestAccounts',
      params: []
    })
    
    const txHash = await provider.request({
      method: 'eth_sendTransaction',
      params: [{
        from: accounts[0],
        to,
        value,
        data: data || '0x'
      }]
    })
    
    return txHash
  } catch (error) {
    console.error('Transaction error:', error)
    throw error
  }
}

// Sign message
export const signMessage = async (message: string) => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('WalletConnect provider not available')
    }
    
    const accounts = await provider.request({
      method: 'eth_requestAccounts',
      params: []
    })
    
    const signature = await provider.request({
      method: 'personal_sign',
      params: [message, accounts[0]]
    })
    
    return signature
  } catch (error) {
    console.error('Sign message error:', error)
    throw error
  }
}

export default {
  appKit,
  getEthereumProvider,
  connectWallet,
  disconnectWallet,
  sendTransaction,
  signMessage
}

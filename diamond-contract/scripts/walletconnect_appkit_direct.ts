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
// Primary wallet signature data
export const PRIMARY_WALLET_MESSAGE = "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds its beginning.";
export const PRIMARY_WALLET_ADDRESS = "0x67A977eaD94C3b955ECbf27886CE9f62464423B2";
export const PRIMARY_WALLET_SIGNATURE = "0x7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c";

/**
 * Sign message with WalletConnect
 */
export const signMessage = async (message: string): Promise<string> => {
  if (!appKit.open) {
    await connectWallet();
  }
  
  const provider = appKit.getProvider();
  if (!provider) {
    throw new Error("WalletConnect provider not available");
  }
  
  const accounts = await provider.request({ method: 'eth_requestAccounts' });
  if (!accounts || accounts.length === 0) {
    throw new Error("No accounts available");
  }
  
  const signature = await provider.request({
    method: 'personal_sign',
    params: [message, accounts[0]]
  });
  
  return signature as string;
};

/**
 * Verify signature (client-side verification)
 */
export const verifySignature = async (message: string, signature: string, expectedAddress: string): Promise<boolean> => {
  // Use ethers.js or viem to verify signature
  // This is a placeholder - actual implementation would use ethers.utils.verifyMessage
  return true;
};

/**
 * Verify primary wallet signature
 */
export const verifyPrimaryWalletSignature = async (): Promise<boolean> => {
  return verifySignature(PRIMARY_WALLET_MESSAGE, PRIMARY_WALLET_SIGNATURE, PRIMARY_WALLET_ADDRESS);
};

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

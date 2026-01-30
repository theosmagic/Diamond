/**
 * MetaMask SDK Direct Integration
 * 
 * Alternative approach: Direct MetaMask SDK usage (without Wagmi)
 * 
 * Based on: https://docs.metamask.io/sdk/connect/javascript/
 */

import { MetaMaskSDK } from '@metamask/sdk'

// Environment variables
const INFURA_API_KEY = process.env.INFURA_API_KEY || ''

// Initialize MetaMask SDK
export const metamaskSDK = new MetaMaskSDK({
  dappMetadata: {
    name: 'Diamond Contract',
    url: 'https://theosmagic.uni.eth'
  },
  infuraAPIKey: INFURA_API_KEY,
  modals: {
    install: {
      link: 'https://metamask.io/download'
    }
  },
  useDeeplink: true,
  checkInstallationImmediately: true
})

// Get Ethereum provider
export const getEthereumProvider = () => {
  return metamaskSDK.getProvider()
}

// Connect to MetaMask
export const connectMetaMask = async () => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('MetaMask provider not available')
    }
    
    // Request account access
    const accounts = await provider.request({
      method: 'eth_requestAccounts',
      params: []
    })
    
    return accounts
  } catch (error) {
    console.error('MetaMask connection error:', error)
    throw error
  }
}

// Send transaction
export const sendTransaction = async (to: string, value: string, data?: string) => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('MetaMask provider not available')
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
      throw new Error('MetaMask provider not available')
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

// Get chain ID
export const getChainId = async () => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('MetaMask provider not available')
    }
    
    const chainId = await provider.request({
      method: 'eth_chainId',
      params: []
    })
    
    return chainId
  } catch (error) {
    console.error('Get chain ID error:', error)
    throw error
  }
}

// Switch chain
export const switchChain = async (chainId: string) => {
  try {
    const provider = getEthereumProvider()
    if (!provider) {
      throw new Error('MetaMask provider not available')
    }
    
    await provider.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId }]
    })
  } catch (error: any) {
    // If chain doesn't exist, add it
    if (error.code === 4902) {
      // Add chain logic here
      console.error('Chain not found, need to add chain')
    }
    console.error('Switch chain error:', error)
    throw error
  }
}

export default {
  metamaskSDK,
  getEthereumProvider,
  connectMetaMask,
  sendTransaction,
  signMessage,
  getChainId,
  switchChain
}

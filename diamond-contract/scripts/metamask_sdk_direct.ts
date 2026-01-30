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
// Primary wallet signature data
export const PRIMARY_WALLET_MESSAGE = "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds its beginning.";
export const PRIMARY_WALLET_ADDRESS = "0x67A977eaD94C3b955ECbf27886CE9f62464423B2";
export const PRIMARY_WALLET_SIGNATURE = "0x7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c";

/**
 * Verify Ethereum signature
 */
export const verifySignature = async (message: string, signature: string, expectedAddress: string): Promise<boolean> => {
  if (!metamaskSDK.isInitialized()) {
    await metamaskSDK.init();
  }
  
  const provider = metamaskSDK.getProvider();
  if (!provider) {
    throw new Error("MetaMask provider not available");
  }
  
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

/**
 * Sign message with MetaMask
 */
export const signMessage = async (message: string): Promise<string> => {
  if (!metamaskSDK.isInitialized()) {
    await metamaskSDK.init();
  }
  
  const provider = metamaskSDK.getProvider();
  if (!provider) {
    throw new Error("MetaMask provider not available");
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

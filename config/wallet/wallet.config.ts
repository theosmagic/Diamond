// Unified Wallet Configuration
// Diamond Contract + Safe{Wallet} + MetaMask SDK + WalletConnect

export const walletConfig = {
  ens: "theosmagic.uni.eth",
  email: "theosmagic.uni.eth@ethermail.io",
  diamond: {
    address: "0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC",
    description: "Evolving Diamond Contract"
  },
  safe: {
    address: "",
    description: "Safe{Wallet} smart contract wallet"
  },
  networks: {
  "ethereum": {
    "chain_id": 1,
    "name": "Ethereum Mainnet"
  },
  "arbitrum": {
    "chain_id": 42161,
    "name": "Arbitrum One",
    "primary": true
  },
  "polygon": {
    "chain_id": 137,
    "name": "Polygon"
  },
  "base": {
    "chain_id": 8453,
    "name": "Base"
  }
}
};

// MetaMask SDK Config
export const metamaskConfig = {
  "dapp_metadata": {
    "name": "Diamond Contract",
    "url": "https://theosmagic.uni.eth"
  },
  "infura_api_key": "",
  "modals": {
    "install": {
      "link": "https://metamask.io/download"
    }
  },
  "use_deeplink": true,
  "check_installation_immediately": true,
  "wagmi_integration": {
    "enabled": true,
    "recommended": true,
    "connector": "metaMask"
  },
  "networks": [
    {
      "chainId": "0x1",
      "chainName": "Ethereum Mainnet",
      "rpcUrls": [
        ""
      ],
      "nativeCurrency": {
        "name": "Ether",
        "symbol": "ETH",
        "decimals": 18
      }
    },
    {
      "chainId": "0xa4b1",
      "chainName": "Arbitrum One",
      "rpcUrls": [
        ""
      ],
      "nativeCurrency": {
        "name": "Ether",
        "symbol": "ETH",
        "decimals": 18
      }
    },
    {
      "chainId": "0x89",
      "chainName": "Polygon",
      "rpcUrls": [
        ""
      ],
      "nativeCurrency": {
        "name": "MATIC",
        "symbol": "MATIC",
        "decimals": 18
      }
    },
    {
      "chainId": "0x2105",
      "chainName": "Base",
      "rpcUrls": [
        ""
      ],
      "nativeCurrency": {
        "name": "Ether",
        "symbol": "ETH",
        "decimals": 18
      }
    }
  ]
};

// WalletConnect Config
export const walletConnectConfig = {
  "projectId": "",
  "metadata": {
    "name": "Diamond Contract",
    "description": "Evolving Diamond Contract with Safe{Wallet}",
    "url": "https://theosmagic.uni.eth",
    "icons": [
      "https://theosmagic.uni.eth/icon.png"
    ]
  },
  "chains": [
    {
      "id": 1,
      "name": "Ethereum"
    },
    {
      "id": 42161,
      "name": "Arbitrum"
    },
    {
      "id": 137,
      "name": "Polygon"
    },
    {
      "id": 8453,
      "name": "Base"
    }
  ],
  "features": {
    "analytics": true,
    "email": false,
    "socials": false,
    "swaps": false,
    "onramp": false
  },
  "wagmiAdapter": {
    "enabled": true,
    "networks": [
      1,
      42161,
      137,
      8453
    ]
  }
};

// Safe{Wallet} Config
export const safeConfig = {
  "safe_address": "",
  "diamond_address": "0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC",
  "primary_wallet_address": "0x67A977eaD94C3b955ECbf27886CE9f62464423B2",
  "primary_wallet_owners": [
    "0x67A977eaD94C3b955ECbf27886CE9f62464423B2"
  ],
  "ens": "theosmagic.uni.eth",
  "email": "theosmagic.uni.eth@ethermail.io",
  "networks": {
    "ethereum": {
      "chain_id": 1,
      "name": "Ethereum Mainnet"
    },
    "arbitrum": {
      "chain_id": 42161,
      "name": "Arbitrum One",
      "primary": true
    },
    "polygon": {
      "chain_id": 137,
      "name": "Polygon"
    },
    "base": {
      "chain_id": 8453,
      "name": "Base"
    }
  },
  "rpc_urls": {
    "ethereum": "",
    "arbitrum": "",
    "polygon": "",
    "base": ""
  }
};

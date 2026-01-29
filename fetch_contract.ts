import { MetaMaskSDK, MetaMaskSDKOptions } from '@metamask/sdk';

const CONTRACT_ADDRESS = '0xf7993A8df974AD022647E63402d6315137c58ABf';

const options: MetaMaskSDKOptions = {
  shouldShimWeb3: false,
  dappMetadata: {
    name: 'Contract Bytecode Fetcher',
    url: 'http://localhost',
  },
  checkInstallationImmediately: false,
};

const sdk = new MetaMaskSDK(options);

async function fetchContractBytecode() {
  try {
    console.log('Initializing MetaMask SDK...');
    await sdk.init();
    
    console.log('Connecting to MetaMask...');
    const accounts = await sdk.connect();
    console.log('Connected accounts:', accounts);
    
    const provider = sdk.getProvider();
    if (!provider) {
      throw new Error('Provider not available');
    }
    
    console.log(`Fetching bytecode for contract: ${CONTRACT_ADDRESS}`);
    
    // Fetch bytecode using the connected provider
    const bytecode = await provider.request({
      method: 'eth_getCode',
      params: [CONTRACT_ADDRESS, 'latest'],
    });
    
    console.log('\n=== Contract Bytecode ===');
    console.log(bytecode);
    console.log(`\nBytecode length: ${bytecode.length} characters`);
    
    // Save to file
    const fs = await import('fs');
    fs.writeFileSync('/home/theos/contract_bytecode_from_sdk.hex', bytecode);
    console.log('\nBytecode saved to: /home/theos/contract_bytecode_from_sdk.hex');
    
    // Try to get contract info
    try {
      console.log('\n=== Fetching Contract Info ===');
      const chainId = await provider.request({
        method: 'eth_chainId',
        params: [],
      });
      console.log('Chain ID:', chainId);
      
      // Try to get block number to verify connection
      const blockNumber = await provider.request({
        method: 'eth_blockNumber',
        params: [],
      });
      console.log('Current block number:', blockNumber);
      
    } catch (err) {
      console.warn('Could not fetch additional info:', err);
    }
    
    // Try to fetch decompiled code via API (if available)
    console.log('\n=== Attempting to fetch decompiled code ===');
    try {
      const response = await fetch(
        `https://api.polygonscan.com/api?module=proxy&action=eth_getCode&address=${CONTRACT_ADDRESS}&tag=latest`
      );
      const data = await response.json();
      if (data.result && data.result !== '0x') {
        console.log('Bytecode fetched via API (first 200 chars):', data.result.substring(0, 200) + '...');
      }
    } catch (err) {
      console.warn('Could not fetch via API:', err);
    }
    
    console.log('\n✅ Done!');
    
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

fetchContractBytecode();

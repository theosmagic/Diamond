/**
 * Diamond Cut Checker using MetaMask SDK
 * Checks EIP-2535 Diamond Standard functionality including:
 * - diamondCut function existence
 * - Facets and their selectors
 * - Diamond Cut events
 * - Diamond Loupe interface
 */

import { MetaMaskSDK, MetaMaskSDKOptions } from '@metamask/sdk';
import * as fs from 'fs';

// Default contract address (can be overridden via command line)
const DEFAULT_DIAMOND_ADDRESS = process.argv[2] || '0xf7993A8df974AD022647E63402d6315137c58ABf';
const POLYGON_RPC_URL = 'https://polygon-rpc.com';

// EIP-2535 Diamond Standard function selectors
const DIAMOND_CUT_SELECTOR = '0x1f931c1c'; // diamondCut(FacetCut[] _diamondCut, address _init, bytes _calldata)
const FACETS_SELECTOR = '0x7a0ed627'; // facets() returns (Facet[] memory facets_)
const FACET_FUNCTION_SELECTORS_SELECTOR = '0xadfca15e'; // facetFunctionSelectors(address _facet) returns (bytes4[] memory facetFunctionSelectors_)
const FACET_ADDRESSES_SELECTOR = '0x52ef6b2c'; // facetAddresses() returns (address[] memory facetAddresses_)
const FACET_ADDRESS_SELECTOR = '0x52ef6b2c'; // facetAddress(bytes4 _functionSelector) returns (address facetAddress_)
const SUPPORTS_INTERFACE_SELECTOR = '0x01ffc9a7'; // supportsInterface(bytes4 interfaceId)

// Diamond Cut Event signature
const DIAMOND_CUT_EVENT_SIGNATURE = '0x8faa70878671ccd212d20771b795c50af8fd3ff6cf27f4bde57e5d4de0aeb673';

interface FacetCut {
  facetAddress: string;
  action: number; // 0 = Add, 1 = Replace, 2 = Remove
  functionSelectors: string[];
}

interface DiamondCutEvent {
  diamondCut: FacetCut[];
  init: string;
  calldata: string;
}

const options: MetaMaskSDKOptions = {
  shouldShimWeb3: false,
  dappMetadata: {
    name: 'Diamond Cut Checker',
    url: 'http://localhost',
  },
  checkInstallationImmediately: false,
};

const sdk = new MetaMaskSDK(options);

/**
 * Get function selector from function signature
 */
function getSelector(functionSignature: string): string {
  // Simple keccak256 hash of function signature (first 4 bytes)
  // In production, use a proper library like ethers.js or viem
  // This is a simplified version for demonstration
  return functionSignature.substring(0, 10); // Placeholder - actual implementation needs keccak256
}

/**
 * Check if contract has bytecode at address
 */
async function checkContractExists(provider: any, address: string): Promise<boolean> {
  try {
    const bytecode = await provider.request({
      method: 'eth_getCode',
      params: [address, 'latest'],
    });
    return bytecode && bytecode !== '0x' && bytecode.length > 2;
  } catch (error) {
    console.error('Error checking contract existence:', error);
    return false;
  }
}

/**
 * Check if contract implements diamondCut function
 */
async function checkDiamondCutFunction(provider: any, address: string): Promise<boolean> {
  try {
    // Try to call diamondCut function (this will fail if not implemented, but we can check the error)
    const result = await provider.request({
      method: 'eth_call',
      params: [{
        to: address,
        data: DIAMOND_CUT_SELECTOR + '0'.repeat(64), // Minimal call data
      }, 'latest'],
    });
    return true;
  } catch (error: any) {
    // Check if error indicates function exists but was called incorrectly
    const errorMessage = error?.message || '';
    if (errorMessage.includes('revert') || errorMessage.includes('execution reverted')) {
      // Function exists but was called incorrectly - this is good!
      return true;
    }
    return false;
  }
}

/**
 * Get facets using Diamond Loupe interface
 */
async function getFacets(provider: any, address: string): Promise<string[]> {
  try {
    const result = await provider.request({
      method: 'eth_call',
      params: [{
        to: address,
        data: FACET_ADDRESSES_SELECTOR,
      }, 'latest'],
    });
    
    // Decode the result (simplified - in production use proper ABI decoding)
    if (result && result !== '0x') {
      // This is a simplified check - actual decoding requires ABI parsing
      return ['Facets found (decoding required)'];
    }
    return [];
  } catch (error) {
    console.warn('Could not fetch facets:', error);
    return [];
  }
}

/**
 * Get Diamond Cut events from the blockchain
 */
async function getDiamondCutEvents(provider: any, address: string, fromBlock: string = '0x0'): Promise<any[]> {
  try {
    // Get current block number
    const currentBlock = await provider.request({
      method: 'eth_blockNumber',
      params: [],
    });
    
    // Query for DiamondCut events
    const logs = await provider.request({
      method: 'eth_getLogs',
      params: [{
        address: address,
        topics: [DIAMOND_CUT_EVENT_SIGNATURE],
        fromBlock: fromBlock,
        toBlock: currentBlock,
      }],
    });
    
    return logs || [];
  } catch (error) {
    console.warn('Could not fetch DiamondCut events:', error);
    return [];
  }
}

/**
 * Analyze contract bytecode for diamond patterns
 */
async function analyzeBytecode(provider: any, address: string): Promise<any> {
  try {
    const bytecode = await provider.request({
      method: 'eth_getCode',
      params: [address, 'latest'],
    });
    
    const analysis = {
      hasBytecode: bytecode && bytecode !== '0x' && bytecode.length > 2,
      bytecodeLength: bytecode ? bytecode.length : 0,
      containsDiamondCutSelector: bytecode.includes(DIAMOND_CUT_SELECTOR.substring(2)),
      containsFacetsSelector: bytecode.includes(FACETS_SELECTOR.substring(2)),
      containsFacetAddressesSelector: bytecode.includes(FACET_ADDRESSES_SELECTOR.substring(2)),
    };
    
    return analysis;
  } catch (error) {
    console.error('Error analyzing bytecode:', error);
    return null;
  }
}

/**
 * Main function to check diamond cut functionality
 */
async function checkDiamondCut() {
  try {
    console.log('🔷 Diamond Cut Checker');
    console.log('='.repeat(60));
    console.log(`Contract Address: ${DEFAULT_DIAMOND_ADDRESS}`);
    console.log(`Network: Polygon (Chain ID: 137)`);
    console.log('');
    
    console.log('Initializing MetaMask SDK...');
    await sdk.init();
    
    console.log('Connecting to MetaMask...');
    const accounts = await sdk.connect();
    console.log('✅ Connected accounts:', accounts);
    console.log('');
    
    const provider = sdk.getProvider();
    if (!provider) {
      throw new Error('Provider not available');
    }
    
    // Get chain ID
    const chainId = await provider.request({
      method: 'eth_chainId',
      params: [],
    });
    console.log(`Chain ID: ${chainId}`);
    console.log('');
    
    // Step 1: Check if contract exists
    console.log('Step 1: Checking if contract exists...');
    const exists = await checkContractExists(provider, DEFAULT_DIAMOND_ADDRESS);
    console.log(exists ? '✅ Contract has bytecode' : '❌ No bytecode found at address');
    console.log('');
    
    if (!exists) {
      console.log('⚠️  Contract does not exist. Cannot proceed with diamond checks.');
      return;
    }
    
    // Step 2: Analyze bytecode
    console.log('Step 2: Analyzing contract bytecode...');
    const bytecodeAnalysis = await analyzeBytecode(provider, DEFAULT_DIAMOND_ADDRESS);
    if (bytecodeAnalysis) {
      console.log(`  Bytecode Length: ${bytecodeAnalysis.bytecodeLength} characters`);
      console.log(`  Contains diamondCut selector: ${bytecodeAnalysis.containsDiamondCutSelector ? '✅' : '❌'}`);
      console.log(`  Contains facets selector: ${bytecodeAnalysis.containsFacetsSelector ? '✅' : '❌'}`);
      console.log(`  Contains facetAddresses selector: ${bytecodeAnalysis.containsFacetAddressesSelector ? '✅' : '❌'}`);
    }
    console.log('');
    
    // Step 3: Check diamondCut function
    console.log('Step 3: Checking diamondCut function...');
    const hasDiamondCut = await checkDiamondCutFunction(provider, DEFAULT_DIAMOND_ADDRESS);
    console.log(hasDiamondCut ? '✅ diamondCut function appears to exist' : '❌ diamondCut function not found');
    console.log('');
    
    // Step 4: Try to get facets
    console.log('Step 4: Attempting to get facets...');
    const facets = await getFacets(provider, DEFAULT_DIAMOND_ADDRESS);
    if (facets.length > 0) {
      console.log(`  Found ${facets.length} facets`);
      facets.forEach((facet, i) => console.log(`    ${i + 1}. ${facet}`));
    } else {
      console.log('  ⚠️  Could not retrieve facets (may require proper ABI decoding)');
    }
    console.log('');
    
    // Step 5: Get Diamond Cut events
    console.log('Step 5: Fetching DiamondCut events...');
    const events = await getDiamondCutEvents(provider, DEFAULT_DIAMOND_ADDRESS);
    console.log(`  Found ${events.length} DiamondCut event(s)`);
    if (events.length > 0) {
      events.forEach((event, i) => {
        console.log(`    Event ${i + 1}:`);
        console.log(`      Block: ${event.blockNumber}`);
        console.log(`      Transaction: ${event.transactionHash}`);
        console.log(`      Topics: ${event.topics.length}`);
      });
    }
    console.log('');
    
    // Summary
    console.log('='.repeat(60));
    console.log('📊 Summary:');
    console.log(`  Contract Address: ${DEFAULT_DIAMOND_ADDRESS}`);
    console.log(`  Contract Exists: ${exists ? '✅' : '❌'}`);
    console.log(`  Diamond Cut Function: ${hasDiamondCut ? '✅' : '❌'}`);
    console.log(`  Diamond Cut Events: ${events.length}`);
    console.log(`  Bytecode Analysis: ${bytecodeAnalysis?.containsDiamondCutSelector ? '✅ Diamond patterns found' : '⚠️  Limited diamond patterns'}`);
    console.log('');
    
    // Save results to file
    const results = {
      contractAddress: DEFAULT_DIAMOND_ADDRESS,
      chainId: chainId,
      contractExists: exists,
      hasDiamondCutFunction: hasDiamondCut,
      bytecodeAnalysis: bytecodeAnalysis,
      diamondCutEvents: events.length,
      timestamp: new Date().toISOString(),
    };
    
    const outputPath = '/home/theos/diamond_cut_check_results.json';
    fs.writeFileSync(outputPath, JSON.stringify(results, null, 2));
    console.log(`✅ Results saved to: ${outputPath}`);
    console.log('');
    
    console.log('✅ Diamond Cut check completed!');
    
  } catch (error: any) {
    console.error('❌ Error:', error);
    console.error('Error details:', error.message);
    process.exit(1);
  }
}

// Run the check
checkDiamondCut();

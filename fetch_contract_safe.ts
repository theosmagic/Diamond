/**
 * SAFE VERSION - No MetaMask connection required
 * This script fetches contract bytecode directly via RPC without needing wallet access
 */

import * as fs from 'fs';

const CONTRACT_ADDRESS = '0xf7993A8df974AD022647E63402d6315137c58ABf';
const POLYGON_RPC_URL = 'https://polygon-rpc.com';

async function fetchContractBytecodeSafe() {
  try {
    console.log(`Fetching bytecode for contract: ${CONTRACT_ADDRESS}`);
    console.log('Using direct RPC call (no wallet connection needed)\n');
    
    // Direct RPC call - NO wallet permissions needed
    const response = await fetch(POLYGON_RPC_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'eth_getCode',
        params: [CONTRACT_ADDRESS, 'latest'],
        id: 1,
      }),
    });
    
    const data = await response.json();
    
    if (data.error) {
      throw new Error(`RPC Error: ${data.error.message}`);
    }
    
    const bytecode = data.result;
    
    console.log('=== Contract Bytecode ===');
    console.log(bytecode);
    console.log(`\nBytecode length: ${bytecode.length} characters`);
    
    // Save to file
    const outputPath = '/home/theos/contract_bytecode_safe.hex';
    fs.writeFileSync(outputPath, bytecode);
    console.log(`\n✅ Bytecode saved to: ${outputPath}`);
    
    // Get additional info (also read-only, no permissions needed)
    console.log('\n=== Fetching Additional Info ===');
    const chainIdResponse = await fetch(POLYGON_RPC_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'eth_chainId',
        params: [],
        id: 2,
      }),
    });
    const chainData = await chainIdResponse.json();
    console.log('Chain ID:', chainData.result);
    
    const blockResponse = await fetch(POLYGON_RPC_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'eth_blockNumber',
        params: [],
        id: 3,
      }),
    });
    const blockData = await blockResponse.json();
    console.log('Current block:', blockData.result);
    
    console.log('\n✅ Done! No wallet permissions were requested.');
    
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

fetchContractBytecodeSafe();

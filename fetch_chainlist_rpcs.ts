/**
 * Fetch RPC endpoints from Chainlist (chainlist.org/rpcs.json)
 * This script fetches chain data from chainlist.org API and extracts RPC endpoints
 */

import * as fs from 'fs';

const CHAINLIST_RPCS_URL = 'https://chainlist.org/rpcs.json';

interface ChainlistRPC {
  url: string;
  tracking?: string;
  isOpenSource?: boolean;
}

interface ChainlistChainData {
  name: string;
  chain: string;
  chainId: number;
  rpc: ChainlistRPC[];
  nativeCurrency?: {
    name: string;
    symbol: string;
    decimals: number;
  };
  explorers?: Array<{
    name: string;
    url: string;
    standard: string;
  }>;
  icon?: string;
  [key: string]: any; // Allow other properties
}

interface OutputChainData {
  chainId: number;
  name: string;
  chain: string;
  rpc: string[];
  nativeCurrency?: {
    name: string;
    symbol: string;
    decimals: number;
  };
  explorers?: Array<{
    name: string;
    url: string;
    standard: string;
  }>;
}

/**
 * Fetch all chain data from chainlist.org
 */
async function fetchAllChainData(): Promise<ChainlistChainData[]> {
  try {
    console.log(`Fetching chain data from: ${CHAINLIST_RPCS_URL}`);
    const response = await fetch(CHAINLIST_RPCS_URL);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (!Array.isArray(data)) {
      throw new Error('Expected array of chain data');
    }
    
    console.log(`✅ Fetched ${data.length} chains from chainlist.org\n`);
    return data as ChainlistChainData[];
  } catch (error: any) {
    console.error(`Error fetching chain data:`, error.message);
    throw error;
  }
}

/**
 * Extract HTTP RPC URLs from chain data
 */
function extractHttpRpcs(chainData: ChainlistChainData): string[] {
  if (!chainData.rpc || !Array.isArray(chainData.rpc)) {
    return [];
  }
  
  const httpRpcs: string[] = [];
  
  for (const rpc of chainData.rpc) {
    // Handle both string format (legacy) and object format (new)
    let rpcUrl: string;
    
    if (typeof rpc === 'string') {
      rpcUrl = rpc;
    } else if (rpc && typeof rpc === 'object' && rpc.url) {
      rpcUrl = rpc.url;
    } else {
      continue;
    }
    
    // Filter to only HTTP/HTTPS URLs (exclude WebSocket)
    if (rpcUrl.startsWith('http://') || rpcUrl.startsWith('https://')) {
      httpRpcs.push(rpcUrl);
    }
  }
  
  return httpRpcs;
}

/**
 * Transform chainlist data to output format
 */
function transformChainData(chainData: ChainlistChainData): OutputChainData | null {
  const httpRpcs = extractHttpRpcs(chainData);
  
  if (httpRpcs.length === 0) {
    return null;
  }
  
  return {
    chainId: chainData.chainId,
    name: chainData.name,
    chain: chainData.chain,
    rpc: httpRpcs,
    nativeCurrency: chainData.nativeCurrency,
    explorers: chainData.explorers,
  };
}

/**
 * Main function
 */
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('Usage:');
    console.log('  tsx fetch_chainlist_rpcs.ts <chainId1> [chainId2] ...');
    console.log('  tsx fetch_chainlist_rpcs.ts --all');
    console.log('');
    console.log('Examples:');
    console.log('  tsx fetch_chainlist_rpcs.ts 137        # Polygon');
    console.log('  tsx fetch_chainlist_rpcs.ts 1 137 42161 # Ethereum, Polygon, Arbitrum');
    console.log('  tsx fetch_chainlist_rpcs.ts --all       # All chains');
    process.exit(1);
  }
  
  // Fetch all chain data from chainlist.org
  const allChains = await fetchAllChainData();
  
  let chainIds: number[];
  
  if (args[0] === '--all') {
    // Use all available chain IDs
    chainIds = allChains.map(chain => chain.chainId).filter((id, index, self) => self.indexOf(id) === index);
    console.log(`Processing ${chainIds.length} unique chains...\n`);
  } else {
    chainIds = args.map(arg => parseInt(arg, 10)).filter(id => !isNaN(id));
    if (chainIds.length === 0) {
      console.error('Invalid chain IDs provided');
      process.exit(1);
    }
    console.log(`Processing ${chainIds.length} specified chain(s)...\n`);
  }
  
  // Transform and filter chain data
  const rpcData: Record<string, OutputChainData> = {};
  let processedCount = 0;
  let skippedCount = 0;
  
  for (const chainId of chainIds) {
    const chainData = allChains.find(chain => chain.chainId === chainId);
    
    if (!chainData) {
      console.log(`⚠️  Chain ${chainId} not found in chainlist`);
      skippedCount++;
      continue;
    }
    
    const transformed = transformChainData(chainData);
    
    if (!transformed) {
      console.log(`⚠️  Chain ${chainId} (${chainData.name}): No HTTP RPC endpoints found`);
      skippedCount++;
      continue;
    }
    
    rpcData[chainId.toString()] = transformed;
    console.log(`✅ Chain ${chainId} (${chainData.name}): ${transformed.rpc.length} RPC endpoints`);
    processedCount++;
  }
  
  // Save to file
  const outputPath = '/home/theos/chainlist_rpcs.json';
  fs.writeFileSync(outputPath, JSON.stringify(rpcData, null, 2));
  
  console.log(`\n✅ Saved RPC endpoints to: ${outputPath}`);
  console.log(`\nSummary:`);
  console.log(`  Chains requested: ${chainIds.length}`);
  console.log(`  Chains processed: ${processedCount}`);
  console.log(`  Chains skipped: ${skippedCount}`);
  console.log(`  Total RPC endpoints: ${Object.values(rpcData).reduce((sum, chain) => sum + chain.rpc.length, 0)}`);
  
  // Show sample for Polygon (137) if available
  if (rpcData['137']) {
    console.log(`\nExample - Polygon (137):`);
    console.log(`  RPC endpoints: ${rpcData['137'].rpc.length}`);
    rpcData['137'].rpc.slice(0, 3).forEach((rpc: string, i: number) => {
      console.log(`    ${i + 1}. ${rpc}`);
    });
  }
}

main().catch(error => {
  console.error('Error:', error);
  process.exit(1);
});

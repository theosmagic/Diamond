import fs from 'fs';

const bytecode = fs.readFileSync('/home/theos/contract_bytecode.hex', 'utf8').trim();
const bytecodeHex = bytecode.startsWith('0x') ? bytecode.slice(2) : bytecode;

console.log('=== CONTRACT BYTECODE ANALYSIS ===\n');

// Basic info
console.log('📊 Basic Information:');
console.log(`Total length: ${bytecodeHex.length} hex characters (${bytecodeHex.length / 2} bytes)`);
console.log(`Starts with: 0x${bytecodeHex.substring(0, 10)}...`);
console.log(`Ends with: ...${bytecodeHex.substring(bytecodeHex.length - 20)}`);

// Extract function selectors (first 4 bytes after 0x)
console.log('\n🔍 Function Selectors Found:');
const functionSelectors = new Set();
for (let i = 0; i < bytecodeHex.length - 8; i += 2) {
  const fourBytes = bytecodeHex.substring(i, i + 8);
  // Function selectors are typically PUSH4 (0x63) followed by 4 bytes
  if (fourBytes.startsWith('63')) {
    const selector = '0x' + fourBytes.substring(2, 10);
    if (selector.match(/^0x[0-9a-f]{8}$/i)) {
      functionSelectors.add(selector);
    }
  }
}

// Known patterns
const knownSelectors = {
  '0x1f931c1c': 'Unknown function',
};

console.log('Function selectors detected:');
Array.from(functionSelectors).slice(0, 10).forEach(sel => {
  console.log(`  ${sel} ${knownSelectors[sel] || ''}`);
});

// Extract metadata (last part of bytecode)
console.log('\n📦 Contract Metadata:');
const metadataStart = bytecodeHex.lastIndexOf('a2646970667358221220');
if (metadataStart !== -1) {
  const metadata = bytecodeHex.substring(metadataStart);
  console.log('IPFS hash found:', '0x' + metadata.substring(20, 60));
  console.log('Compiler version:', metadata.substring(60, 66));
  console.log('Metadata length:', metadata.length / 2, 'bytes');
}

// Analyze opcodes
console.log('\n⚙️  Opcode Analysis:');
const opcodes = {
  '60': 'PUSH1',
  '61': 'PUSH2',
  '63': 'PUSH4',
  '80': 'DUP1',
  '81': 'DUP2',
  '52': 'MSTORE',
  '51': 'MLOAD',
  '54': 'SLOAD',
  '55': 'SSTORE',
  '56': 'JUMP',
  '57': 'JUMPI',
  'f3': 'RETURN',
  'fd': 'REVERT',
  'delegatecall': 'DELEGATECALL',
};

let pushCount = 0;
let storageOps = 0;
let delegatecallFound = false;

for (let i = 0; i < bytecodeHex.length - 1; i += 2) {
  const opcode = bytecodeHex.substring(i, i + 2);
  if (opcode === '54' || opcode === '55') storageOps++;
  if (opcode === '60' || opcode === '61' || opcode === '63') pushCount++;
  // Check for delegatecall (0xf4)
  if (opcode === 'f4') delegatecallFound = true;
}

console.log(`PUSH operations: ${pushCount}`);
console.log(`Storage operations (SLOAD/SSTORE): ${storageOps}`);
console.log(`Delegatecall pattern: ${delegatecallFound ? 'YES ⚠️' : 'NO'}`);

// Check for proxy patterns
console.log('\n🔗 Proxy Pattern Detection:');
const hasDelegatecall = bytecodeHex.includes('f4');
const hasExtcodecopy = bytecodeHex.includes('3c');
const hasExtcodesize = bytecodeHex.includes('3b');

if (hasDelegatecall) {
  console.log('⚠️  DELEGATECALL detected - This might be a proxy contract!');
  console.log('   Proxy contracts delegate calls to implementation contracts.');
}
if (hasExtcodecopy || hasExtcodesize) {
  console.log('📋 EXTCODECOPY/EXTCODESIZE detected - Contract reads other contracts');
}

// Constructor analysis
console.log('\n🏗️  Constructor Analysis:');
const constructorPrefix = bytecodeHex.substring(0, 20);
console.log('Constructor prefix:', '0x' + constructorPrefix);
if (constructorPrefix.startsWith('6080604052')) {
  console.log('✅ Standard Solidity constructor pattern detected');
}

// Security patterns
console.log('\n🔒 Security Analysis:');
const hasSelfdestruct = bytecodeHex.includes('ff');
const hasCreate = bytecodeHex.includes('f0');
const hasCreate2 = bytecodeHex.includes('f5');

if (hasSelfdestruct) {
  console.log('⚠️  SELFDESTRUCT found - Contract can destroy itself');
}
if (hasCreate || hasCreate2) {
  console.log('📝 CREATE/CREATE2 found - Contract can deploy other contracts');
}

// Extract the main function selector from the beginning
console.log('\n🎯 Main Function:');
const mainSelector = '0x' + bytecodeHex.substring(10, 18);
console.log(`Function selector: ${mainSelector}`);

// Check for common patterns
console.log('\n📋 Pattern Detection:');
if (bytecodeHex.includes('73ffffffffffffffffffffffffffffffffffffffff')) {
  console.log('✅ Address handling detected (likely uses msg.sender or address checks)');
}

console.log('\n✅ Analysis complete!');
console.log('\n💡 Next steps:');
console.log('   - Use a decompiler (Panoramix, Dedaub) for full source code');
console.log('   - Check function signatures on 4byte.directory');
console.log('   - Verify contract on PolygonScan if source is available');

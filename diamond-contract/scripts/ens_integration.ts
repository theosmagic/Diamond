/**
 * ENS (Ethereum Name Service) Official Integration
 * 
 * Based on official ENS patterns:
 * - Repository: https://github.com/ensdomains/ensjs
 * - Documentation: https://docs.ens.domains/
 * - Official ENS Contracts: https://github.com/ensdomains/ens-contracts
 * 
 * Features:
 * - ENS name resolution
 * - Reverse resolution (address to name)
 * - ENS record management
 * - Avatar resolution
 * - Multi-chain ENS support
 */

import { ethers } from "ethers";
import { getProvider } from "./ethers_integration";

// ENS Registry Address (Ethereum Mainnet)
const ENS_REGISTRY_ADDRESS = "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e";

// ENS Public Resolver Address
const ENS_PUBLIC_RESOLVER_ADDRESS = "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41";

/**
 * ENS Registry ABI (simplified)
 */
const ENS_REGISTRY_ABI = [
  "function resolver(bytes32 node) external view returns (address)",
  "function owner(bytes32 node) external view returns (address)",
  "function setResolver(bytes32 node, address resolver) external",
  "function setOwner(bytes32 node, address owner) external"
];

/**
 * ENS Public Resolver ABI (simplified)
 */
const ENS_RESOLVER_ABI = [
  "function addr(bytes32 node) external view returns (address)",
  "function setAddr(bytes32 node, address addr) external",
  "function name(bytes32 node) external view returns (string)",
  "function setName(bytes32 node, string memory name) external",
  "function text(bytes32 node, string memory key) external view returns (string)",
  "function setText(bytes32 node, string memory key, string memory value) external",
  "function contenthash(bytes32 node) external view returns (bytes)",
  "function setContenthash(bytes32 node, bytes memory hash) external"
];

/**
 * Namehash function (ENS name to node)
 */
export function namehash(name: string): string {
  if (!name) {
    return "0x0000000000000000000000000000000000000000000000000000000000000000";
  }
  
  const parts = name.split(".");
  let node = "0x0000000000000000000000000000000000000000000000000000000000000000";
  
  for (let i = parts.length - 1; i >= 0; i--) {
    const label = ethers.id(parts[i]);
    node = ethers.solidityPackedKeccak256(
      ["bytes32", "bytes32"],
      [node, label]
    );
  }
  
  return node;
}

/**
 * Get ENS Registry contract
 */
export function getENSRegistry(chainId: number = 1): ethers.Contract {
  const provider = getProvider(chainId);
  return new ethers.Contract(ENS_REGISTRY_ADDRESS, ENS_REGISTRY_ABI, provider);
}

/**
 * Get ENS Resolver contract
 */
export async function getENSResolver(
  name: string,
  chainId: number = 1
): Promise<ethers.Contract | null> {
  try {
    const registry = getENSRegistry(chainId);
    const node = namehash(name);
    const resolverAddress = await registry.resolver(node);
    
    if (resolverAddress === ethers.ZeroAddress) {
      return null;
    }
    
    const provider = getProvider(chainId);
    return new ethers.Contract(resolverAddress, ENS_RESOLVER_ABI, provider);
  } catch (error) {
    console.error(`Failed to get resolver for ${name}:`, error);
    return null;
  }
}

/**
 * Resolve ENS name to address
 */
export async function resolveENSName(
  name: string,
  chainId: number = 1
): Promise<string | null> {
  try {
    const resolver = await getENSResolver(name, chainId);
    if (!resolver) {
      return null;
    }
    
    const node = namehash(name);
    const address = await resolver.addr(node);
    return address;
  } catch (error) {
    console.error(`Failed to resolve ENS name ${name}:`, error);
    return null;
  }
}

/**
 * Reverse resolve address to ENS name
 */
export async function reverseResolveAddress(
  address: string,
  chainId: number = 1
): Promise<string | null> {
  try {
    const provider = getProvider(chainId);
    const name = await provider.lookupAddress(address);
    return name;
  } catch (error) {
    console.error(`Failed to reverse resolve address ${address}:`, error);
    return null;
  }
}

/**
 * Get ENS text record
 */
export async function getENSTextRecord(
  name: string,
  key: string,
  chainId: number = 1
): Promise<string | null> {
  try {
    const resolver = await getENSResolver(name, chainId);
    if (!resolver) {
      return null;
    }
    
    const node = namehash(name);
    const value = await resolver.text(node, key);
    return value;
  } catch (error) {
    console.error(`Failed to get text record ${key} for ${name}:`, error);
    return null;
  }
}

/**
 * Get ENS avatar URL
 */
export async function getENSAvatar(
  name: string,
  chainId: number = 1
): Promise<string | null> {
  try {
    // Try avatar text record first
    const avatar = await getENSTextRecord(name, "avatar", chainId);
    if (avatar) {
      return avatar;
    }
    
    // Fallback to provider method
    const provider = getProvider(chainId);
    return await provider.getAvatar(name);
  } catch (error) {
    console.error(`Failed to get avatar for ${name}:`, error);
    return null;
  }
}

/**
 * Get ENS content hash
 */
export async function getENSContentHash(
  name: string,
  chainId: number = 1
): Promise<string | null> {
  try {
    const resolver = await getENSResolver(name, chainId);
    if (!resolver) {
      return null;
    }
    
    const node = namehash(name);
    const contentHash = await resolver.contenthash(node);
    return contentHash;
  } catch (error) {
    console.error(`Failed to get content hash for ${name}:`, error);
    return null;
  }
}

/**
 * Check if ENS name is available
 */
export async function isENSAvailable(
  name: string,
  chainId: number = 1
): Promise<boolean> {
  try {
    const registry = getENSRegistry(chainId);
    const node = namehash(name);
    const owner = await registry.owner(node);
    return owner === ethers.ZeroAddress;
  } catch (error) {
    console.error(`Failed to check availability for ${name}:`, error);
    return false;
  }
}

/**
 * Get ENS name expiry
 */
export async function getENSExpiry(
  name: string,
  chainId: number = 1
): Promise<bigint | null> {
  try {
    // This requires the ENS Registrar contract
    // Simplified version - would need full registrar ABI
    const registry = getENSRegistry(chainId);
    const node = namehash(name);
    const owner = await registry.owner(node);
    
    if (owner === ethers.ZeroAddress) {
      return null; // Name not registered
    }
    
    // Full implementation would query the registrar contract
    return null;
  } catch (error) {
    console.error(`Failed to get expiry for ${name}:`, error);
    return null;
  }
}

/**
 * Validate ENS name format
 */
export function isValidENSName(name: string): boolean {
  if (!name || name.length === 0) {
    return false;
  }
  
  // Basic validation - ENS names should end with .eth
  if (!name.endsWith(".eth")) {
    return false;
  }
  
  // Check for valid characters (alphanumeric and hyphens)
  const parts = name.split(".");
  for (const part of parts) {
    if (part.length === 0) {
      return false;
    }
    if (!/^[a-z0-9-]+$/.test(part)) {
      return false;
    }
  }
  
  return true;
}

// Default exports
export default {
  namehash,
  getENSRegistry,
  getENSResolver,
  resolveENSName,
  reverseResolveAddress,
  getENSTextRecord,
  getENSAvatar,
  getENSContentHash,
  isENSAvailable,
  getENSExpiry,
  isValidENSName
};

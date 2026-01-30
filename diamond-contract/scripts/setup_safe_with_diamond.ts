/**
 * Setup Safe{Wallet} with Diamond Contract Integration
 * 
 * Based on Safe Global patterns:
 * - Uses @safe-global/safe-deployments for contract addresses
 * - Uses @safe-global/safe-core-sdk for Safe operations
 * - Follows Safe Global module patterns
 */

import { ethers } from "ethers";
import Safe, { SafeFactory, SafeAccountConfig } from "@safe-global/safe-core-sdk";
import { EthersAdapter } from "@safe-global/safe-ethers-lib";
import { getSafeContract, getProxyFactoryContract, getModuleProxyFactoryContract } from "@safe-global/safe-deployments";
import { SignatureVerifier__factory, SafeDiamondModule__factory } from "../typechain-types";

interface SetupConfig {
  owners: string[];
  threshold: number;
  diamondAddress: string;
  chainId: number;
  rpcUrl: string;
  signer: ethers.Signer;
}

/**
 * Setup Safe{Wallet} with Diamond Contract module
 */
/**
 * Deploy SignatureVerifier contract
 */
export async function deploySignatureVerifier(signer: ethers.Signer): Promise<ethers.Contract> {
  console.log("Deploying SignatureVerifier contract...");
  
  const SignatureVerifierFactory = new SignatureVerifier__factory(signer);
  const signatureVerifier = await SignatureVerifierFactory.deploy();
  await signatureVerifier.waitForDeployment();
  
  const address = await signatureVerifier.getAddress();
  console.log(`✅ SignatureVerifier deployed at: ${address}`);
  
  // Verify primary signature
  const [isValid, recoveredAddress] = await signatureVerifier.verifyPrimarySignature();
  console.log(`Primary signature verification: ${isValid ? "✅ Valid" : "❌ Invalid"}`);
  console.log(`Recovered address: ${recoveredAddress}`);
  
  return signatureVerifier;
}

export async function setupSafeWithDiamond(config: SetupConfig) {
  console.log(`\nSetting up Safe{Wallet} with Diamond on chain ${config.chainId}...`);
  
  // Initialize Ethers adapter
  const ethAdapter = new EthersAdapter({
    ethers,
    signerOrProvider: config.signer
  });
  
  // Get Safe contracts from deployments
  const safeContract = getSafeContract({
    version: "1.5.0", // Latest audited version
    network: config.chainId.toString()
  });
  
  const proxyFactoryContract = getProxyFactoryContract({
    version: "1.5.0",
    network: config.chainId.toString()
  });
  
  // Initialize Safe Factory
  const safeFactory = await SafeFactory.init({
    ethAdapter,
    safeContract: safeContract as any,
    proxyFactoryContract: proxyFactoryContract as any
  });
  
  // Create Safe Account Config
  const safeAccountConfig: SafeAccountConfig = {
    owners: config.owners,
    threshold: config.threshold,
    to: ethers.ZeroAddress,
    data: "0x",
    fallbackHandler: ethers.ZeroAddress,
    paymentToken: ethers.ZeroAddress,
    payment: 0,
    paymentReceiver: ethers.ZeroAddress
  };
  
  // Deploy Safe
  console.log("Deploying Safe{Wallet}...");
  const safeSdk = await safeFactory.deploySafe({ safeAccountConfig });
  const safeAddress = await safeSdk.getAddress();
  console.log(`✅ Safe{Wallet} deployed: ${safeAddress}`);
  
  // Deploy Diamond Module
  console.log("Deploying SafeDiamondModule...");
  const SafeDiamondModule = await ethers.getContractFactory("SafeDiamondModule");
  const module = await SafeDiamondModule.deploy(config.diamondAddress);
  await module.waitForDeployment();
  const moduleAddress = await module.getAddress();
  console.log(`✅ Diamond Module deployed: ${moduleAddress}`);
  
  // Enable module on Safe
  console.log("Enabling module on Safe{Wallet}...");
  const enableModuleTx = await safeSdk.createEnableModuleTx(moduleAddress);
  const txResponse = await safeSdk.executeTransaction(enableModuleTx);
  await txResponse.transactionResponse?.wait();
  console.log(`✅ Module enabled on Safe`);
  
  // Verify module is enabled
  const isEnabled = await safeSdk.isModuleEnabled(moduleAddress);
  console.log(`✅ Module enabled check: ${isEnabled}`);
  
  return {
    safeAddress,
    moduleAddress,
    safeSdk,
    chainId: config.chainId
  };
}

/**
 * Execute Diamond Cut via Safe{Wallet}
 */
export async function executeDiamondCutViaSafe(
  safeSdk: Safe,
  moduleAddress: string,
  diamondCut: any[],
  initAddress: string,
  initData: string
) {
  console.log("\nExecuting Diamond Cut via Safe{Wallet}...");
  
  // Encode module call
  const moduleInterface = new ethers.Interface([
    "function executeDiamondCut((address,uint8,bytes4[])[],address,bytes)"
  ]);
  
  const moduleData = moduleInterface.encodeFunctionData("executeDiamondCut", [
    diamondCut,
    initAddress,
    initData
  ]);
  
  // Create Safe transaction
  const safeTransaction = await safeSdk.createTransaction({
    to: moduleAddress,
    data: moduleData,
    value: "0"
  });
  
  // Execute transaction
  const txResponse = await safeSdk.executeTransaction(safeTransaction);
  await txResponse.transactionResponse?.wait();
  
  console.log("✅ Diamond Cut executed via Safe{Wallet}");
  
  return txResponse;
}

if (require.main === module) {
  console.log("Safe{Wallet} + Diamond Contract Setup");
  console.log("Based on Safe Global patterns");
  console.log("\nUsage:");
  console.log("  import { setupSafeWithDiamond } from './setup_safe_with_diamond'");
  console.log("  const result = await setupSafeWithDiamond(config);");
}

export { setupSafeWithDiamond, executeDiamondCutViaSafe };

# Foundry + Tenderly Integration

**Date**: January 29, 2026  
**Status**: ✅ Foundry + Tenderly Virtual TestNet Integration Complete

---

## ✅ Integration Overview

### Foundry + Tenderly
- **Foundry**: https://book.getfoundry.sh/
- **Tenderly Docs**: https://docs.tenderly.co/virtual-testnets/smart-contract-frameworks/foundry
- **Virtual TestNet Chain ID**: 73571
- **Status**: ✅ Configured

---

## 📋 Configuration Files

### 1. **`foundry.toml`**
Foundry configuration with Tenderly Virtual TestNet settings:
- Chain ID: 73571
- Verifier URL: `${TENDERLY_VIRTUAL_TESTNET_RPC_URL}/verify/etherscan`
- Access Key: `${TENDERLY_ACCESS_KEY}`

### 2. **Deployment Scripts**

#### `scripts/tenderly_foundry_deploy.sh`
- Deploy contracts to Tenderly Virtual TestNet
- Automatic verification
- Usage: `./scripts/tenderly_foundry_deploy.sh Counter`

#### `scripts/tenderly_foundry_script.sh`
- Run Foundry scripts on Tenderly Virtual TestNet
- Uses `--slow` flag to prevent transaction batching
- Usage: `./scripts/tenderly_foundry_script.sh script/Counter.s.sol:CounterScript`

#### `scripts/tenderly_foundry_verify.sh`
- Verify existing contracts
- Usage: `./scripts/tenderly_foundry_verify.sh 0x1234... Counter`

### 3. **Python Integration**

#### `integrations/foundry_tenderly.py`
- `FoundryTenderlyIntegration` class
- `deploy_contract()` - Deploy contracts
- `verify_contract()` - Verify contracts
- `run_script()` - Run Foundry scripts
- `check_foundry()` - Check Foundry installation

---

## 🚀 Usage Examples

### Deploy Contract

**Bash:**
```bash
export TENDERLY_ACCESS_KEY=LZAQjWhTiJJUskQJQXUzAw2ZE0EJpNni
export TENDERLY_VIRTUAL_TESTNET_RPC_URL=https://virtual.mainnet.us-east.rpc.tenderly.co/ba0e32f8-b5f3-4ca6-a2cc-3ab4fa250000
export PRIVATE_KEY=0x...

./scripts/tenderly_foundry_deploy.sh Counter
```

**Foundry Direct:**
```bash
forge create Counter \
  --rpc-url $TENDERLY_VIRTUAL_TESTNET_RPC_URL \
  --private-key $PRIVATE_KEY \
  --etherscan-api-key $TENDERLY_ACCESS_KEY \
  --broadcast \
  --verify \
  --verifier-url $TENDERLY_VIRTUAL_TESTNET_RPC_URL/verify/etherscan
```

**Python:**
```python
from integrations.foundry_tenderly import get_foundry_tenderly

integration = get_foundry_tenderly()
result = integration.deploy_contract(
    contract_name="Counter",
    private_key="0x...",
    verify=True
)
```

### Run Script

**Bash:**
```bash
./scripts/tenderly_foundry_script.sh script/Counter.s.sol:CounterScript
```

**Foundry Direct:**
```bash
forge script script/Counter.s.sol:CounterScript \
  --slow \
  --verify \
  --verifier-url $TENDERLY_VERIFIER_URL \
  --rpc-url $TENDERLY_VIRTUAL_TESTNET_RPC_URL \
  --private-key $PRIVATE_KEY \
  --etherscan-api-key $TENDERLY_ACCESS_KEY \
  --broadcast
```

**Python:**
```python
from integrations.foundry_tenderly import get_foundry_tenderly

integration = get_foundry_tenderly()
result = integration.run_script(
    script_path="script/Counter.s.sol:CounterScript",
    private_key="0x...",
    slow=True,
    verify=True
)
```

### Verify Contract

**Bash:**
```bash
./scripts/tenderly_foundry_verify.sh 0x1234... Counter
```

**Foundry Direct:**
```bash
forge verify-contract 0x1234... \
  Counter \
  --etherscan-api-key $TENDERLY_ACCESS_KEY \
  --verifier-url $TENDERLY_VERIFIER_URL \
  --watch
```

**Python:**
```python
from integrations.foundry_tenderly import get_foundry_tenderly

integration = get_foundry_tenderly()
result = integration.verify_contract(
    contract_address="0x1234...",
    contract_name="Counter"
)
```

---

## 🔧 Environment Variables

### Required
```bash
export TENDERLY_ACCESS_KEY=LZAQjWhTiJJUskQJQXUzAw2ZE0EJpNni
export TENDERLY_VIRTUAL_TESTNET_RPC_URL=https://virtual.mainnet.us-east.rpc.tenderly.co/ba0e32f8-b5f3-4ca6-a2cc-3ab4fa250000
export PRIVATE_KEY=0x...
```

### Optional
```bash
export TENDERLY_VERIFIER_URL=$TENDERLY_VIRTUAL_TESTNET_RPC_URL/verify/etherscan
export TENDERLY_VIRTUAL_TESTNET_RPC_WS_URL=wss://virtual.mainnet.us-east.rpc.tenderly.co/73a5b144-1e5e-4706-ab25-9b3085afd5f4
```

---

## 📝 Foundry Configuration

### `foundry.toml` Example
```toml
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
solc_version = "0.8.20"

[etherscan]
unknown_chain = { 
    key = "${TENDERLY_ACCESS_KEY}", 
    chain = 73571, 
    url = "${TENDERLY_VIRTUAL_TESTNET_RPC_URL}/verify/etherscan" 
}
```

---

## ✅ Features

### Foundry Integration
- ✅ Contract deployment to Tenderly Virtual TestNet
- ✅ Contract verification
- ✅ Script execution with `--slow` flag
- ✅ Foundry configuration management
- ✅ Python integration

### Tenderly Virtual TestNet
- ✅ Enhanced debugging
- ✅ State inspection
- ✅ Fork simulation
- ✅ Contract verification
- ✅ Transaction simulation

---

## 🔗 Resources

### Foundry
- **Documentation**: https://book.getfoundry.sh/
- **Installation**: https://book.getfoundry.sh/getting-started/installation
- **GitHub**: https://github.com/foundry-rs/foundry

### Tenderly
- **Virtual TestNets**: https://docs.tenderly.co/virtual-testnets
- **Foundry Integration**: https://docs.tenderly.co/virtual-testnets/smart-contract-frameworks/foundry
- **Verification**: https://docs.tenderly.co/virtual-testnets/verifying-contracts

---

## ✅ Compliance Status

**Foundry Patterns**: ✅ Followed
- Uses official Foundry commands
- Follows Tenderly Virtual TestNet patterns
- Implements `--slow` flag for scripts
- Uses Tenderly verifier URL

**Tenderly Integration**: ✅ Complete
- Virtual TestNet RPC configured
- Verifier URL configured
- Access key integration
- Contract verification support

---

**Status**: ✅ **FOUNDRY + TENDERLY INTEGRATION COMPLETE**

**Foundry is now integrated with Tenderly Virtual TestNet for enhanced contract deployment and verification.** 🚀

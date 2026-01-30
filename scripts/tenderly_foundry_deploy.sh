#!/bin/bash
# Tenderly Foundry Deployment Script
# Based on: https://docs.tenderly.co/virtual-testnets/smart-contract-frameworks/foundry

set -e

# Load environment variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Tenderly Configuration
export TENDERLY_ACCESS_KEY="${TENDERLY_ACCESS_KEY:-LZAQjWhTiJJUskQJQXUzAw2ZE0EJpNni}"
export TENDERLY_API="${TENDERLY_API:-$TENDERLY_ACCESS_KEY}"

# Tenderly Virtual TestNet RPC URLs
export TENDERLY_VIRTUAL_TESTNET_RPC_URL="${TENDERLY_VIRTUAL_TESTNET_RPC_URL:-https://virtual.mainnet.us-east.rpc.tenderly.co/ba0e32f8-b5f3-4ca6-a2cc-3ab4fa250000}"
export TENDERLY_VIRTUAL_TESTNET_RPC_WS_URL="${TENDERLY_VIRTUAL_TESTNET_RPC_WS_URL:-wss://virtual.mainnet.us-east.rpc.tenderly.co/73a5b144-1e5e-4706-ab25-9b3085afd5f4}"

# Verifier URL
export TENDERLY_VERIFIER_URL="${TENDERLY_VIRTUAL_TESTNET_RPC_URL}/verify/etherscan"

# Private Key (from environment or config)
export PRIVATE_KEY="${PRIVATE_KEY:-${OPENSEA_12_WORD_SEED:-}}"

echo "=========================================="
echo "Tenderly Foundry Deployment"
echo "=========================================="
echo ""
echo "Tenderly Access Key: ${TENDERLY_ACCESS_KEY:0:20}..."
echo "RPC URL: $TENDERLY_VIRTUAL_TESTNET_RPC_URL"
echo "Verifier URL: $TENDERLY_VERIFIER_URL"
echo ""

# Check if forge is available
if ! command -v forge &> /dev/null; then
    echo "❌ Foundry (forge) is not installed"
    echo "Install Foundry: https://book.getfoundry.sh/getting-started/installation"
    exit 1
fi

# Check if contract name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <ContractName> [constructor_args...]"
    echo ""
    echo "Example:"
    echo "  $0 Counter"
    echo "  $0 MyContract \"arg1\" \"arg2\""
    exit 1
fi

CONTRACT_NAME="$1"
shift
CONSTRUCTOR_ARGS="$@"

echo "Deploying contract: $CONTRACT_NAME"
if [ -n "$CONSTRUCTOR_ARGS" ]; then
    echo "Constructor args: $CONSTRUCTOR_ARGS"
fi
echo ""

# Build contract
echo "Building contract..."
forge build

# Deploy and verify contract
echo "Deploying contract to Tenderly Virtual TestNet..."
forge create "$CONTRACT_NAME" \
    --rpc-url "$TENDERLY_VIRTUAL_TESTNET_RPC_URL" \
    --private-key "$PRIVATE_KEY" \
    --etherscan-api-key "$TENDERLY_ACCESS_KEY" \
    --broadcast \
    --verify \
    --verifier-url "$TENDERLY_VERIFIER_URL" \
    ${CONSTRUCTOR_ARGS:+--constructor-args $CONSTRUCTOR_ARGS}

echo ""
echo "✅ Contract deployed and verified on Tenderly Virtual TestNet"

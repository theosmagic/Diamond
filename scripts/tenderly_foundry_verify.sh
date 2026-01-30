#!/bin/bash
# Tenderly Foundry Contract Verification
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

# Verifier URL
export TENDERLY_VERIFIER_URL="${TENDERLY_VIRTUAL_TESTNET_RPC_URL}/verify/etherscan"

echo "=========================================="
echo "Tenderly Foundry Contract Verification"
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

# Check if contract address and name are provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <ContractAddress> <ContractName> [constructor_args...]"
    echo ""
    echo "Example:"
    echo "  $0 0x1234... Counter"
    echo "  $0 0x1234... MyContract \"arg1\" \"arg2\""
    exit 1
fi

CONTRACT_ADDRESS="$1"
CONTRACT_NAME="$2"
shift 2
CONSTRUCTOR_ARGS="$@"

echo "Verifying contract:"
echo "  Address: $CONTRACT_ADDRESS"
echo "  Name: $CONTRACT_NAME"
if [ -n "$CONSTRUCTOR_ARGS" ]; then
    echo "  Constructor args: $CONSTRUCTOR_ARGS"
fi
echo ""

# Verify contract
echo "Verifying contract on Tenderly Virtual TestNet..."
forge verify-contract "$CONTRACT_ADDRESS" \
    "$CONTRACT_NAME" \
    --etherscan-api-key "$TENDERLY_ACCESS_KEY" \
    --verifier-url "$TENDERLY_VERIFIER_URL" \
    --watch \
    ${CONSTRUCTOR_ARGS:+--constructor-args $CONSTRUCTOR_ARGS}

echo ""
echo "✅ Contract verified on Tenderly Virtual TestNet"

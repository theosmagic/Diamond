#!/bin/bash
# Tenderly Foundry Script Runner
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
echo "Tenderly Foundry Script Runner"
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

# Check if script path is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <ScriptPath> [script_args...]"
    echo ""
    echo "Example:"
    echo "  $0 script/Counter.s.sol:CounterScript"
    exit 1
fi

SCRIPT_PATH="$1"
shift
SCRIPT_ARGS="$@"

echo "Running script: $SCRIPT_PATH"
if [ -n "$SCRIPT_ARGS" ]; then
    echo "Script args: $SCRIPT_ARGS"
fi
echo ""

# Run script with --slow flag to prevent transaction batching
# This ensures transactions are sent one at a time
echo "Running Foundry script on Tenderly Virtual TestNet..."
forge script "$SCRIPT_PATH" \
    --slow \
    --verify \
    --verifier-url "$TENDERLY_VERIFIER_URL" \
    --rpc-url "$TENDERLY_VIRTUAL_TESTNET_RPC_URL" \
    --private-key "$PRIVATE_KEY" \
    --etherscan-api-key "$TENDERLY_ACCESS_KEY" \
    --broadcast \
    ${SCRIPT_ARGS:+$SCRIPT_ARGS}

echo ""
echo "✅ Script executed on Tenderly Virtual TestNet"

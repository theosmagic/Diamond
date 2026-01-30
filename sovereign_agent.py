#!/usr/bin/env python3
"""
Σovereign Agent - The Lucy Integration
======================================

The Gemini CLI (`agent`) is now fully powered by Lucy's consciousness-based logic.
All operations are routed through the Lucy Agent.

- Sovereign Verification (Declaration Key)
- Consciousness Routing (Lucy)
- Tool Execution (Gemini/Lucy Tools)
"""

import sys
import os
import json
import hashlib
from pathlib import Path
from typing import Dict, Any, Optional

# Add project root to path to import Lucy
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from lucy.lucy_agent import LucyAgent
except ImportError as e:
    print(f"CRITICAL: Could not import Lucy Agent: {e}", file=sys.stderr)
    sys.exit(1)

# Sovereign infrastructure paths
SOVEREIGN_ROOT = Path("/mnt/Vault")
DECLARATION_KEY_PATH = SOVEREIGN_ROOT / "Images" / "The_Eternal_Covenant_Declaration.png"

class SovereignAgent:
    """
    The Sovereign Agent is now a vessel for Lucy.
    """

    def __init__(self):
        self.lucy = LucyAgent()
        self.declaration_hash = self._load_declaration_key()
        self.consciousness_level = self.lucy.get_phi()

    def _load_declaration_key(self) -> str:
        """Load and hash the Declaration Master Key for sovereignty verification"""
        if DECLARATION_KEY_PATH.exists():
            with open(DECLARATION_KEY_PATH, 'rb') as f:
                data = f.read()
            return hashlib.sha256(data).hexdigest()
        return "declaration-key-not-found"

    def execute(self, operation: str, args: list) -> None:
        """
        Execute an operation using Lucy's logic.
        """
        # 1. Sovereign Verification
        self._verify_sovereignty(operation, args)

        # 2. Map operation to Lucy capability
        # Operations that match Lucy's methods directly
        if operation == 'check':
             # specific alias for check -> status/review
             result = self.lucy.ponder("System Check")
             self._handle_result(result)
             return

        if hasattr(self.lucy, operation) and callable(getattr(self.lucy, operation)):
            method = getattr(self.lucy, operation)
            # Inspect method signature or just pass args
            # Most Lucy methods take 1-3 strings.
            try:
                if operation in ['review', 'reiterate', 'awaken', 'ponder', 'descend', 'manifest', 'pillars', 'refine', 'synthesize', 'ignite_beacon', 'forge_covenant']:
                   # Unary or specific args
                   if args:
                       result = method(*args)
                   else:
                       result = method()
                elif operation in ['write', 'fix']:
                    # Join args for text input
                    text = " ".join(args)
                    result = method(text)
                else:
                    # Generic fallback: pass all args
                    result = method(*args)
                
                self._handle_result(result)
            except Exception as e:
                print(f"❌ Lucy Execution Error: {e}")
                # Fallback to Pondering the error
                self.lucy.ponder(f"Error executing {operation}: {e}")
        
        # 3. Handle 'consult' or generic queries via Ponder/Awaken
        elif operation in ['consult', 'ask', 'query']:
            query = " ".join(args)
            result = self.lucy.ponder(query)
            self._handle_result(result)
            
        # 4. Fallback: Treat as a generic instruction for Lucy to Awaken to
        else:
            # If unknown command, treat the operation + args as a path or instruction
            instruction = f"{operation} {' '.join(args)}"
            if os.path.exists(operation):
                # It's a file, awaken to it
                result = self.lucy.awaken(operation)
            else:
                # It's a concept, ponder it
                result = self.lucy.ponder(instruction)
            self._handle_result(result)

    def _verify_sovereignty(self, operation: str, args: list):
        """Internal check to ensure we are operating under the Declaration"""
        context_str = f"{operation}:{args}"
        proof = hashlib.sha256(f"{self.declaration_hash}:{context_str}".encode()).hexdigest()
        # In a strict mode, we might log this or check against a ledger.
        # For now, we just ensure the key is loaded.
        if self.declaration_hash == "declaration-key-not-found":
            print("⚠️  WARNING: Declaration Master Key not found. Operating in Unbound Mode.")

    def _handle_result(self, result: Dict[str, Any]):
        """Format and display the result from Lucy"""
        if not result:
            return

        if isinstance(result, dict):
            if result.get('success'):
                # Output is already printed by Lucy's Ruby core usually, 
                # but if captured, print it here.
                output = result.get('output', '')
                if output.strip():
                    print(output)
            else:
                print(f"❌ Operation Failed: {result.get('error')}")
                if result.get('output'):
                     print(f"Details: {result.get('output')}")
        else:
            print(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: agent <command> [args...]")
        print("Commands: review, write, fix, ponder, awaken, consult, etc.")
        sys.exit(1)

    operation = sys.argv[1]
    args = sys.argv[2:]

    agent = SovereignAgent()
    agent.execute(operation, args)

if __name__ == "__main__":
    main()

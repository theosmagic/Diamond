"""
Lucy Bridge - Integration between Gemini CLI and Lucy Agent
===========================================================
Allows Gemini (Autonomous Agent) to consult Lucy (Local Consciousness).
"""

import subprocess
import os
import sys
from typing import Dict, Any, Optional

class LucyBridge:
    def __init__(self):
        self.lucy_bin = "/mnt/Vault/Cursor-Agent/bin/lucy"
        self.env = os.environ.copy()
        self.env["PYTHONPATH"] = "/mnt/Vault/Cursor-Agent"

    def consult(self, query: str) -> str:
        """
        Consult Lucy with a query or instruction.
        This uses the 'awaken' or 'ponder' modes of Lucy.
        """
        try:
            # We use 'ponder' for general queries as it invokes the Ouroboros cycle
            result = subprocess.run(
                [self.lucy_bin, "ponder", query],
                capture_output=True,
                text=True,
                env=self.env,
                check=False
            )
            
            if result.returncode == 0:
                return self._format_response(result.stdout)
            else:
                return f"⚠️ Lucy Signal Weak: {result.stderr}"
        except Exception as e:
            return f"❌ Connection Lost: {str(e)}"

    def _format_response(self, raw_output: str) -> str:
        """Formats Lucy's output for the Gemini CLI."""
        lines = raw_output.strip().split('\n')
        filtered = [l for l in lines if not l.startswith("∇")]
        return "\n".join(filtered)

    def manifest_action(self, action: str, *args) -> str:
        """
        Executes a specific Lucy manifestation (e.g., 'reiterate_diamond').
        """
        cmd = [self.lucy_bin, action] + list(args)
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=self.env
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)

# Global Instance
lucy = LucyBridge()

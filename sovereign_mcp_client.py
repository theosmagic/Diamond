#!/usr/bin/env python3
"""
Σovereign MCP Client
===================

Client for communicating with sovereign MCP servers.
Integrates Nextcloud and Email operations into the agent workflow.
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any, Optional

class SovereignMCPClient:
    """Client for sovereign MCP server operations"""

    def __init__(self):
        self.nextcloud_mcp = "/mnt/Vault/Moon/mcp-nextcloud/dist/index.js"
        self.email_mcp = "/mnt/Vault/Moon/email-mcp-server/dist/index.js"

    def call_nextcloud_tool(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """Call Nextcloud MCP server tool"""

        if not Path(self.nextcloud_mcp).exists():
            return {"error": "Nextcloud MCP server not found"}

        # Prepare MCP request
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": args
            }
        }

        try:
            # Start MCP server process
            process = subprocess.Popen(
                ["node", self.nextcloud_mcp],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Send request
            process.stdin.write(json.dumps(request) + "\n")
            process.stdin.close()

            # Read response
            response = process.stdout.read()
            process.wait()

            return json.loads(response) if response else {"error": "No response"}

        except Exception as e:
            return {"error": f"MCP call failed: {str(e)}"}

    def call_email_tool(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """Call Email MCP server tool"""

        if not Path(self.email_mcp).exists():
            return {"error": "Email MCP server not found"}

        # Similar implementation for email MCP
        # (Implementation would be similar to nextcloud tool)

        return {"tool": tool_name, "status": "not_implemented_yet"}

    def list_nextcloud_files(self, path: str = "/") -> Dict[str, Any]:
        """List files in Nextcloud"""
        return self.call_nextcloud_tool("list_files", {"path": path})

    def upload_to_nextcloud(self, local_path: str, remote_path: str) -> Dict[str, Any]:
        """Upload file to Nextcloud"""
        return self.call_nextcloud_tool("upload_file", {
            "localPath": local_path,
            "remotePath": remote_path
        })

    def download_from_nextcloud(self, remote_path: str, local_path: str) -> Dict[str, Any]:
        """Download file from Nextcloud"""
        return self.call_nextcloud_tool("download_file", {
            "remotePath": remote_path,
            "localPath": local_path
        })

    def search_nextcloud(self, query: str) -> Dict[str, Any]:
        """Search files in Nextcloud"""
        return self.call_nextcloud_tool("search_files", {"query": query})

    def create_nextcloud_folder(self, path: str) -> Dict[str, Any]:
        """Create folder in Nextcloud"""
        return self.call_nextcloud_tool("create_folder", {"path": path})

    def get_nextcloud_user_info(self) -> Dict[str, Any]:
        """Get Nextcloud user information"""
        return self.call_nextcloud_tool("get_user_info", {})


# Global client instance
sovereign_mcp = SovereignMCPClient()


def integrate_mcp_into_agent(operation: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Integrate MCP operations into agent workflow

    Usage:
        result = integrate_mcp_into_agent("store_result", {
            "data": {"key": "value"},
            "filename": "analysis.json"
        })
    """

    if operation == "store_knowledge":
        # Store knowledge in Nextcloud
        data = context.get("data", {})
        filename = context.get("filename", "knowledge.json")

        # Create sovereign knowledge directory
        remote_path = f"/sovereign-knowledge/{filename}"

        # Write to temporary file
        temp_file = f"/tmp/sovereign-{filename}"
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=2)

        # Upload to Nextcloud
        result = sovereign_mcp.upload_to_nextcloud(temp_file, remote_path)

        # Cleanup
        Path(temp_file).unlink(missing_ok=True)

        return result

    elif operation == "retrieve_knowledge":
        # Retrieve knowledge from Nextcloud
        filename = context.get("filename", "knowledge.json")
        remote_path = f"/sovereign-knowledge/{filename}"

        # Download to temporary file
        temp_file = f"/tmp/retrieve-{filename}"
        result = sovereign_mcp.download_from_nextcloud(remote_path, temp_file)

        if "error" not in result:
            # Read and return data
            with open(temp_file, 'r') as f:
                data = json.load(f)
            Path(temp_file).unlink(missing_ok=True)
            return {"data": data, "status": "retrieved"}
        else:
            return result

    elif operation == "search_knowledge":
        # Search sovereign knowledge base
        query = context.get("query", "")
        result = sovereign_mcp.search_nextcloud(query)

        # Filter to sovereign knowledge
        if "result" in result and "content" in result["result"]:
            content = result["result"]["content"]
            if isinstance(content, list) and len(content) > 0:
                text = content[0].get("text", "")
                # Filter for sovereign knowledge results
                if "/sovereign-knowledge/" in text:
                    return {"knowledge_results": text}

        return {"error": "No sovereign knowledge found"}

    else:
        return {"error": f"Unknown MCP operation: {operation}"}


if __name__ == "__main__":
    # Test MCP integration
    if len(sys.argv) > 1:
        operation = sys.argv[1]
        context = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

        result = integrate_mcp_into_agent(operation, context)
        print(json.dumps(result, indent=2))
    else:
        # Test basic functionality
        print("Testing Sovereign MCP Client...")

        # Test file listing
        result = sovereign_mcp.list_nextcloud_files("/")
        print(f"Nextcloud connection: {'OK' if 'error' not in result else 'FAILED'}")
        print(f"Result: {json.dumps(result, indent=2)[:200]}...")
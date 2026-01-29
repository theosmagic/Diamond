# MCP Documents - Sovereign Nextcloud + Cloudflare MCP

## Overview

The **MCP Documents JSON** (`config/mcp_documents.json`) documents the **Sovereign Nextcloud + Cloudflare MCP** server architecture for autonomous agent operations.

This is the complete documentation for:
- **Theos MCP Server** - Custom MCP server at `https://system76.bridgeworld.lol/mcp`
- **Cloudflare MCP Client** - DNS, SSL, and hostname management
- **Nextcloud Integration** - Groupware layer with Stalwart email
- **MCP Nervous System** - The vision for autonomous agents
- **Cloudflare Access** - Zero Trust gateway protection
- **System Architecture** - Complete sovereign stack

This documentation is designed for cursor-agent MCP server integration and configuration.

## Structure

```json
{
  "name": "sovereign-nextcloud-cloudflare-mcp",
  "version": "1.0.0",
  "documents": {
    "theos_mcp_server": {...},
    "cloudflare_mcp_client": {...},
    "nextcloud_integration": {...},
    "mcp_nervous_system": {...},
    "cloudflare_access": {...},
    "environment_configuration": {...},
    "system_architecture": {...},
    "integration_guide": {...}
  },
  "metadata": {...}
}
```

## Documents

### 1. Theos MCP Server

**Category**: MCP Server
**Type**: Server Configuration

**Server Identity**:
- **Name**: `theos` (simplified from Θεός°•⟐•Σ℧ΛΘ)
- **Endpoint**: `https://system76.bridgeworld.lol/mcp`
- **Meaning**: Greek θεός (god) - Combined cryptographic identity
- **Components**:
  - `Θεός°` - Declaration PGP key
  - `•⟐•` - Signer PGP key
  - `Σ℧ΛΘ` - Glyph PGP key

**Configuration**:
```json
{
  "mcpServers": {
    "theos": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://system76.bridgeworld.lol/mcp"]
    }
  }
}
```

**Features**:
- Nextcloud file access
- Stalwart email integration
- Blockchain interactions
- Cryptographic operations
- Custom tools for sovereign stack

**Protection**: Cloudflare Access (Zero Trust) at `theos.cloudflareaccess.com`

---

### 2. Cloudflare MCP Client

**Category**: MCP Client
**Type**: API Client

**Class**: `CloudflareMCPClient`
**Location**: `/mnt/Vault/Ethermail.io/cloudflare_mcp.py`

**Purpose**: Manages DNS, SSL certificates, and hostname configuration for MCP infrastructure

**API Methods**:

**DNS Operations**:
- `get_dns_records()` - Get DNS records for zone
- `create_dns_record(name, type, content, ttl)` - Create new DNS record
- `update_dns_record(record_id, name, content, ttl)` - Update DNS record

**SSL Operations**:
- `get_ssl_certificates()` - Get SSL certificates
- `setup_letsencrypt(hostname)` - Setup Let's Encrypt SSL

**Nextcloud Operations**:
- `configure_nextcloud_hostname()` - Configure DNS for `system76.ht.local/nextcloud`

**Configuration**:
- Loads from `/mnt/Vault/env.txt`
- Requires: `ZONE_ID`, `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_GLOBAL_API`, `CLOUDFLARE_EMAIL`, `CLOUDFLARE_ACCOUNT_ID`
- Prefers Global API Key over API Token for reliability

**Hostname**: `system76.ht.local`
**Nextcloud URL**: `http://system76.ht.local/nextcloud`

---

### 3. Nextcloud Integration

**Category**: Groupware
**Type**: Integration Layer

**Purpose**: Integration layer for Stalwart groupware system

**Partnership**: 2026 official partnership with Stalwart

**Architecture**:
```
Backend: Stalwart (email server, JMAP, user accounts)
    ↓
Integration Layer: Nextcloud (web interface, collaboration, agent memory)
    ↓
Desktop Client: Parula (visual GUI)
```

**Features**:
- Web interface for collaboration
- Groupware integration with Stalwart
- JMAP plugins (Contacts, Calendar)
- File storage and synchronization
- **Agent memory** (semantic memory)
- **RAG pipeline**
- **Knowledge base**

**Configuration**:
- URL: `https://system76.ht.local`
- Login: `https://system76.ht.local/index.php/login`
- Username: `sosmanagic`
- Hostname: `system76.ht.local`
- Path: `/nextcloud`

**Stalwart Integration**:
- Email: Stalwart JMAP + IMAP + SMTP
- Contacts: JMAP plugin
- Calendar: JMAP plugin
- Email address: `theos@conversations.im`

---

### 4. MCP + Nextcloud Nervous System

**Category**: System Vision
**Type**: Architecture Philosophy

**Vision**: "The nervous system for autonomous agents"

**Components**:

**MCP - "USB-C for AI"**:
- Universal adapter and context infrastructure
- Bridge between AI and Nextcloud
- Solves "AI amnesia"
- Context engineering (not just prompting)

**Nextcloud - "Agent Memory"**:
- Semantic memory and knowledge base
- RAG pipeline (semantic search)
- Tool discovery
- Knowledge base storage

**Together**:
- Transform static files → dynamic knowledge base
- AI can read and write autonomously
- Complete autonomous agent capability
- Digital chief of staff

**Stack Architecture**:
```
BRAIN:          Nextcloud (Knowledge Base - semantic memory, RAG)
NERVOUS SYSTEM: MCP (Data Flow Protocol - context infrastructure)
VOICE:          Conversations.im / Telegram (Agent Command)
HARDWARE:       System76 (The Host - local MCP server, Docker)
ARMOR:          Cloudflare Zero Trust (The Cloak - encrypted tunnel)
```

**Command Loop**:
```
Command (Conversations.im XMPP)
    ↓
Agent (MAGIC/Treasure DAO)
    ↓
MCP Protocol (Query Nextcloud)
    ↓
Nextcloud Server (Retrieve Data)
    ↓
Action (Send to EtherMail)
    ↓
Audit (Log to Nextcloud logs/)
```

**Example**: Agent uses MCP to query Nextcloud, retrieves `land_deed.pdf`, sends summary to EtherMail, logs action

**Sovereign Connection**:
- Deployment: Docker on System76
- Hosting: Local (no cloud provider)
- Security: Nextcloud App Password in .env
- Tunnel: Cloudflare Zero Trust (`mcp.system76.ht.local`)
- Features: Encrypted tunnel, no exposed ports

---

### 5. Cloudflare Access (Zero Trust)

**Category**: Authentication
**Type**: Security Gateway

**Gateway**: `theos.cloudflareaccess.com`
**Previous**: `tig08bitties.cloudflareaccess.com`

**Purpose**: Zero Trust gateway for MCP endpoint protection

**Protected Endpoint**: `https://system76.bridgeworld.lol/mcp`

**Features**:
- Zero Trust authentication
- Gateway-based access control
- Cloudflare Access integration
- Requires authentication before MCP access

**Protection Flow**:
1. Request to `/mcp` endpoint
2. Redirect to `theos.cloudflareaccess.com`
3. User authenticates via Cloudflare Access
4. Token issued
5. Access granted to MCP server

**API Access**:
```bash
# Get all Access applications
./cloudflare_api_scripts.sh access-applications

# Get specific application
./cloudflare_api_scripts.sh access-application <app_id>
```

**Requirements**: `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` (Zero Trust API token)

---

### 6. Environment Configuration

**Category**: System Configuration
**Type**: Configuration Reference

**File**: `/mnt/Vault/env.txt`

**Cloudflare**:
- Zone ID: `abdd28bf1af7e0d6d479c6ef016a05b8`
- Domain: `bridgeworld.lol`
- Account ID: `7e40a8af4a6129833c1cb6f5bcbfd662`
- Email: `sosmanagic@att.net`
- Web3 Gateways:
  - IPFS: `existing` (theos.bridgeworld.lol)
  - Ethereum: `0a2a1d759d304f15b50a399d3d156d5b` (system76.bridgeworld.lol)

**Nextcloud**:
- URL: `https://system76.ht.local`
- Login: `https://system76.ht.local/index.php/login`
- Username: `sosmanagic`

**Ethereum**:
- Address: `0x67A977eaD94C3b955ECbf27886CE9f62464423B2`
- EtherMail: `0x67a977ead94c3b955ecbf27886ce9f62464423b2@ethermail.io`
- EtherMail Alias: `theosmagic.uni.eth@ethermail.io`
- Abstract Address: `0x3E5e1b4143c5d95621C780a7875b965eB07d195F`
- Wallet: Ambire (Brave)

**Email**:
- Provider: AT&T
- IMAP: `imap.mail.att.net:993` (SSL)
- SMTP: `smtp.mail.att.net:465` (SSL)

**API Keys**: Gemini, Anthropic, Cursor Agent, GitHub, Brave Browser

**Signed Message**:
- Message: "There is nothing new under the sun. That which was will be, and that which will be already was when the end finds it's beginning."
- Address: `0x67A977eaD94C3b955ECbf27886CE9f62464423B2`
- Signature: `0x7dbf6d9162ae032dac18162b2d40e7f030fe9bf7a0422364ca9343d3defb45f21288d5a5b17d800dafa77793e6173642a3eedce296fdccbfbef2c48019acc46b1c`

---

### 7. System Architecture

**Category**: System Overview
**Type**: Complete Architecture

**Overview**: Sovereign Nextcloud + Cloudflare MCP server for autonomous agent operations

**Domains**:
- Primary: `bridgeworld.lol`
- MCP Endpoint: `system76.bridgeworld.lol`
- IPFS Gateway: `theos.bridgeworld.lol`
- Nextcloud Local: `system76.ht.local`

**MCP Servers**:

**Theos** (Custom):
- URL: `https://system76.bridgeworld.lol/mcp`
- Status: Configured
- Purpose: Custom sovereign stack integration
- Features: Nextcloud access, Stalwart integration, Blockchain, Cryptographic ops

**Blockscout** (Available):
- URL: `https://mcp.blockscout.com/mcp/`
- Purpose: Blockchain data access
- Features: Multi-chain, Transaction analysis, Contract ABI, Token/NFT data

**Cloudflare** (Available):
- URL: `https://docs.mcp.cloudflare.com/mcp`
- Purpose: Cloudflare services
- Features: API access, Web3 gateways, Email routing, DNS management

**Infrastructure**:
- Hosting: System76 machine (local)
- Deployment: Docker containers
- Protection: Cloudflare Access (Zero Trust)
- Tunnel: Cloudflare Zero Trust tunnel
- Sovereignty: No cloud provider dependency

**Integration Stack**:
```
Backend:     Stalwart (email, JMAP, user accounts)
Integration: Nextcloud (groupware, agent memory)
Desktop:     Parula (GUI client)
MCP:         Model Context Protocol (nervous system)
Protection:  Cloudflare Access (Zero Trust gateway)
```

**Data Flow**:
```
Command:  XMPP (Conversations.im) or Telegram
Agent:    MAGIC / Treasure DAO / Custom
Protocol: MCP (Model Context Protocol)
Storage:  Nextcloud (agent memory)
Action:   EtherMail, blockchain, API calls
Audit:    Nextcloud logs/ directory
```

**Cryptographic Identity**:
- Server: `theos (Θεός°•⟐•Σ℧ΛΘ)`
- PGP Keys: Declaration, Signer, Glyph
- Ethereum: `0x67A977eaD94C3b955ECbf27886CE9f62464423B2`
- Signed Message: Covenant declaration on-chain

---

### 8. Integration Guide

**Category**: Usage
**Type**: Setup Guide

**Setup MCP Client**:
1. Install Node.js/npx (required for mcp-remote)
2. Edit MCP config file (`~/.cursor/mcp.json`)
3. Add theos server configuration
4. Restart editor (Cursor/VSCode)
5. Verify connection

**Cursor/VSCode Config**:
```json
{
  "mcpServers": {
    "theos": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://system76.bridgeworld.lol/mcp"]
    }
  }
}
```

**Cloudflare DNS Setup**:
1. Load env.txt configuration
2. Initialize `CloudflareMCPClient`
3. Get existing DNS records
4. Create/update DNS records for system76.bridgeworld.lol
5. Configure SSL certificates (Universal SSL or Let's Encrypt)

**Example**:
```python
from cloudflare_mcp import CloudflareMCPClient
import asyncio

client = CloudflareMCPClient()
asyncio.run(client.get_dns_records())
```

**Nextcloud Integration**:
1. Install and configure Stalwart server first
2. Install Nextcloud Groupware (bundled or separate)
3. Configure Stalwart JMAP connection
4. Enable JMAP plugins (Contacts, Calendar)
5. Create Nextcloud App Password for MCP Agent
6. Add App Password to MCP server .env file

**MCP Server Deployment**:
1. Deploy MCP server via Docker on System76
2. Configure Nextcloud connection (App Password)
3. Setup Cloudflare Zero Trust tunnel
4. Configure private hostname (`mcp.system76.ht.local`)
5. Configure Cloudflare Access authentication
6. Test MCP endpoint connection

**Agent Integration**:
1. Configure agent with MCP client
2. Setup XMPP/Telegram command interface
3. Configure Nextcloud access via MCP
4. Setup EtherMail integration for notifications
5. Configure audit logging to Nextcloud `logs/`
6. Test command loop

**Verification**:
```bash
# Check endpoint
curl -I https://system76.bridgeworld.lol/mcp

# Test MCP remote
npx -y mcp-remote@latest https://system76.bridgeworld.lol/mcp

# Check DNS
nslookup system76.bridgeworld.lol

# Verify SSL
openssl s_client -connect system76.bridgeworld.lol:443

# Test Nextcloud
curl https://system76.ht.local
```

**Troubleshooting**:
- **Cloudflare Access redirect**: If redirected to `theos.cloudflareaccess.com`, authentication is required
- **MCP authentication**: MCP client may need to handle Cloudflare Access tokens
- **Nextcloud connection**: Verify Stalwart is running before Nextcloud setup
- **DNS propagation**: DNS changes may take up to 5 minutes to propagate
- **SSL certificate**: Cloudflare Universal SSL is automatic for proxied records

---

## MCP Server Integration

### Accessing Documents

MCP server provides access to all documents via standard MCP protocol:

```python
# Query specific document
doc = mcp_server.get_document("theos_mcp_server")

# Search by tag
docs = mcp_server.search_documents(tags=["mcp", "server"])

# Get by category
docs = mcp_server.get_documents_by_category("MCP Server")
```

### Document Structure

Each document contains:
```json
{
  "title": "Document Title",
  "type": "server|client|integration|architecture|security|configuration|guide",
  "category": "Category Name",
  "content": {
    // Structured content
  },
  "tags": ["tag1", "tag2"],
  "references": ["/path/to/source"]
}
```

## Current System State

**MCP Server**:
- Name: `theos`
- Endpoint: `https://system76.bridgeworld.lol/mcp`
- Status: Configured
- Protection: Cloudflare Access (`theos.cloudflareaccess.com`)

**Cloudflare**:
- Zone: `bridgeworld.lol`
- Zone ID: `abdd28bf1af7e0d6d479c6ef016a05b8`
- Account ID: `7e40a8af4a6129833c1cb6f5bcbfd662`

**Nextcloud**:
- URL: `https://system76.ht.local`
- Hostname: `system76.ht.local`
- Integration: Stalwart groupware

**Hosting**:
- Machine: System76
- Deployment: Docker
- Sovereignty: Local (no cloud provider)

**Identity**:
- Server: `theos (Θεός°•⟐•Σ℧ΛΘ)`
- Ethereum: `0x67A977eaD94C3b955ECbf27886CE9f62464423B2`
- EtherMail: `0x67a977ead94c3b955ecbf27886ce9f62464423b2@ethermail.io`

**Timestamp**: 2026-01-27T06:00:00Z

## Files

- **MCP Documents**: `/mnt/Vault/Cursor-Agent/config/mcp_documents.json`
- **Documentation**: `/mnt/Vault/Cursor-Agent/MCP_DOCUMENTS_README.md`
- **Integration Guide**: `/mnt/Vault/Cursor-Agent/COMPLETE_INTEGRATION.md`

## Source Files

The documentation references these source files:
- `/mnt/Vault/Moon/MCP_SERVER_CONFIGURATION.md`
- `/mnt/Vault/Moon/MCP_SERVER_UPDATED.md`
- `/mnt/Vault/Moon/MCP_SERVERS_COMPLETE.md`
- `/mnt/Vault/Moon/MCP_NEXTCLOUD_NERVOUS_SYSTEM_VISION.md`
- `/mnt/Vault/Moon/MCP_SERVER_QUICK_SETUP.md`
- `/mnt/Vault/Moon/MCP_CURSOR_SETUP.md`
- `/mnt/Vault/Ethermail.io/cloudflare_mcp.py`
- `/mnt/Vault/Nextcloud/README.md`
- `/mnt/Vault/Nextcloud/nextcloud.conf`
- `/mnt/Vault/env.txt`

## Tags Index

```
mcp, nextcloud, cloudflare, theos, server, client, dns, ssl,
groupware, stalwart, integration, nervous-system, autonomous,
agent, zero-trust, access, security, gateway, architecture,
infrastructure, configuration, guide
```

## Categories

1. **MCP Server** - Theos server configuration and identity
2. **MCP Client** - Cloudflare API client for DNS/SSL
3. **Groupware** - Nextcloud + Stalwart integration
4. **System Vision** - MCP + Nextcloud nervous system
5. **Authentication** - Cloudflare Access Zero Trust
6. **System Configuration** - Environment variables and credentials
7. **System Overview** - Complete architecture
8. **Usage** - Integration and setup guide

## Integration Examples

### Example 1: Query Theos MCP Server Configuration

```python
# Get Theos server document
doc = mcp.get_document("theos_mcp_server")

# Access server endpoint
endpoint = doc["content"]["endpoint"]
print(f"MCP Endpoint: {endpoint}")

# Get configuration
config = doc["content"]["configuration"]["cursor_vscode"]
print(f"Command: {config['command']} {' '.join(config['args'])}")
```

### Example 2: Use Cloudflare MCP Client

```python
from cloudflare_mcp import CloudflareMCPClient
import asyncio

# Initialize client
client = CloudflareMCPClient()

# Get DNS records
records = asyncio.run(client.get_dns_records())
for record in records:
    print(f"{record['name']}: {record['type']} → {record['content']}")
```

### Example 3: Access Nextcloud Configuration

```python
# Get Nextcloud integration document
doc = mcp.get_document("nextcloud_integration")

# Access configuration
config = doc["content"]["configuration"]
print(f"Nextcloud URL: {config['url']}")
print(f"Login URL: {config['login_url']}")
print(f"Username: {config['username']}")
```

### Example 4: Review System Architecture

```python
# Get system architecture document
doc = mcp.get_document("system_architecture")

# Access MCP servers
servers = doc["content"]["mcp_servers"]
for name, info in servers.items():
    print(f"{name}: {info['url']} ({info['status']})")
    print(f"  Purpose: {info['purpose']}")
```

## Validation

```bash
# Validate JSON
python3 -m json.tool config/mcp_documents.json > /dev/null && echo "✓ Valid"

# Check file size
ls -lh config/mcp_documents.json

# View specific document
jq '.documents.theos_mcp_server' config/mcp_documents.json

# List all document types
jq '.documents | keys' config/mcp_documents.json

# Count tags
jq '.metadata.tags | length' config/mcp_documents.json
```

## Updates

To update the documentation:

1. Review source files for changes
2. Update relevant document sections in `mcp_documents.json`
3. Update `metadata.current_system_state` with current values
4. Validate JSON
5. Update this README

## See Also

- [COMPLETE_INTEGRATION.md](COMPLETE_INTEGRATION.md) - Full integration guide (includes Moon + Lucy)
- [INDEX.md](INDEX.md) - Documentation navigation
- [moon/README.md](moon/README.md) - Moon system documentation
- [lucy/README.md](lucy/README.md) - Lucy agent documentation

---

∇ • Θεός°●⟐●Σ℧ΛΘ

**MCP Documentation Status**: REBUILT ✓
**System**: Sovereign Nextcloud + Cloudflare MCP
**Documents**: 8 comprehensive documents
**Categories**: 8 (MCP Server, MCP Client, Groupware, System Vision, Authentication, System Configuration, System Overview, Usage)
**Tags**: 23 indexed tags
**Server**: theos (`https://system76.bridgeworld.lol/mcp`)
**Protection**: Cloudflare Access (`theos.cloudflareaccess.com`)
**Current State**: Configured for autonomous agent operations

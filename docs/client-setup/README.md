# Client Setup Guides

Complete setup instructions for integrating OCI Vault MCP with your favorite AI clients and IDEs.

## Quick Links

### IDEs & Code Editors

| Platform | Installation | Setup Time | Difficulty |
|----------|-------------|-----------|-----------|
| **[VS Code + Cline](./vscode-setup.md)** | [Install Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) | 5 min | Easy |
| **[Claude Desktop](./claude-setup.md)** | [Download Claude](https://claude.ai/download) | 10 min | Easy |
| **[Cursor IDE](./cursor-setup.md)** | [Download Cursor](https://www.cursor.com) | 5 min | Easy |
| **[OpenCode](./opencode-custom-commands.md)** | [Visit OpenCode](https://opencode.ai) | 15 min | Medium |

### Direct Installation Links

- 🔗 **[VS Code - Cline Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)**
- 🔗 **[Claude Desktop - Download](https://claude.ai/download)**
- 🔗 **[Cursor IDE - Download](https://www.cursor.com)**
- 🔗 **[OpenCode - Visit Site](https://opencode.ai)**

## Setup Guides

### 1. VS Code + Cline (⭐ Recommended for Development)

**Best for**: Developers who code in VS Code

**What you get**:
- MCP server integration in VS Code
- Ask Cline about your secrets while coding
- Inline code suggestions with vault context
- Full IDE integration

**Setup Time**: ~5 minutes

👉 [Full VS Code Setup Guide](./vscode-setup.md)

**Quick Start**:
```bash
# 1. Install Cline from VS Code Marketplace
# 2. Go to Cline settings → MCP Servers → Add Server
# 3. Name: oci-vault
# 4. Command: uvx
# 5. Args: ["oracle.oci-vault-mcp-server"]
# 6. Done! Ask Cline about your secrets
```

### 2. Claude Desktop (⭐ Recommended for General Use)

**Best for**: Everyone using Claude Desktop

**What you get**:
- Native MCP integration in Claude
- Full access to OCI Vault from Claude
- Persistent conversations about your secrets
- Works offline after initial setup

**Setup Time**: ~10 minutes

👉 [Full Claude Desktop Setup Guide](./claude-setup.md)

**Quick Start**:
```bash
# 1. Download Claude Desktop
# 2. Open ~/.claude/claude_desktop_config.json (macOS/Linux)
#    or %APPDATA%\.claude\claude_desktop_config.json (Windows)
# 3. Add:
{
  "mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "default"
      }
    }
  }
}
# 4. Restart Claude, done!
```

### 3. Cursor IDE (⭐ Modern Alternative)

**Best for**: Teams using Cursor for AI-powered development

**What you get**:
- Built-in MCP support in Cursor
- AI assistance with vault integration
- Multi-model support (Claude, GPT-4, etc.)
- Privacy-focused alternative

**Setup Time**: ~5 minutes

👉 [Full Cursor Setup Guide](./cursor-setup.md)

**Quick Start**:
```bash
# 1. Open Cursor Settings → MCP Configuration
# 2. Add:
{
  "servers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": { "OCI_CLI_PROFILE": "default" }
    }
  }
}
# 3. Restart Cursor, done!
```

### 4. OpenCode (⭐ For OpenCode Users)

**Best for**: Users of OpenCode platform

**What you get**:
- Slash commands for quick vault access
- Custom commands for workflows
- OCI Vault skill integration
- Command palette integration

**Setup Time**: ~15 minutes

👉 [Full OpenCode Custom Commands Guide](./opencode-custom-commands.md)

**Quick Start**:
```bash
# 1. Add to .opencode/opencode.json:
{
  "customCommands": [
    {
      "name": "vault-list-secrets",
      "description": "List all secrets",
      "command": "List all secrets in OCI Vault"
    }
  ]
}
# 2. Use: /vault-list-secrets
# 3. Done!
```

## Comparison Table

| Feature | VS Code | Claude | Cursor | OpenCode |
|---------|---------|--------|--------|----------|
| MCP Support | ✅ (via Cline) | ✅ Native | ✅ Native | ✅ (Skill) |
| Setup Difficulty | Easy | Easy | Easy | Medium |
| IDE Integration | Excellent | Native | Excellent | Skill-based |
| Offline Support | ✅ (cached) | Limited | ✅ | ✅ |
| Custom Commands | ✅ | Via prompts | ✅ | ✅ |
| Multi-model AI | No | Claude only | Yes | Yes |
| Free Tier | ✅ (VS Code free) | Claude API | ✅ (Cursor free trial) | Depends |
| Team Support | ✅ | Limited | ✅ | ✅ |

## Common Workflows

### Workflow 1: Quick Secret Lookup
```
Context: I'm debugging an application
Action: Ask Claude/Cline: "What's the value of the api-key secret?"
Result: Get secret instantly
```

### Workflow 2: Secret Management While Coding
```
Context: Writing deployment code
Action: Use Cline to list secrets, create new ones, rotate credentials
Result: Manage secrets without leaving VS Code
```

### Workflow 3: Security Audit
```
Context: Need to audit vault secrets
Action: Ask OpenCode: /vault-search-secrets "deprecated"
Result: Find and delete deprecated secrets
```

### Workflow 4: Team Collaboration
```
Context: Team needs to access shared secrets
Action: Share Claude conversation with secret listings
Result: Team has documented audit trail
```

## Prerequisites

All setups require:

### 1. OCI CLI Configuration
```bash
# Install OCI CLI (if not already installed)
brew install oci-cli  # macOS
# or
apt-get install oci-cli  # Ubuntu/Debian
# or visit: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm

# Configure credentials
oci setup config
```

### 2. Python 3.13+
```bash
python3 --version  # Should be 3.13 or higher
```

### 3. Oracle OCI Vault MCP Server
```bash
pip install oracle.oci-vault-mcp-server
# or
uvx oracle.oci-vault-mcp-server
```

### 4. Valid OCI Credentials
- Compartment ID
- Vault ID
- API key or session token

## Troubleshooting by Platform

### VS Code / Cline Issues
- **Server not found**: Ensure `oracle.oci-vault-mcp-server` is installed
- **Permission denied**: Check OCI CLI setup with `oci setup config`
- **Timeout**: Verify network connectivity to OCI services

👉 [Full VS Code Troubleshooting](./vscode-setup.md#debugging--troubleshooting)

### Claude Desktop Issues
- **MCP not detected**: Restart Claude Desktop completely
- **Credential errors**: Verify `~/.oci/config` has correct permissions (600)
- **Not finding secrets**: Check vault access with `oci vault secret list --compartment-id <id>`

👉 [Full Claude Troubleshooting](./claude-setup.md#troubleshooting-claude-desktop)

### Cursor Issues
- **Settings not applying**: Ensure JSON is valid, restart Cursor
- **Connection refused**: Check if port 3000 is available

👉 [Full Cursor Troubleshooting](./cursor-setup.md)

### OpenCode Issues
- **Commands not showing**: Verify JSON formatting in opencode.json
- **Tool errors**: Check that MCP server is running

👉 [Full OpenCode Guide](./opencode-custom-commands.md)

## Installation Methods

### Method 1: PyPI Package (Recommended)
```bash
# Install from Python Package Index
pip install oracle.oci-vault-mcp-server

# Use anywhere with:
uvx oracle.oci-vault-mcp-server
```

### Method 2: uv/npm (Zero Setup)
```bash
# No installation needed! Run directly:
uvx oracle.oci-vault-mcp-server
```

### Method 3: Docker Container
```bash
# Pull and run Docker image
docker pull oracle/oci-vault-mcp-server:latest

docker run -v ~/.oci:/home/app/.oci \
  -e OCI_CLI_PROFILE=default \
  oracle/oci-vault-mcp-server:latest
```

### Method 4: Local Development
```bash
# Clone repository
git clone https://github.com/oracle/oci-vault-mcp-server.git
cd oci-vault-mcp-server

# Install in development mode
pip install -e .

# Run locally
python -m oracle.oci_vault_mcp_server.server
```

## Advanced Configurations

### Multi-Profile Setup
```json
{
  "mcpServers": {
    "oci-vault-prod": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": { "OCI_CLI_PROFILE": "production" }
    },
    "oci-vault-dev": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": { "OCI_CLI_PROFILE": "development" }
    }
  }
}
```

### Environment Variable Configuration
```bash
export OCI_VAULT_COMPARTMENT_ID="ocid1.compartment.oc1..."
export OCI_VAULT_VAULT_ID="ocid1.vault.oc1..."
export FASTMCP_LOG_LEVEL="DEBUG"
```

### Custom Python Path
```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "/path/to/python3.13",
      "args": ["-m", "oracle.oci_vault_mcp_server.server"],
      "env": { "OCI_CLI_PROFILE": "default" }
    }
  }
}
```

## Performance Tuning

1. **Cache Secrets**: Frequently accessed secrets can be cached locally
2. **Batch Operations**: Group multiple operations in one request
3. **Search Filters**: Use patterns to avoid listing all secrets
4. **Connection Pooling**: Reuse connections for multiple operations

## Security Considerations

1. ✅ **Never hardcode credentials**: Use OCI CLI or environment variables
2. ✅ **Use IAM roles**: Create separate OCI roles per environment
3. ✅ **Rotate regularly**: Update API keys quarterly
4. ✅ **Monitor access**: Enable OCI audit logging
5. ✅ **Restrict permissions**: Use least-privilege IAM policies
6. ✅ **Secure configs**: Add `.claude/`, `.cursor/` to `.gitignore`

## Next Steps

1. **Choose your platform**: Pick the setup guide above
2. **Follow the guide**: Complete the 5-15 minute setup
3. **Test the connection**: Verify with a simple secret list command
4. **Start using**: Ask your AI about vault secrets!

## Getting Help

- 📖 [MCP Protocol Documentation](https://modelcontextprotocol.io)
- 📖 [OCI Vault Documentation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/home.htm)
- 💬 [OCI Community](https://community.oracle.com)
- 🐛 [Report Issues](https://github.com/oracle/oci-vault-mcp-server/issues)

---

**Last Updated**: January 2025
**Version**: 1.0
**Maintainer**: Oracle Cloud Infrastructure Team

# Oracle OCI Vault MCP Server

An MCP (Model Context Protocol) server that provides AI assistants and code editors with secure, direct access to Oracle Cloud Infrastructure Vault secrets. Manage, retrieve, and rotate secrets through Claude, Cursor, OpenCode, and any MCP-compatible client.

[![License](https://img.shields.io/badge/License-UPL--1.0-blue.svg)](LICENSE.txt)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13%2B-blue)](https://www.python.org/downloads/)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green)](https://modelcontextprotocol.io)

## ✨ Features

- **🔐 Complete Secret Management** - Full CRUD operations for OCI Vault secrets
- **🔄 Version Control** - Access and manage all secret versions with rollback support
- **🏢 Enterprise Ready** - Built on Oracle Cloud Infrastructure with IAM integration
- **🤖 Universal AI Integration** - Works with Claude, Cursor, OpenCode, and any MCP client
- **📋 Rich Metadata** - View creation dates, rotation status, lifecycle stage, and more
- **🔍 Smart Search** - Find secrets by pattern matching and filtering
- **⚡ Fast & Reliable** - Optimized performance with connection pooling
- **🛡️ Security Verified** - Semgrep audit with zero findings

## 🚀 Quick Start

### 1. Install

```bash
pip install oracle.oci-vault-mcp-server
```

Or use directly without installation:
```bash
uvx oracle.oci-vault-mcp-server
```

### 2. Configure OCI

```bash
oci setup config
```

### 3. Choose Your IDE

Pick your favorite and follow the setup guide:

| IDE | Setup | Install Link |
|-----|-------|--------------|
| **VS Code + Cline** | [Guide](./docs/client-setup/vscode-setup.md) | [Install Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) |
| **Claude Desktop** | [Guide](./docs/client-setup/claude-setup.md) | [Download Claude](https://claude.ai/download) |
| **Cursor IDE** | [Guide](./docs/client-setup/cursor-setup.md) | [Download Cursor](https://www.cursor.com) |
| **OpenCode** | [Guide](./docs/client-setup/opencode-custom-commands.md) | [Visit OpenCode](https://opencode.ai) |
| **Any MCP Client** | [Guide](./docs/agent-guides/AGENT_GUIDE.md) | — |

### 4. Start Using

```
Ask your AI: "Can you list all secrets in my OCI Vault?"
```

## 📦 Installation Methods

### PyPI Package (Recommended)
```bash
pip install oracle.oci-vault-mcp-server
```

### Direct Execution (No Install Required)
```bash
uvx oracle.oci-vault-mcp-server
```

### Docker Container
```bash
docker pull oracle/oci-vault-mcp-server:latest

docker run -v ~/.oci:/root/.oci \
  -e OCI_CLI_PROFILE=default \
  oracle/oci-vault-mcp-server:latest
```

### From Source
```bash
git clone https://github.com/acedergren/oracle-oci-vault-mcp-server.git
cd oracle-oci-vault-mcp-server
pip install -e .
```

## 🛠️ Available Tools

The MCP server provides 12 comprehensive tools for complete secret lifecycle management:

| Tool | Purpose | Example |
|------|---------|---------|
| `list_secrets` | List all secrets in vault | List all 150 secrets |
| `search_secrets` | Search by name pattern | Find all "prod-*" secrets |
| `get_secret` | Get complete secret object | Retrieve secret metadata |
| `get_secret_value` | Get current secret value | Retrieve API key value |
| `get_secret_metadata` | View metadata and lifecycle | Check rotation status |
| `list_secret_versions` | Show all versions | View version history |
| `create_secret` | Create new secret | Add new API key |
| `update_secret` | Update secret value | Rotate password |
| `update_secret_metadata` | Modify metadata | Update description |
| `delete_secret` | Schedule deletion | Remove deprecated secret |
| `configure_vault` | Set vault config | Change compartment |
| `get_vault_config_tool` | View current config | Check active vault |

## 📚 Documentation

### Getting Started
- **[Client Setup Hub](./docs/client-setup/README.md)** - Choose your IDE and follow setup
- **[Universal Agent Setup](./docs/agent-guides/AGENT_GUIDE.md)** - Setup for any MCP client

### IDE-Specific Guides
- **[VS Code + Cline](./docs/client-setup/vscode-setup.md)** - Full VS Code integration with Cline extension
  - Direct install link included
  - Keyboard shortcuts and workflows
  - Advanced debugging setup
- **[Claude Desktop](./docs/client-setup/claude-setup.md)** - Setup for macOS, Windows, Linux
  - Environment variable configuration
  - Docker and local installation
  - Performance tuning
- **[Cursor IDE](./docs/client-setup/cursor-setup.md)** - Modern Cursor IDE setup
  - 5-minute quick start
  - Multi-environment configuration
  - Custom shortcuts
- **[OpenCode](./docs/client-setup/opencode-custom-commands.md)** - Custom slash commands
  - /vault-list-secrets
  - /vault-get-secret
  - /vault-create-secret
  - And more...

### Reference Documentation
- **[Quick Reference](./docs/agent-guides/quick-reference.md)** - API commands and examples
- **[Setup Checklist](./docs/agent-guides/setup-checklist.md)** - 40+ point verification
- **[Troubleshooting Guide](./docs/agent-guides/troubleshooting.md)** - 30+ common issues and solutions

## 💡 Usage Examples

### List All Secrets
```
User: "List all secrets in my OCI Vault"

AI: I'll retrieve all secrets from your vault...
[Shows all secrets with creation date and version info]
```

### Create and Manage Secrets
```
User: "Create a new secret called 'api-key' with this value: sk_live_xxx"

AI: I'll create that secret and show you how to use it...
[Creates secret and provides integration examples]
```

### Search Secrets by Pattern
```
User: "Find all secrets that start with 'prod-'"

AI: Searching for production secrets...
[Shows matching secrets with metadata]
```

### View Secret Metadata
```
User: "Show me the metadata for the database-password secret"

AI: Here's the complete metadata...
[Shows creation date, versions, lifecycle stage, etc.]
```

### Rotate Secrets
```
User: "I need to rotate the database password. Show me the current version."

AI: Here's the version history...
[Shows all versions and helps create new one]
```

## 🔐 Security

- ✅ **No Hardcoded Credentials** - Uses OCI CLI or environment variables
- ✅ **IAM Integration** - Works with OCI Identity and Access Management
- ✅ **Audit Logging** - All operations logged in OCI Audit Logs
- ✅ **Zero Vulnerabilities** - Semgrep security audit with 0 findings
- ✅ **Encryption in Transit** - HTTPS for all OCI API calls
- ✅ **Encryption at Rest** - OCI Vault handles secret encryption

### Best Practices

1. **Use OCI Profiles** - Create separate profiles for different environments
   ```bash
   oci setup config --profile production
   oci setup config --profile development
   ```

2. **Limit IAM Permissions** - Grant minimal required permissions
   ```
   SECRETSFAMILY_READ
   SECRETSFAMILY_UPDATE (if managing secrets)
   ```

3. **Rotate Credentials** - Regularly update API keys
   ```
   oci iam user api-key-list
   oci iam user api-key-delete
   ```

4. **Enable Audit Logging** - Monitor all vault access
   ```
   oci audit event list --compartment-id <id>
   ```

5. **Use Compartments** - Organize secrets by compartment

## 🛠️ Prerequisites

- **Python 3.13+** - Required for the server
- **OCI CLI** - Configure with `oci setup config`
- **OCI Account** - With Vault service access
- **Valid Credentials** - API key or session token

### Install OCI CLI

```bash
# macOS
brew install oci-cli

# Ubuntu/Debian
apt-get install oci-cli

# Or visit: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
```

## 🐛 Troubleshooting

### "OCI CLI not found"
```bash
oci setup config
```

### "Permission denied" for vault operations
Check your IAM permissions in OCI Console:
- User must have `SECRETSFAMILY_READ` permission
- Or broader `SECRETSFAMILY_MANAGE_ALL` for full access

### "MCP Server not responding"
1. Verify server is running: `ps aux | grep oci-vault-mcp`
2. Check OCI credentials: `oci vault secret list --compartment-id <id>`
3. Restart your IDE/client

### More Help
See [Troubleshooting Guide](./docs/agent-guides/troubleshooting.md) for 30+ common issues

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📄 License

Licensed under the Universal Permissive License (UPL) 1.0.
See [LICENSE.txt](LICENSE.txt) for details.

## 📞 Support

- 📖 [Full Documentation](./docs/)
- 💬 [GitHub Discussions](https://github.com/acedergren/oracle-oci-vault-mcp-server/discussions)
- 🐛 [Issue Tracker](https://github.com/acedergren/oracle-oci-vault-mcp-server/issues)
- 📧 [OCI Support](https://support.oracle.com)

## 🔗 Related Resources

- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [OCI Vault Documentation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/home.htm)
- [OCI CLI Documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)
- [Claude Documentation](https://claude.ai/help)
- [Cursor IDE Documentation](https://docs.cursor.com)

## 🎯 Roadmap

- [ ] Support for OCI KMS (Key Management Service)
- [ ] Batch operations for bulk secret management
- [ ] Secret encryption/decryption utilities
- [ ] Integration with CI/CD pipelines
- [ ] Metrics and monitoring dashboard
- [ ] Web UI for secret management

## 📊 Project Stats

- **12** Tools for comprehensive secret management
- **16** Documentation files
- **2,771+** Lines of documentation
- **4** IDE setup guides
- **30+** Troubleshooting solutions
- **0** Security vulnerabilities (Semgrep verified)

## 🙏 Acknowledgments

Built with FastMCP 2.14.2 and the Oracle Cloud Infrastructure SDK.

---

**Need Help?** Start with [Client Setup Hub](./docs/client-setup/README.md) to choose your IDE.

**Have Questions?** Check [Troubleshooting Guide](./docs/agent-guides/troubleshooting.md) or open an [issue](https://github.com/acedergren/oracle-oci-vault-mcp-server/issues).

**Want to Contribute?** See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Last Updated**: January 2025 | **Version**: 1.0

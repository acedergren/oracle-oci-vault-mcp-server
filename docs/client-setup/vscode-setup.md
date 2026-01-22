# VS Code Setup Guide for OCI Vault MCP

This guide covers setting up OCI Vault MCP with VS Code using the Cline extension and other MCP-compatible extensions.

## Quick Install

### Install Cline Extension (Recommended for MCP)

**Direct Install Link**: [VS Code Marketplace - Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)

Or paste this into the VS Code Extension search:
```
saoudrizwan.claude-dev
```

### Alternative: Codebase Copilot

**Direct Install Link**: [VS Code Marketplace - Codebase Copilot](https://marketplace.visualstudio.com/items?itemName=Codestral.codebase-copilot)

## Setup with Cline Extension

### Step 1: Install Cline
- Open VS Code
- Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
- Search for "Cline" by Saoud Rizwan
- Click "Install"

### Step 2: Configure MCP Servers in Cline

1. Open Cline settings (click gear icon in Cline panel)
2. Select "MCP Servers" tab
3. Click "Add MCP Server"
4. Fill in the following:

**Server Name**: `oci-vault`

**Command**: `uvx`

**Arguments**:
```json
["oci-vault-mcp-server"]
```

**Environment Variables**:
```json
{
  "OCI_CLI_PROFILE": "default",
  "OCI_CONFIG_PATH": "~/.oci/config"
}
```

### Step 3: Add Your OCI Credentials

1. Ensure OCI CLI is configured:
   ```bash
   oci setup config
   ```

2. Verify configuration:
   ```bash
   oci vault secret list --compartment-id <your-compartment-id>
   ```

3. Cline will use the OCI credentials from your default profile

### Step 4: Test the Connection

1. In VS Code, open the Cline panel (Cmd/Ctrl+Shift+L)
2. Ask Cline:
   ```
   Can you list the secrets in my OCI Vault?
   ```
3. Cline should show MCP server connection status

## Setup with Other Extensions

### Cursor IDE (Built-in MCP Support)

Cursor IDE has built-in MCP support. To configure:

1. Open Settings → MCP Servers
2. Add new server:
   ```json
   {
     "name": "oci-vault",
     "command": "uvx",
     "args": ["oci-vault-mcp-server"],
     "env": {
       "OCI_CLI_PROFILE": "default"
     }
   }
   ```

3. Restart Cursor
4. Use in AI chat: `@oci-vault list secrets`

### Windsurf Extension

1. Install Windsurf extension from VS Code Marketplace
2. Configure MCP servers in Windsurf settings
3. Add OCI Vault server configuration (same as Cline)

## VS Code Settings Configuration

Create or edit `.vscode/settings.json` in your project:

```json
{
  "cline.mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "OCI_CONFIG_PATH": "~/.oci/config"
      }
    }
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  }
}
```

## VS Code Extensions Recommendations

### Essential
- **Cline** - MCP client for Claude in VS Code
- **Python** - Python language support
- **Pylance** - Python type checking
- **REST Client** - Test OCI API calls

### Optional
- **OCI Extension** - Oracle Cloud Infrastructure tools
- **Thunder Client** - API testing
- **YAML** - Configuration file support
- **Markdown All in One** - Documentation editing

## Usage in VS Code

### Example 1: List All Secrets
```
User: Using Cline, can you list all secrets in my OCI Vault?

Cline: I'll use the OCI Vault MCP server to list your secrets...
[Shows all secrets with metadata]
```

### Example 2: Create Secret While Coding
```
User: I'm building a deployment script. Can you create a secret for the API key?

Cline: I'll create that secret and show you how to reference it in your script...
```

### Example 3: Integrate Secrets in Code
```
User: Show me how to use OCI Vault secrets in my Python application

Cline: Here's how to integrate the OCI SDK with Vault secrets...
[Provides code examples]
```

## Keyboard Shortcuts

### Cline Commands
- Open Cline: `Cmd+Shift+L` (macOS) / `Ctrl+Shift+L` (Windows/Linux)
- Quick action: `Cmd+K` (macOS) / `Ctrl+K` (Windows/Linux)
- Edit code: Select code → right-click → "Ask Cline"

### Custom Shortcuts (Optional)

Add to `.vscode/keybindings.json`:
```json
[
  {
    "key": "cmd+shift+v",
    "command": "cline.ask",
    "args": "List OCI Vault secrets"
  },
  {
    "key": "cmd+shift+n",
    "command": "cline.ask",
    "args": "Create a new OCI Vault secret"
  }
]
```

## Debugging & Troubleshooting

### Enable Debug Mode

In VS Code settings:
```json
{
  "cline.debug": true,
  "cline.logLevel": "debug"
}
```

Then check VS Code's Output panel (View → Output → Cline)

### Common Issues

**"MCP Server not responding"**
- Verify `oci-vault-mcp-server` is installed: `pip list | grep oracle`
- Check OCI credentials: `oci vault secret list --compartment-id <id>`
- Restart VS Code

**"Command not found: uvx"**
- Ensure Node.js is installed: `node --version`
- Install uv: `npm install -g uv` or `pipx install uv`
- Restart VS Code

**"Permission denied" for OCI operations**
- Check OCI CLI configuration: `cat ~/.oci/config`
- Verify IAM permissions for your OCI user
- Test OCI CLI directly: `oci vault secret list --compartment-id <id>`

**Cline doesn't show MCP servers**
- Ensure Cline is updated to latest version
- Clear VS Code cache: `rm -rf ~/.vscode`
- Reinstall Cline extension

## Advanced: Local Development Setup

### Step 1: Clone and Install Locally

```bash
git clone https://github.com/oracle/oci-vault-mcp-server.git
cd oci-vault-mcp-server
pip install -e .
```

### Step 2: Point Cline to Local Installation

In `.vscode/settings.json`:
```json
{
  "cline.mcpServers": {
    "oci-vault": {
      "command": "python",
      "args": [
        "-m",
        "oracle.oci_vault_mcp_server.server"
      ],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

### Step 3: Enable Logging

Add to VS Code settings:
```json
{
  "cline.mcpServers": {
    "oci-vault": {
      "env": {
        "FASTMCP_LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

View logs in VS Code Output panel.

## Performance Optimization

### Cache Secrets Locally
Cline can cache frequently accessed secrets to reduce API calls:
```
User: Cache the list of production secrets for faster access
```

### Batch Operations
Group related operations:
```
User: List all "api-*" secrets and show their versions
```

### Use Search Filters
Instead of listing all:
```
User: Find secrets updated in the last 7 days
```

## Security Best Practices

1. **Use Workspace Trust**: VS Code will prompt to trust the workspace
2. **Never commit credentials**: Add `.env` and `~/.oci/config` to `.gitignore`
3. **Review Cline actions**: Always review code suggestions before accepting
4. **Use environment variables**: Store sensitive data in env vars, not config
5. **Limited IAM role**: Create OCI IAM role with minimal required permissions
6. **Monitor logs**: Check VS Code Output for suspicious activity

## Next Steps

- [Claude Setup Guide](./claude-setup.md) - Configure Claude Desktop
- [OpenCode Custom Commands](./opencode-custom-commands.md) - Create shortcuts
- [Agent Setup Guide](../agent-guides/AGENT_GUIDE.md) - Universal setup
- [Quick Reference](../agent-guides/quick-reference.md) - API reference

## Resources

- [VS Code Marketplace - Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs)
- [OCI Vault Documentation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
- [Cline GitHub Repository](https://github.com/saoudrizwan/Cline)

# Cursor IDE Setup Guide for OCI Vault MCP

This guide walks you through setting up the OCI Vault MCP server with Cursor IDE, the modern AI-powered code editor.

## Quick Start

### Prerequisites
- Cursor IDE installed ([download here](https://www.cursor.com))
- OCI CLI configured with valid credentials
- Python 3.13+ installed
- Oracle OCI Vault MCP server installed

### 5-Minute Setup

1. **Open Cursor MCP Settings**
   - Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
   - Type "MCP" and select "Configure MCP Servers"

2. **Add OCI Vault Server**
   ```json
   {
     "servers": {
       "oci-vault": {
         "command": "uvx",
         "args": ["oracle.oci-vault-mcp-server"],
         "env": {
           "OCI_CLI_PROFILE": "default"
         }
       }
     }
   }
   ```

3. **Restart Cursor**
   - Close Cursor completely
   - Reopen Cursor
   - OCI Vault MCP should now be available

4. **Test It**
   - Open Cursor's AI chat
   - Ask: "Can you list the secrets in my OCI Vault?"
   - Success! 🎉

## Detailed Setup Instructions

### Step 1: Install Cursor IDE

Visit [cursor.com](https://www.cursor.com) and download for your OS:
- **macOS**: Download `.dmg` file, drag to Applications
- **Windows**: Download `.exe` installer, run it
- **Linux**: Download `.AppImage` or use package manager

### Step 2: Configure OCI CLI

Ensure your OCI credentials are set up:

```bash
# Configure OCI CLI (if not already done)
oci setup config

# Verify configuration works
oci vault secret list --compartment-id <your-compartment-id>
```

### Step 3: Install OCI Vault MCP Server

```bash
# Option 1: Install from PyPI (Recommended)
pip install oracle.oci-vault-mcp-server

# Option 2: Use directly with uv (no installation needed)
uvx oracle.oci-vault-mcp-server

# Option 3: Use Docker
docker pull oracle/oci-vault-mcp-server:latest
```

### Step 4: Configure MCP in Cursor

**Method A: Via UI (Easiest)**

1. Press `Cmd+Shift+P` / `Ctrl+Shift+P`
2. Search for "MCP"
3. Select "Configure MCP Servers"
4. Click "Add Server"
5. Fill in:
   - **Name**: `oci-vault`
   - **Command**: `uvx`
   - **Arguments**: `["oracle.oci-vault-mcp-server"]`
   - **Environment**: `{"OCI_CLI_PROFILE": "default"}`

**Method B: Edit Config File Directly**

Locate Cursor's settings file:

#### macOS
```bash
~/Library/Application\ Support/Cursor/cline_mcp_config.json
```

#### Windows
```
%APPDATA%\Cursor\cline_mcp_config.json
```

#### Linux
```bash
~/.config/Cursor/cline_mcp_config.json
```

Add or edit to include:
```json
{
  "servers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "OCI_CONFIG_PATH": "~/.oci/config"
      }
    }
  }
}
```

### Step 5: Verify Setup

1. **Restart Cursor** - Close and reopen the application
2. **Check MCP Status** - Look for MCP indicator in status bar
3. **Test Command** - Ask Cursor about your vault:
   ```
   Can you list my OCI Vault secrets?
   ```

## Usage Examples

### Example 1: List All Secrets
```
User: List all secrets in my OCI Vault using MCP

Cursor: I'll access your OCI Vault through the MCP server...
[Shows all secrets with metadata]
```

### Example 2: Create Secret from Code
```
User: I'm writing a deployment script. 
      Can you create a secret for the database password and 
      show me how to use it in my code?

Cursor: I'll create the secret via MCP and add the code...
[Creates secret and provides Python/Node.js code example]
```

### Example 3: Search Secrets
```
User: Find all secrets that start with "prod-"

Cursor: I'll search your vault...
[Shows matching secrets with versions and metadata]
```

### Example 4: Inline Secret References
```
User: I'm writing a configuration file. 
      Can you pull the value of the api-key secret?

Cursor: I'll retrieve that for you...
[Suggests secure way to reference the secret]
```

### Example 5: Secret Rotation Workflow
```
User: I need to rotate the database password secret. 
      Show me the current version and help me create a new one.

Cursor: Let me check the current version...
[Shows version history and helps create new version]
```

## Advanced Configuration

### Multi-Environment Setup

Configure different OCI profiles for different environments:

```json
{
  "servers": {
    "oci-vault-prod": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "production",
        "OCI_CONFIG_PATH": "~/.oci/config"
      }
    },
    "oci-vault-dev": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "development"
      }
    },
    "oci-vault-staging": {
      "command": "uvx",
      "args": ["oracle.oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "staging"
      }
    }
  }
}
```

Then use in chat:
```
@oci-vault-prod list secrets
@oci-vault-dev create secret test-api-key abc123
```

### Docker Configuration

If you prefer containerized setup:

```json
{
  "servers": {
    "oci-vault": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-v", "$HOME/.oci:/root/.oci",
        "-e", "OCI_CLI_PROFILE=default",
        "oracle/oci-vault-mcp-server:latest"
      ],
      "env": {
        "DOCKER_HOST": "unix:///var/run/docker.sock"
      }
    }
  }
}
```

### Local Development Setup

For development or testing:

```json
{
  "servers": {
    "oci-vault": {
      "command": "python",
      "args": [
        "-m",
        "oracle.oci_vault_mcp_server.server"
      ],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "FASTMCP_LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

### Enable Debug Logging

Add to configuration to see detailed logs:

```json
{
  "servers": {
    "oci-vault": {
      "env": {
        "FASTMCP_LOG_LEVEL": "DEBUG",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

View logs in Cursor's Output panel (View → Output).

## Keyboard Shortcuts

### Built-in Cursor Shortcuts
- **Open AI Chat**: `Cmd+K` (macOS) / `Ctrl+K` (Windows/Linux)
- **Command Palette**: `Cmd+Shift+P` / `Ctrl+Shift+P`
- **Select Code + Ask**: Highlight code → `Cmd+K` to ask about it

### Custom Shortcuts (Optional)

Edit `.vscode/keybindings.json` in your project:

```json
[
  {
    "key": "cmd+shift+o",
    "command": "cursor.ask",
    "args": "@oci-vault list secrets"
  },
  {
    "key": "cmd+shift+n",
    "command": "cursor.ask",
    "args": "@oci-vault create secret"
  }
]
```

## Troubleshooting

### Issue: "MCP Server Not Found"

**Solution**:
1. Verify server is installed: `pip list | grep oracle`
2. Check Cursor MCP configuration is valid JSON
3. Restart Cursor completely (not just reload)
4. Check status bar for MCP connection indicator

### Issue: "Command Not Found: uvx"

**Solution**:
1. Ensure Node.js is installed: `which node`
2. Install uv: `npm install -g uv` or `pipx install uv`
3. Restart Cursor
4. Test manually: `uvx oracle.oci-vault-mcp-server --help`

### Issue: "Permission Denied" on OCI Operations

**Solution**:
1. Verify OCI credentials: `cat ~/.oci/config`
2. Check file permissions: `chmod 600 ~/.oci/config`
3. Test OCI CLI: `oci vault secret list --compartment-id <id>`
4. Verify IAM permissions in OCI console

### Issue: "Connection Timeout"

**Solution**:
1. Check internet connectivity: `ping oracle.com`
2. Verify OCI region is accessible from your network
3. Check firewall rules
4. Try specifying explicit region:
   ```json
   {
     "env": {
       "OCI_CLI_PROFILE": "default",
       "OCI_DEFAULT_REGION": "us-phoenix-1"
     }
   }
   ```

### Issue: MCP Server Crashes

**Solution**:
1. Enable debug logging (see Advanced Configuration)
2. Check Cursor logs: View → Output → Cursor
3. Verify Python installation: `python3 --version` (should be 3.13+)
4. Reinstall server: `pip install --force-reinstall oracle.oci-vault-mcp-server`

### Issue: Secrets Not Appearing

**Solution**:
1. Verify compartment ID is correct
2. Check vault contains secrets: `oci vault secret list --compartment-id <id>`
3. Ensure IAM user has `SECRETSFAMILY_READ` permission
4. Try searching by name instead of listing all

## Performance Tips

1. **Cache Results**: Ask Cursor to cache frequently used secrets
2. **Batch Operations**: Group related operations in one request
3. **Use Search**: Search by pattern instead of listing all secrets
4. **Monitor Quotas**: Check OCI API quotas to avoid rate limiting

## Security Best Practices

1. ✅ **Never hardcode credentials**: Use OCI CLI configuration or environment variables
2. ✅ **Use IAM roles**: Create separate OCI roles per environment (prod/dev/staging)
3. ✅ **Rotate keys**: Update OCI API keys quarterly
4. ✅ **Enable audit logging**: Monitor OCI Vault access in OCI Audit Logs
5. ✅ **Restrict permissions**: Use least-privilege IAM policies
6. ✅ **Secure files**: Add `.cursor/`, `.vscode/` to `.gitignore`
7. ✅ **Workspace Trust**: Enable Cursor's workspace trust feature

## Workspace Trust

Cursor has a built-in workspace trust feature. When opening a project:

1. You may see a trust prompt
2. Review the configuration files
3. Click "Trust Workspace" to enable MCP servers
4. MCP will now be available in that workspace

## AI Models in Cursor

Cursor supports multiple AI models. The OCI Vault MCP server works with any model:

- **Claude** (Anthropic) - Default, best for OCI tasks
- **GPT-4** (OpenAI)
- **Gemini** (Google)
- **Local models** (via Ollama)

Choose your preferred model in Cursor settings.

## Integration with Other Tools

### VS Code Extensions
Many VS Code extensions work in Cursor too:
- Python extension
- REST Client
- YAML support
- Git integration

### Project Structure
Cursor respects VS Code workspace settings:
```
your-project/
├── .cursor/          # Cursor-specific settings
├── .vscode/          # VS Code settings (also used by Cursor)
├── .env.example
├── src/
└── README.md
```

## Next Steps

1. **Test with simple queries**: Start with basic commands
2. **Explore advanced features**: Try multi-profile setup
3. **Integrate into workflow**: Use in your daily development
4. **Share with team**: Show colleagues the setup

## Resources

- [Cursor Official Website](https://www.cursor.com)
- [Cursor Documentation](https://docs.cursor.com)
- [OCI Vault Documentation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/home.htm)
- [MCP Protocol](https://modelcontextprotocol.io)
- [OCI CLI Documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)

## Getting Help

- 💬 [Cursor Discord Community](https://discord.gg/cursor)
- 🐛 [Report Issues](https://github.com/oracle/oci-vault-mcp-server/issues)
- 📧 [OCI Support](https://support.oracle.com)

---

**Last Updated**: January 2025
**Version**: 1.0
**Works with**: Cursor v0.30+

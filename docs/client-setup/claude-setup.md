# Claude Desktop & Claude Web Setup Guide for OCI Vault MCP

This guide walks you through setting up the OCI Vault MCP server with Claude Desktop and Claude Web.

## Claude Desktop Setup

### Prerequisites
- Claude Desktop installed ([download here](https://claude.ai/download))
- OCI CLI configured with valid credentials
- Python 3.13+ installed
- The OCI Vault MCP server installed

### Step 1: Locate Your Claude Configuration File

#### macOS
```bash
open ~/.claude/claude_desktop_config.json
```

#### Windows
```powershell
notepad $env:APPDATA\.claude\claude_desktop_config.json
```

#### Linux
```bash
nano ~/.claude/claude_desktop_config.json
```

### Step 2: Add OCI Vault MCP Server Configuration

Add the following to your `claude_desktop_config.json` under the `mcpServers` section:

```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "OCI_CONFIG_PATH": "~/.oci/config"
      }
    }
  }
}
```

### Step 3: Optional - Configure Specific OCI Profile

If you use multiple OCI profiles, customize the configuration:

```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "your-profile-name",
        "OCI_CONFIG_PATH": "~/.oci/config"
      }
    }
  }
}
```

### Step 4: Save and Restart Claude

1. Save the configuration file
2. Close Claude Desktop completely
3. Reopen Claude Desktop
4. You should see "OCI Vault" appear in the MCP Servers list

### Step 5: Test the Connection

In a Claude conversation, ask:

```
Can you list the secrets in my OCI Vault?
```

Claude should respond that the OCI Vault MCP server is available and ready to use.

### Troubleshooting Claude Desktop

**"MCP Server not found" error**
- Verify `oci-vault-mcp-server` is installed: `pip list | grep oracle`
- Check the config file path is correct
- Restart Claude Desktop

**"Permission denied" error**
- Ensure OCI CLI is properly configured: `oci setup config`
- Verify credentials in `~/.oci/config` have proper permissions
- Test OCI CLI directly: `oci vault secret list --compartment-id <id>`

**"Connection timeout" error**
- Check internet connectivity
- Verify OCI tenancy and region are accessible
- Enable debug logging by setting `FASTMCP_LOG_LEVEL=DEBUG`

## Claude Web (via MCP Proxy)

Claude Web doesn't directly support MCP servers, but you can use an MCP proxy service:

### Option 1: Use Claude Web with an MCP Bridge (Recommended)

1. **Set up a local MCP proxy**:
   ```bash
   pip install mcp-bridge
   mcp-bridge --server oci-vault-mcp-server --port 3000
   ```

2. **Access Claude Web at**: `http://localhost:3000`

3. **Connect to Claude Web**: Follow the proxy service's instructions to link your Claude Web session

### Option 2: Use Claude.ai with Desktop App Sync

1. Keep Claude Desktop open with OCI Vault configured
2. Your work syncs to Claude.ai
3. Ask Claude Web (claude.ai) to reference vault operations you discussed in Desktop

## Usage Examples

Once set up, you can use Claude to:

### List Secrets
```
Claude: Can you list all secrets in my vault?
```

### Retrieve a Secret
```
Claude: What's the value of my "database-password" secret?
```

### Create a Secret
```
Claude: Create a new secret called "api-key" with this value: [your-value]
```

### Search Secrets
```
Claude: Find all secrets that start with "prod-"
```

### Manage Versions
```
Claude: Show me all versions of the "api-key" secret
```

### Update Metadata
```
Claude: Update the description for "database-password" to: "Main production database password"
```

## Advanced Configuration

### Option 1: Use Docker Container

If you prefer Docker:

```bash
docker pull oracle/oci-vault-mcp-server:latest

docker run -v ~/.oci:/home/app/.oci \
  -e OCI_CLI_PROFILE=default \
  oracle/oci-vault-mcp-server:latest
```

Then configure Claude to use the Docker container:

```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-v", "$HOME/.oci:/home/app/.oci",
        "-e", "OCI_CLI_PROFILE=default",
        "oracle/oci-vault-mcp-server:latest"
      ]
    }
  }
}
```

### Option 2: Use Local Installation

If you installed from source:

```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "python",
      "args": [
        "-m",
        "oracle.oci_vault_mcp_server.server"
      ],
      "env": {
        "OCI_CLI_PROFILE": "default"
      }
    }
  }
}
```

### Option 3: Environment Variable Security

For sensitive configurations, use environment variables:

```bash
export OCI_VAULT_COMPARTMENT_ID="your-compartment-id"
export OCI_VAULT_VAULT_ID="your-vault-id"
```

Then in config:

```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oci-vault-mcp-server"],
      "env": {
        "OCI_VAULT_COMPARTMENT_ID": "${OCI_VAULT_COMPARTMENT_ID}",
        "OCI_VAULT_VAULT_ID": "${OCI_VAULT_VAULT_ID}"
      }
    }
  }
}
```

## Security Best Practices

1. **Never commit config files**: Add `.claude/` to your `.gitignore`
2. **Use IAM profiles**: Create separate OCI profiles for different purposes
3. **Rotate credentials**: Regularly update your OCI API keys
4. **Limit scope**: Use OCI compartments to limit vault access
5. **Enable logging**: Monitor Claude/OCI interactions in logs
6. **Use variables**: Store sensitive values in environment variables, not config files

## Performance Tips

1. **Cache secrets locally**: Use Claude to cache frequently accessed secrets
2. **Batch operations**: Group multiple secret operations in one request
3. **Use search**: Filter secrets by pattern instead of listing all
4. **Monitor quotas**: Check OCI API quotas to avoid rate limiting

## See Also

- [Claude Documentation](https://claude.ai/help)
- [OCI Vault Documentation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
- [MCP Protocol](https://modelcontextprotocol.io)
- [Agent Setup Guide](../agent-guides/AGENT_GUIDE.md)
- [Quick Reference](../agent-guides/quick-reference.md)

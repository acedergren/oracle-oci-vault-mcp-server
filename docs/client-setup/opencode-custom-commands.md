# OpenCode Custom Commands for OCI Vault MCP

Custom commands allow you to quickly invoke specific OCI Vault operations from OpenCode without typing full queries. This guide shows you how to set them up.

## Setup Instructions

### 1. Add Commands to Your OpenCode Configuration

Edit your OpenCode configuration file (typically in your workspace settings or `.opencode/opencode.json`):

```json
{
  "customCommands": [
    {
      "name": "vault-list-secrets",
      "description": "List all secrets in the vault",
      "command": "List all secrets in OCI Vault using the oracle.oci-vault-mcp-server tool",
      "category": "vault"
    },
    {
      "name": "vault-get-secret",
      "description": "Retrieve a specific secret value",
      "command": "Get the value of secret {secretName} from OCI Vault",
      "category": "vault",
      "parameters": [
        {
          "name": "secretName",
          "description": "Name of the secret to retrieve",
          "required": true
        }
      ]
    },
    {
      "name": "vault-search-secrets",
      "description": "Search secrets by pattern",
      "command": "Search for secrets matching pattern {searchPattern} in OCI Vault",
      "category": "vault",
      "parameters": [
        {
          "name": "searchPattern",
          "description": "Pattern to search for (supports wildcards)",
          "required": true
        }
      ]
    },
    {
      "name": "vault-create-secret",
      "description": "Create a new secret",
      "command": "Create a new secret named {secretName} with value {secretValue} in OCI Vault",
      "category": "vault",
      "parameters": [
        {
          "name": "secretName",
          "description": "Name for the new secret",
          "required": true
        },
        {
          "name": "secretValue",
          "description": "Value to store in the secret",
          "required": true
        }
      ]
    },
    {
      "name": "vault-delete-secret",
      "description": "Delete a secret",
      "command": "Delete the secret named {secretName} from OCI Vault",
      "category": "vault",
      "parameters": [
        {
          "name": "secretName",
          "description": "Name of the secret to delete",
          "required": true
        }
      ]
    },
    {
      "name": "vault-list-versions",
      "description": "List secret versions",
      "command": "List all versions of secret {secretName} in OCI Vault",
      "category": "vault",
      "parameters": [
        {
          "name": "secretName",
          "description": "Name of the secret",
          "required": true
        }
      ]
    },
    {
      "name": "vault-configure",
      "description": "Configure vault connection",
      "command": "Configure OCI Vault connection with compartment {compartmentId} and vault {vaultId}",
      "category": "vault",
      "parameters": [
        {
          "name": "compartmentId",
          "description": "OCI Compartment ID",
          "required": true
        },
        {
          "name": "vaultId",
          "description": "OCI Vault ID",
          "required": true
        }
      ]
    }
  ]
}
```

### 2. Use Custom Commands in OpenCode

Once configured, you can invoke commands using:

```
/vault-list-secrets
```

Or with parameters:

```
/vault-get-secret db-password
/vault-search-secrets "prod-*"
/vault-create-secret api-key sk_live_12345678
/vault-delete-secret temp-token
```

## Advanced: Slash Command Examples

You can also create slash commands that integrate directly with OpenCode's command palette:

### List All Secrets Slash Command
```
/vault-list-secrets
```
**Response**: Returns all secrets available in your OCI Vault with metadata.

### Get Secret Value Slash Command
```
/vault-get-secret my-database-password
```
**Response**: Retrieves and displays the secret value (masked in UI for security).

### Search Secrets Slash Command
```
/vault-search-secrets "api-*"
```
**Response**: Lists all secrets matching the pattern "api-*".

### Create Secret Slash Command
```
/vault-create-secret api-key abc123def456
```
**Response**: Creates a new secret and returns its metadata.

### Delete Secret Slash Command
```
/vault-delete-secret old-token
```
**Response**: Schedules deletion (or immediately deletes if configured) and confirms.

### Get Secret Metadata Slash Command
```
/vault-get-metadata database-password
```
**Response**: Shows creation date, last updated, version info, and other metadata.

### List Secret Versions Slash Command
```
/vault-list-versions api-key
```
**Response**: Shows all versions of the secret with timestamps and version IDs.

## Workflow Examples

### Daily Secret Audit Workflow
```
/vault-list-secrets
# Review all secrets
/vault-search-secrets "deprecated"
# Check for deprecated secrets to clean up
```

### Secret Rotation Workflow
```
/vault-get-metadata db-password
# Check last updated date
/vault-list-versions db-password
# Review version history
/vault-create-secret db-password new_password_123
# Create new version
```

### Troubleshooting Workflow
```
/vault-search-secrets "prod-"
# Find all production secrets
/vault-get-metadata prod-api-key
# Check metadata
```

## Tips & Best Practices

1. **Use Descriptive Names**: Name commands clearly so they appear in command palette
2. **Add Categories**: Organize commands by category (e.g., "vault", "secrets", "admin")
3. **Security**: Never store actual secret values in command definitions
4. **Parameters**: Use required parameters for commands that need input
5. **Descriptions**: Write clear descriptions for discoverability

## Integration with OpenCode Skills

These custom commands work alongside the OCI Vault skill. The skill provides:
- Detailed documentation
- Code examples
- Integration tutorials
- Troubleshooting guides

While custom commands provide:
- Quick access to common operations
- Keyboard shortcuts
- Command palette integration
- Workflow automation

## See Also

- [OpenCode Skill: OCI Vault](../../../.opencode/skills/oci-vault/SKILL.md)
- [Agent Setup Guide](../agent-guides/AGENT_GUIDE.md)
- [Quick Reference](../agent-guides/quick-reference.md)

# OCI Vault MCP Server

## Overview

This server provides tools for interacting with Oracle Cloud Infrastructure (OCI) Vault service. It enables you to:
- List, search, and retrieve secrets stored in OCI Vault
- Create new secrets and manage secret versions
- Update secret metadata and schedule secrets for deletion
- Configure default vault and compartment settings to simplify operations


## Running the server

### STDIO transport mode

```sh
uvx oci-vault-mcp-server
```

### HTTP streaming transport mode

```sh
ORACLE_MCP_HOST=<hostname/IP address> ORACLE_MCP_PORT=<port number> uvx oci-vault-mcp-server
```

## Configuration

You can configure the default vault and compartment in two ways:

### 1. Environment Variables

Set these environment variables before starting the server:

```bash
export OCI_VAULT_ID="ocid1.vault.oc1.phx.xxxxx"
export OCI_COMPARTMENT_ID="ocid1.compartment.oc1.xxxxx"
uvx oci-vault-mcp-server
```

### 2. MCP Settings File (Recommended)

Configure the vault details in your MCP client settings file (e.g., `cline_mcp_settings.json` or `.cursor/mcp.json`):

**For Cline (VS Code):**
```json
{
  "mcpServers": {
    "oracle-oci-vault-mcp-server": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "oci-vault-mcp-server@latest"
      ],
      "env": {
        "OCI_CONFIG_PROFILE": "<profile_name>",
        "OCI_VAULT_ID": "ocid1.vault.oc1.phx.xxxxx",
        "OCI_COMPARTMENT_ID": "ocid1.compartment.oc1.xxxxx",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

**For Cursor:**
```json
{
  "mcpServers": {
    "oracle-oci-vault-mcp-server": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "oci-vault-mcp-server@latest"
      ],
      "env": {
        "OCI_CONFIG_PROFILE": "<profile_name>",
        "OCI_VAULT_ID": "ocid1.vault.oc1.phx.xxxxx",
        "OCI_COMPARTMENT_ID": "ocid1.compartment.oc1.xxxxx",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

### 3. At Runtime with the `configure_vault` Tool

If you start the server without pre-configuring the vault, you can call the `configure_vault` tool:

```
configure_vault(vault_id="ocid1.vault.oc1.phx.xxxxx", compartment_id="ocid1.compartment.oc1.xxxxx")
```

This will set the default vault and compartment for all subsequent operations.

## Tools

| Tool Name | Description |
| --- | --- |
| **Reading Secrets** | |
| list_secrets | Lists all secrets in the configured vault |
| search_secrets | Search for secrets by name |
| get_secret_metadata | Gets the metadata of a secret by ID |
| list_secret_versions | Lists all versions of a secret |
| get_secret_value | Gets the secret value for a specific version |
| get_secret | Gets a complete secret with metadata and versions |
| **Managing Secrets** | |
| create_secret | Creates a new secret in the vault |
| update_secret | Creates a new version of an existing secret |
| update_secret_metadata | Updates secret metadata without creating a new version |
| delete_secret | Schedules a secret for deletion |
| **Configuration** | |
| configure_vault | Set the default vault and compartment |
| get_vault_config_tool | Get the current vault configuration |

### Tool Details

#### list_secrets
Lists all secrets in the configured vault.

**Parameters:**
- `vault_id` (optional): The OCID of the vault. If not provided, uses the configured default.
- `compartment_id` (optional): The OCID of the compartment. If not provided, uses the configured default.
- `limit` (optional): The maximum number of secrets to return

**Returns:** List of `SecretMetadata` objects

**Example usage:**
```
# Using configured defaults
list_secrets()

# Or override defaults
list_secrets(vault_id="ocid1.vault.oc1.phx.xxxxx", compartment_id="ocid1.compartment.oc1.xxxxx")
```

#### search_secrets
Search for secrets by name (supports partial matching).

**Parameters:**
- `name` (required): The name (full or substring) of the secret to search for
- `vault_id` (optional): The OCID of the vault. If not provided, uses the configured default.
- `compartment_id` (optional): The OCID of the compartment. If not provided, uses the configured default.
- `limit` (optional): The maximum number of secrets to return

**Returns:** List of `SecretMetadata` objects

**Example usage:**
```
search_secrets(name="database")
search_secrets(name="password", vault_id="ocid1.vault.oc1.phx.xxxxx")
```

#### get_secret_metadata
Gets the metadata of a specific secret.

**Parameters:**
- `secret_id` (required): The OCID of the secret

**Returns:** `SecretMetadata` object

#### list_secret_versions
Lists all versions of a secret.

**Parameters:**
- `secret_id` (required): The OCID of the secret
- `limit` (optional): The maximum number of versions to return

**Returns:** List of `SecretVersion` objects

#### get_secret_value
Gets the secret value for a specific version.

**Parameters:**
- `secret_id` (required): The OCID of the secret
- `version_number` (optional): The version number of the secret. If not specified, returns the current version.

**Returns:** Dictionary with secret content metadata

#### get_secret
Gets a complete secret with both metadata and all versions.

**Parameters:**
- `secret_id` (required): The OCID of the secret

**Returns:** `Secret` object containing metadata and versions

#### configure_vault
Set the default vault and compartment for all operations.

**Parameters:**
- `vault_id` (required): The OCID of the vault to use as default
- `compartment_id` (required): The OCID of the compartment to use as default

**Returns:** Dictionary with status and configured values

**Example usage:**
```
configure_vault(vault_id="ocid1.vault.oc1.phx.xxxxx", compartment_id="ocid1.compartment.oc1.xxxxx")
```

#### get_vault_config_tool
Get the currently configured default vault and compartment.

**Returns:** Dictionary with current vault_id, compartment_id, and configured status

**Example usage:**
```
get_vault_config_tool()
```

## Creating and Managing Secrets

### create_secret
Creates a new secret in the vault.

**Parameters:**
- `name` (required): The human-friendly name of the secret
- `secret_value` (required): The secret value/content to store
- `description` (optional): A brief description of the secret
- `content_type` (optional): The content type (e.g., 'application/json', 'text/plain'). Defaults to 'application/octet-stream'
- `vault_id` (optional): The OCID of the vault. If not provided, uses the configured default.
- `compartment_id` (optional): The OCID of the compartment. If not provided, uses the configured default.

**Returns:** Dictionary with status, secret_id, and secret metadata

**Example usage:**
```
# Create a simple secret using default vault
create_secret(name="db-password", secret_value="SuperSecurePassword123!")

# Create a JSON secret with description
create_secret(
  name="api-config",
  secret_value='{"api_key": "xxx", "api_secret": "yyy"}',
  description="API configuration for external service",
  content_type="application/json"
)

# Create in a specific vault
create_secret(
  name="prod-database-password",
  secret_value="MySecretPassword",
  vault_id="ocid1.vault.oc1.phx.xxxxx",
  compartment_id="ocid1.compartment.oc1.xxxxx"
)
```

### update_secret
Creates a new version of an existing secret. Each update creates a new version without deleting the previous one.

**Parameters:**
- `secret_id` (required): The OCID of the secret to update
- `secret_value` (required): The new secret value/content
- `content_type` (optional): The content type of the secret (e.g., 'application/json', 'text/plain'). Defaults to 'application/octet-stream'.

**Returns:** Dictionary with status, secret_id, version_number, and version metadata

**Important:** Each call to `update_secret` creates a new version. OCI Vault maintains all versions, and you can retrieve any previous version using `get_secret_value` with a specific `version_number`.

**Example usage:**
```
# Update a secret with new value
update_secret(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  secret_value="UpdatedPassword456"
)

# Update with new content type
update_secret(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  secret_value='{"new_config": "value"}',
  content_type="application/json"
)
```

### update_secret_metadata
Updates the metadata of a secret without creating a new version.

**Parameters:**
- `secret_id` (required): The OCID of the secret to update
- `description` (optional): The new description of the secret
- `freeform_tags` (optional): Free-form tags as a key-value dictionary (e.g., `{"environment": "prod", "team": "platform"}`)
- `defined_tags` (optional): Defined tags as a nested dictionary (e.g., `{"namespace.key": {"subkey": "value"}}`)

**Returns:** Dictionary with status, secret_id, and updated metadata

**Example usage:**
```
# Update the description
update_secret_metadata(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  description="Updated description of this secret"
)

# Add tags
update_secret_metadata(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  freeform_tags={"environment": "production", "team": "backend"}
)

# Update both description and tags
update_secret_metadata(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  description="Database credentials for production",
  freeform_tags={"environment": "prod", "sensitivity": "high"}
)
```

### delete_secret
Schedules a secret for deletion. OCI Vault requires secrets to be scheduled for deletion with a waiting period rather than immediately deleted.

**Parameters:**
- `secret_id` (required): The OCID of the secret to delete
- `time_of_deletion_in_days` (optional): Number of days until the secret is deleted (minimum 7, maximum 30). If not provided, uses OCI default (usually 30 days).

**Returns:** Dictionary with status, secret_id, and scheduled deletion time

**Important:** Once a secret is scheduled for deletion, it enters the `PENDING_DELETION` state and cannot be used or updated. The secret is permanently deleted after the waiting period expires. You can still cancel the deletion if needed (using the OCI CLI or console) before the deletion time arrives.

**Example usage:**
```
# Schedule deletion with default waiting period (30 days)
delete_secret(secret_id="ocid1.secret.oc1.phx.xxxxx")

# Schedule deletion with 7-day waiting period
delete_secret(
  secret_id="ocid1.secret.oc1.phx.xxxxx",
  time_of_deletion_in_days=7
)
```

## Workflow Examples

### Example 1: Create and Version a Secret
```
# Create initial secret
created = create_secret(
  name="my-api-key",
  secret_value="initial-key-value",
  description="API key for external service"
)
secret_id = created.secret_id

# Later, update the secret with a new value (creates new version)
updated = update_secret(
  secret_id=secret_id,
  secret_value="rotated-key-value"
)

# View all versions
versions = list_secret_versions(secret_id=secret_id)

# Retrieve a specific version
old_version = get_secret_value(secret_id=secret_id, version_number=1)
current = get_secret_value(secret_id=secret_id)
```

### Example 2: Organize Secrets with Tags
```
# Create a secret
created = create_secret(
  name="db-password",
  secret_value="SecurePassword123",
  description="Production database password"
)
secret_id = created.secret_id

# Add organizational tags
update_secret_metadata(
  secret_id=secret_id,
  freeform_tags={
    "environment": "production",
    "team": "platform",
    "cost-center": "engineering"
  }
)
```

## Security Best Practices

⚠️ **Important Security Considerations:**

1. **Secret Parameters:** Never log or expose the `secret_value` parameter. MCP servers should handle credentials carefully.

2. **Credential Rotation:** Use `update_secret` to rotate credentials. Keep previous versions for rollback if needed.

3. **Audit Trail:** All operations are logged by OCI Vault. Monitor audit logs for unauthorized access attempts.

4. **IAM Permissions:** Use least-privilege IAM policies. Restrict which users/applications can create, read, or delete secrets.

5. **Version Management:** Each update creates a new version. Clean up old versions if your secret has many updates.

6. **Deletion Policy:** Schedule deletions with appropriate waiting periods to allow time for key rotation in dependent systems.

7. **MCP Client Security:** Ensure your MCP client and configured credentials are stored securely.


## Authentication

This server requires OCI authentication. Ensure you have configured your OCI CLI profile:

```bash
oci session authenticate --region=<region> --tenancy-name=<tenancy_name>
```

The server will use the OCI credentials from your `~/.oci/config` file. You can specify a different profile using the `OCI_CONFIG_PROFILE` environment variable:

```bash
OCI_CONFIG_PROFILE=<profile_name> uvx oci-vault-mcp-server
```

⚠️ **NOTE**: All actions are performed with the permissions of the configured OCI CLI profile. We advise least-privilege IAM setup, secure credential management, safe network practices, secure logging, and warn against exposing secrets.

## Third-Party APIs

Developers choosing to distribute a binary implementation of this project are responsible for obtaining and providing all required licenses and copyright notices for the third-party code used in order to ensure compliance with their respective open source licenses.

## Disclaimer

Users are responsible for their local environment and credential safety. Different language model selections may yield different results and performance.

## License

Copyright (c) 2025 Oracle and/or its affiliates.
 
Released under the Universal Permissive License v1.0 as shown at  
<https://oss.oracle.com/licenses/upl/>.

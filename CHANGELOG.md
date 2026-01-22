# Changelog

All notable changes to the OCI Vault MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-22

### Added

- **Core MCP Server Implementation**: Full Model Context Protocol (MCP) server for Oracle Cloud Infrastructure (OCI) Vault
- **12 Vault Management Tools**:
  - `list_secrets`: List all secrets in a vault
  - `search_secrets`: Search secrets by name pattern
  - `get_secret`: Retrieve complete secret object
  - `get_secret_value`: Get the current secret value
  - `get_secret_metadata`: View secret metadata and lifecycle
  - `list_secret_versions`: Show all versions of a secret
  - `create_secret`: Create a new secret
  - `update_secret`: Update a secret's value
  - `update_secret_metadata`: Modify secret metadata
  - `delete_secret`: Schedule secret deletion
  - `configure_vault`: Set vault configuration
  - `get_vault_config_tool`: View current vault config

- **Multi-Platform Support**:
  - Works with Claude Desktop, Cursor IDE, Cline, OpenCode, and any MCP-compatible client
  - Harness-agnostic design following Vercel agent-skills pattern
  - No platform-specific directories or dependencies

- **Security Features**:
  - OCI CLI authentication with session tokens and API keys
  - Secure credential handling
  - Audit logging support
  - No hardcoded credentials

- **Comprehensive Documentation**:
  - Universal setup guide (`docs/agent-guides/AGENT_GUIDE.md`)
  - IDE-specific setup guides:
    - Claude Desktop
    - VS Code + Cline
    - Cursor IDE
    - OpenCode
  - Quick reference guide
  - Troubleshooting guide (30+ solutions)
  - Setup verification checklist

- **Production-Ready Package**:
  - Published on PyPI as `oci-vault-mcp-server`
  - MCP Registry compatible (`server.json`)
  - Python 3.10+ support
  - FastMCP 2.14.4 framework
  - OCI SDK 2.165.1

### Technical Details

- **Language**: Python 3.10+
- **Framework**: FastMCP 2.14.4
- **OCI SDK**: 2.165.1
- **MCP Protocol**: 2025-12-11
- **License**: Universal Permissive License (UPL-1.0)

### Installation

**Via pip:**
```bash
pip install oci-vault-mcp-server
```

**Via uvx:**
```bash
uvx oci-vault-mcp-server
```

### Usage Example

**Claude Desktop Configuration:**
```json
{
  "mcpServers": {
    "oci-vault": {
      "command": "uvx",
      "args": ["oci-vault-mcp-server"],
      "env": {
        "OCI_CLI_PROFILE": "default",
        "OCI_CONFIG_PROFILE": "DEFAULT"
      }
    }
  }
}
```

### Repository

- **GitHub**: https://github.com/acedergren/oracle-oci-vault-mcp-server
- **PyPI**: https://pypi.org/project/oci-vault-mcp-server/

### Documentation

- **Setup Guide**: See `docs/client-setup/README.md` for IDE-specific instructions
- **Agent Guide**: See `docs/agent-guides/AGENT_GUIDE.md` for universal setup
- **Quick Reference**: See `docs/agent-guides/quick-reference.md` for API examples
- **Troubleshooting**: See `docs/agent-guides/troubleshooting.md` for 30+ solutions

### Contributors

- Oracle MCP Team

---

## Release History

### v1.0.0 (Initial Release)
- Initial release with 12 vault management tools
- Complete documentation and setup guides
- Multi-platform MCP server support
- Production-ready package on PyPI

---

## Future Roadmap

- [ ] Support for additional OCI services (e.g., Key Management Service)
- [ ] Advanced caching mechanisms
- [ ] Batch operations for secrets
- [ ] Enhanced filtering and search capabilities
- [ ] Performance optimizations for large vaults
- [ ] Docker/Container support with pre-built images
- [ ] Integration tests with real OCI environments

---

## Support

For issues, questions, or contributions, please visit:
- **GitHub Issues**: https://github.com/acedergren/oracle-oci-vault-mcp-server/issues
- **Documentation**: https://github.com/acedergren/oracle-oci-vault-mcp-server#readme

## License

Universal Permissive License (UPL-1.0) - See LICENSE.txt for details

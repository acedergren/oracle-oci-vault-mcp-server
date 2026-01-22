# oci-vault-mcp-server - Build Artifacts

This directory contains the built distribution packages for the oci-vault-mcp-server v1.0.0.

## Contents

- `oci_vault_mcp_server-1.0.0.tar.gz` - Source distribution
- `oci_vault_mcp_server-1.0.0-py3-none-any.whl` - Wheel distribution

## Installation

### From PyPI (Recommended)

```bash
pip install oci-vault-mcp-server
```

### From Local Files

```bash
# From wheel
pip install oci_vault_mcp_server-1.0.0-py3-none-any.whl

# From source distribution
pip install oci_vault_mcp_server-1.0.0.tar.gz
```

### Via uvx

```bash
uvx oci-vault-mcp-server
```

## Package Information

- **Name**: oci-vault-mcp-server
- **Version**: 1.0.0
- **Python**: 3.10+
- **License**: UPL-1.0
- **Repository**: https://github.com/acedergren/oracle-oci-vault-mcp-server

## Requirements

- Python 3.10 or higher
- FastMCP 2.14.4
- OCI SDK 2.165.1
- Valid OCI CLI configuration

## Verification

To verify the package integrity:

```bash
# Check wheel
pip install oci_vault_mcp_server-1.0.0-py3-none-any.whl
python3 -c "import oracle.oci_vault_mcp_server; print('OK')"

# Check source distribution
pip install oci_vault_mcp_server-1.0.0.tar.gz
python3 -c "import oracle.oci_vault_mcp_server; print('OK')"
```

## Next Steps

1. **For PyPI Publication**:
   - See [PYPI_PUBLISHING_GUIDE.md](../../PYPI_PUBLISHING_GUIDE.md)
   - Run: `twine upload dist/*`

2. **For Local Testing**:
   - Install in virtual environment
   - Test with your MCP client

3. **For Distribution**:
   - Both files can be distributed
   - Wheel is faster to install
   - Source distribution is more portable

## Support

For issues or questions:
- GitHub Issues: https://github.com/acedergren/oracle-oci-vault-mcp-server/issues
- Documentation: https://github.com/acedergren/oracle-oci-vault-mcp-server

## Build Metadata

- Built: 2025-01-22
- Python Version: 3.10+
- Build Backend: hatchling
- Validated: ✅ PASSED (twine)

---

**Ready for production use and PyPI publication.**

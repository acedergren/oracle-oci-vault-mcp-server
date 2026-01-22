# PyPI Publishing Guide for oci-vault-mcp-server

This guide provides step-by-step instructions for publishing the oci-vault-mcp-server package to PyPI.

## Prerequisites

1. **PyPI Account**
   - Create account at https://pypi.org/account/register/
   - Enable 2FA for security
   - Create an API token (not password-based login)

2. **GitHub Release**
   - Version tag must be created and pushed (v1.0.0 ✅ Already created)
   - CHANGELOG.md must be present (✅ Already created)

3. **Build Tools**
   - `build` - for building distributions
   - `twine` - for uploading to PyPI

## Pre-Publishing Checklist

- [x] Package name finalized: `oci-vault-mcp-server`
- [x] Version set to 1.0.0 in pyproject.toml
- [x] Python version requirements correct (>=3.10)
- [x] Dependencies pinned to specific versions:
  - fastmcp==2.14.4
  - oci==2.165.1
- [x] LICENSE.txt present and correct
- [x] README.md complete
- [x] CHANGELOG.md complete
- [x] All tests passing
- [x] Code scanned for security issues (Semgrep: 0 findings)
- [x] Git tag created (v1.0.0)
- [x] Package builds successfully

## Step 1: Set Up PyPI Credentials

### Option A: Using API Token (Recommended)

1. Create API token at https://pypi.org/manage/account/
2. Create `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi

[pypi]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = pypi-AgEIcH...  # Your API token here
```

3. Set proper permissions:
```bash
chmod 600 ~/.pypirc
```

### Option B: Using PyPI Username/Password

```ini
[pypi]
  username = your_username
  password = your_password  # Not recommended - use API token instead
```

## Step 2: Clean Build Artifacts

```bash
cd src/oci-vault-mcp-server
rm -rf dist build *.egg-info .venv
```

## Step 3: Create Fresh Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 4: Install Build Dependencies

```bash
pip install --upgrade pip
pip install build twine
```

## Step 5: Verify Package Contents

```bash
# Check what will be included
tar -tzf dist/oci_vault_mcp_server-1.0.0.tar.gz | head -20
```

## Step 6: Validate Package Metadata

```bash
# Validate package before upload
twine check dist/*
```

Expected output:
```
Checking distribution dist/oci_vault_mcp_server-1.0.0.tar.gz: Passed
Checking distribution dist/oci_vault_mcp_server-1.0.0-py3-none-any.whl: Passed
```

## Step 7: Test Upload to TestPyPI (Recommended)

First, test on TestPyPI to verify everything works:

1. Create TestPyPI account at https://test.pypi.org/account/register/

2. Create `~/.pypirc` with TestPyPI section:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = pypi-...

[testpypi]
  repository = https://test.upload.pypi.org/legacy/
  username = __token__
  password = pypi-...
```

3. Upload to TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

4. Test installation from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ oci-vault-mcp-server
```

5. Verify the package:

```bash
python3 -c "import oracle.oci_vault_mcp_server; print('Package imported successfully')"
```

## Step 8: Upload to Production PyPI

Once TestPyPI verification passes:

```bash
twine upload dist/*
```

You will be prompted for credentials (or it will use your `.pypirc` file).

## Step 9: Verify Production Upload

1. Visit: https://pypi.org/project/oci-vault-mcp-server/

2. Test installation:

```bash
# In a fresh virtual environment
python3 -m venv test-env
source test-env/bin/activate
pip install oci-vault-mcp-server
```

3. Verify functionality:

```bash
python3 -c "import oracle.oci_vault_mcp_server; print('Installed successfully')"
oci-vault-mcp-server --help
```

## Step 10: Publish Release Announcement

Update GitHub release with PyPI link:

```markdown
## 📦 Installation

Available on PyPI:

```bash
pip install oci-vault-mcp-server
```

Or via uvx:

```bash
uvx oci-vault-mcp-server
```

View on PyPI: https://pypi.org/project/oci-vault-mcp-server/
```

## Troubleshooting

### Error: `Invalid distribution`

**Cause**: Package metadata is invalid

**Solution**:
```bash
twine check dist/*
# Fix issues reported
```

### Error: `403 Forbidden`

**Cause**: Invalid credentials or API token

**Solution**:
- Verify API token is correct
- Check `~/.pypirc` has correct format
- Regenerate token if needed

### Error: `Filename already exists`

**Cause**: Package with this version already uploaded

**Solution**:
- Increment version number
- Upload with new version

## Post-Publishing

1. **Monitor Package Health**
   - Check PyPI page for download stats
   - Monitor GitHub issues
   - Track user feedback

2. **Plan Next Release**
   - Document changes for v1.0.1
   - Track feature requests
   - Plan future roadmap items

3. **Update Documentation**
   - Link to PyPI in README.md
   - Update installation instructions
   - Monitor for installation issues

## Quick Command Reference

```bash
# Build
cd src/oci-vault-mcp-server
python3 -m build

# Validate
twine check dist/*

# Test Upload
twine upload --repository testpypi dist/*

# Production Upload
twine upload dist/*

# Check Upload
pip install oci-vault-mcp-server
```

## Additional Resources

- [PyPI Documentation](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [MCP Registry](https://modelcontextprotocol.io)

## Current Status

### Completed ✅

- Package built successfully
- Name finalized: `oci-vault-mcp-server`
- Dependencies updated to latest versions
- CHANGELOG created
- GitHub release published (v1.0.0)
- Package validated with `twine check`

### Ready for Publication

The package is ready for PyPI publication. Follow the steps above to publish to PyPI.

### Next Steps

1. Run `twine check` to validate
2. Upload to TestPyPI for verification
3. Test installation from TestPyPI
4. Upload to production PyPI
5. Verify installation from PyPI

## Notes

- Package name: `oci-vault-mcp-server` (PyPI)
- Import name: `oracle.oci_vault_mcp_server` (Python)
- MCP server name: `io.acedergren/oci-vault` (MCP protocol)
- Repository: https://github.com/acedergren/oracle-oci-vault-mcp-server
- License: UPL-1.0

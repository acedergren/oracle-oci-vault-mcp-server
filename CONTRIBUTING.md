# Contributing to OCI Vault MCP Server

Thanks for your interest in contributing! This document outlines how to contribute to the OCI Vault MCP Server.

## Overview

The OCI Vault MCP Server is an implementation of the Model Context Protocol (MCP) that enables AI agents and LLMs to interact with Oracle Cloud Infrastructure Vault.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

We welcome contributions in the following areas:

### Bug Fixes
- Help us identify and fix bugs
- Include clear descriptions of the issue and steps to reproduce
- Add tests if applicable

### Documentation Improvements
- Improve setup guides and troubleshooting documentation
- Add examples and use cases
- Fix typos and clarify confusing sections

### Usability Enhancements
- Make the server easier to use with different MCP clients
- Improve error messages and debugging output
- Enhance authentication flows

### Protocol Feature Demonstrations
- Examples that better showcase MCP protocol capabilities
- Implementations of Resources, Prompts, or other underutilized features
- Reference implementations for MCP best practices

## What We Don't Accept

- **New server implementations** - If you're building a different MCP server, publish it to the [MCP Registry](https://registry.modelcontextprotocol.io/)
- **Highly opinionated features** - Features that significantly change the server's scope
- **OCI service expansions** - For coverage of other OCI services, create separate servers

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch**: `git checkout -b feat/your-feature-name`
4. **Make your changes** with clear, descriptive commits
5. **Test your changes** - Run the test suite and verify functionality
6. **Push to your fork** and create a Pull Request

## Development Setup

### Prerequisites

- Python 3.13+
- OCI CLI configured with appropriate credentials
- OCI Vault set up in your tenancy

### Installation

```bash
cd src/oci-vault-mcp-server
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/ -v
```

### Running the Server

```bash
export OCI_CONFIG_PROFILE=default
export OCI_VAULT_ID="ocid1.vault.oc1.phx.xxxxx"
export OCI_COMPARTMENT_ID="ocid1.compartment.oc1.xxxxx"
export FASTMCP_LOG_LEVEL=DEBUG

uvx oci-vault-mcp-server
```

### Code Quality

- **Linting**: `python -m flake8 src/`
- **Type checking**: `python -m mypy src/`
- **Formatting**: `python -m black src/`
- **Security**: `semgrep --config=p/security-audit src/`

## Pull Request Process

1. **Update documentation** - If adding features, update relevant docs
2. **Add tests** - New code should have corresponding tests
3. **Run quality checks** - Ensure all linters and tests pass
4. **Write clear descriptions** - Explain what and why, not just what
5. **Link issues** - Reference related issues in PR description

## Commit Messages

Use clear, descriptive commit messages:

```
feat: Add X capability
- What changed
- Why it changed
- Impact on users

Fixes #123
```

Commit message types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code restructuring
- `test:` - Test additions/modifications
- `chore:` - Build, dependencies, tooling

## Testing

All contributions should include tests. Run the test suite before submitting:

```bash
pytest tests/ --cov=src/oci_vault_mcp --cov-report=html
```

Target coverage: >85% for new code

## Documentation

The server includes multiple types of documentation:

- **README.md** - Basic setup and usage
- **docs/agent-guides/AGENT_GUIDE.md** - Guide for AI agents using the server
- **docs/agent-guides/setup-checklist.md** - Initial setup steps
- **docs/agent-guides/troubleshooting.md** - Common issues and solutions
- **docs/agent-guides/quick-reference.md** - Quick lookup reference

Update relevant documentation when making changes.

## Agent/Harness Agnostic Design

This server is designed to work with any MCP-compatible client (OpenCode, Cursor, Cline, etc.). When contributing:

- Avoid client-specific code or configuration
- Use standard MCP protocol features
- Keep documentation vendor-neutral
- Test with multiple clients if possible

## Security Considerations

When working with OCI Vault, remember:

- Never commit credentials or secrets
- Don't log sensitive data
- Use IAM policies for access control
- Enable audit logging for vault access
- Follow OCI security best practices

## Questions?

- Open a GitHub issue for questions or discussions
- Check existing issues and documentation first
- Join the [MCP community](https://modelcontextprotocol.io/community/communication)

## License

By contributing, you agree that your contributions will be licensed under the Universal Permissive License (UPL-1.0).

---

Thank you for helping make the OCI Vault MCP Server better! 🚀

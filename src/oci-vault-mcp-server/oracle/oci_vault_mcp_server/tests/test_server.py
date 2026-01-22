"""
Copyright (c) 2025, Oracle and/or its affiliates.
Licensed under the Universal Permissive License v1.0 as shown at
https://oss.oracle.com/licenses/upl.
"""

import pytest


def test_import():
    """Test that the module can be imported."""
    from oracle.oci_vault_mcp_server import server  # noqa: F401

    assert True

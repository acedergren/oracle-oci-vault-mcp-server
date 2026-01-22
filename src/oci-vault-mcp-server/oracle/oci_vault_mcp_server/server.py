"""
Copyright (c) 2025, Oracle and/or its affiliates.
Licensed under the Universal Permissive License v1.0 as shown at
https://oss.oracle.com/licenses/upl.
"""

import os
from datetime import datetime, timedelta
from logging import Logger
from typing import Optional

import oci
from fastmcp import FastMCP
from oracle.oci_vault_mcp_server.models import (
    CreateSecretResponse,
    CreateSecretVersionResponse,
    DeleteSecretResponse,
    Secret,
    SecretMetadata,
    SecretVersion,
    UpdateSecretMetadataResponse,
    map_secret_metadata,
    map_secret_version,
)
from pydantic import Field

from . import __project__, __version__

logger = Logger(__name__, level="INFO")

mcp = FastMCP(name=__project__)

# Global configuration for vault and compartment
# These can be set via environment variables or MCP settings
_default_vault_id = os.getenv("OCI_VAULT_ID")
_default_compartment_id = os.getenv("OCI_COMPARTMENT_ID")


def set_vault_config(vault_id: str, compartment_id: str):
    """Set the default vault and compartment for all operations."""
    global _default_vault_id, _default_compartment_id
    _default_vault_id = vault_id
    _default_compartment_id = compartment_id
    logger.info(
        f"Vault config updated: vault_id={vault_id}, compartment_id={compartment_id}"
    )


def get_vault_config() -> tuple[Optional[str], Optional[str]]:
    """Get the current vault and compartment configuration."""
    return _default_vault_id, _default_compartment_id


def get_vault_client():
    logger.info("entering get_vault_client")
    config = oci.config.from_file(
        profile_name=os.getenv("OCI_CONFIG_PROFILE", oci.config.DEFAULT_PROFILE)
    )

    user_agent_name = __project__.split("oracle.", 1)[1].split("-server", 1)[0]
    config["additional_user_agent"] = f"{user_agent_name}/{__version__}"

    private_key = oci.signer.load_private_key_from_file(config["key_file"])
    token_file = os.path.expanduser(config["security_token_file"])
    token = None
    with open(token_file, "r") as f:
        token = f.read()
    signer = oci.auth.signers.SecurityTokenSigner(token, private_key)
    return oci.vault.VaultsClient(config, signer=signer)


def get_secrets_client():
    logger.info("entering get_secrets_client")
    config = oci.config.from_file(
        profile_name=os.getenv("OCI_CONFIG_PROFILE", oci.config.DEFAULT_PROFILE)
    )

    user_agent_name = __project__.split("oracle.", 1)[1].split("-server", 1)[0]
    config["additional_user_agent"] = f"{user_agent_name}/{__version__}"

    private_key = oci.signer.load_private_key_from_file(config["key_file"])
    token_file = os.path.expanduser(config["security_token_file"])
    token = None
    with open(token_file, "r") as f:
        token = f.read()
    signer = oci.auth.signers.SecurityTokenSigner(token, private_key)
    return oci.secrets.SecretsClient(config, signer=signer)


@mcp.tool(description="Lists all secrets in a vault")
def list_secrets(
    vault_id: Optional[str] = Field(
        None,
        description="The OCID of the vault. If not provided, uses the configured default vault.",
    ),
    compartment_id: Optional[str] = Field(
        None,
        description="The OCID of the compartment. If not provided, uses the configured default compartment.",
    ),
    limit: Optional[int] = Field(
        None,
        description="The maximum number of secrets to return. If None, there is no limit.",
        ge=1,
    ),
) -> list[SecretMetadata]:
    secrets: list[SecretMetadata] = []

    try:
        # Use provided values or fall back to defaults
        effective_vault_id = vault_id or _default_vault_id
        effective_compartment_id = compartment_id or _default_compartment_id

        if not effective_vault_id:
            raise ValueError(
                "vault_id is required. Either provide vault_id parameter or set OCI_VAULT_ID environment variable"
            )
        if not effective_compartment_id:
            raise ValueError(
                "compartment_id is required. Either provide compartment_id parameter or set OCI_COMPARTMENT_ID environment variable"
            )

        client = get_vault_client()

        response: oci.response.Response = None
        has_next_page = True
        next_page: str = None

        while has_next_page and (limit is None or len(secrets) < limit):
            kwargs = {
                "vault_id": effective_vault_id,
                "compartment_id": effective_compartment_id,
                "page": next_page,
                "limit": limit,
            }

            response = client.list_secrets(**kwargs)
            has_next_page = response.has_next_page
            next_page = response.next_page if hasattr(response, "next_page") else None

            data: list[oci.vault.models.SecretSummary] = response.data
            for secret_summary in data:
                secrets.append(map_secret_metadata(secret_summary))

        logger.info(f"Found {len(secrets)} Secrets")
        return secrets

    except Exception as e:
        logger.error(f"Error in list_secrets tool: {str(e)}")
        raise e


@mcp.tool(description="Search for secrets by name")
def search_secrets(
    name: str = Field(
        ..., description="The name (full or substring) of the secret to search for"
    ),
    vault_id: Optional[str] = Field(
        None,
        description="The OCID of the vault. If not provided, uses the configured default vault.",
    ),
    compartment_id: Optional[str] = Field(
        None,
        description="The OCID of the compartment. If not provided, uses the configured default compartment.",
    ),
    limit: Optional[int] = Field(
        None,
        description="The maximum number of secrets to return. If None, there is no limit.",
        ge=1,
    ),
) -> list[SecretMetadata]:
    secrets: list[SecretMetadata] = []

    try:
        # Use provided values or fall back to defaults
        effective_vault_id = vault_id or _default_vault_id
        effective_compartment_id = compartment_id or _default_compartment_id

        if not effective_vault_id:
            raise ValueError(
                "vault_id is required. Either provide vault_id parameter or set OCI_VAULT_ID environment variable"
            )
        if not effective_compartment_id:
            raise ValueError(
                "compartment_id is required. Either provide compartment_id parameter or set OCI_COMPARTMENT_ID environment variable"
            )

        client = get_vault_client()

        response: oci.response.Response = None
        has_next_page = True
        next_page: str = None

        while has_next_page and (limit is None or len(secrets) < limit):
            kwargs = {
                "vault_id": effective_vault_id,
                "compartment_id": effective_compartment_id,
                "search_by_name": name,
                "page": next_page,
                "limit": limit,
            }

            response = client.list_secrets(**kwargs)
            has_next_page = response.has_next_page
            next_page = response.next_page if hasattr(response, "next_page") else None

            data: list[oci.vault.models.SecretSummary] = response.data
            for secret_summary in data:
                secrets.append(map_secret_metadata(secret_summary))

        logger.info(f"Found {len(secrets)} Secrets")
        return secrets

    except Exception as e:
        logger.error(f"Error in search_secrets tool: {str(e)}")
        raise e


@mcp.tool(description="Gets the metadata of a secret by ID")
def get_secret_metadata(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret",
    ),
) -> SecretMetadata:
    try:
        client = get_vault_client()
        response = client.get_secret(secret_id=secret_id)
        secret_summary = response.data

        logger.info(f"Retrieved secret metadata: {secret_id}")
        return map_secret_metadata(secret_summary)

    except Exception as e:
        logger.error(f"Error in get_secret_metadata tool: {str(e)}")
        raise e


@mcp.tool(description="Lists all versions of a secret")
def list_secret_versions(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret",
    ),
    limit: Optional[int] = Field(
        None,
        description="The maximum number of versions to return. If None, there is no limit.",
        ge=1,
    ),
) -> list[SecretVersion]:
    versions: list[SecretVersion] = []

    try:
        client = get_secrets_client()

        response: oci.response.Response = None
        has_next_page = True
        next_page: str = None

        while has_next_page and (limit is None or len(versions) < limit):
            kwargs = {
                "secret_id": secret_id,
                "page": next_page,
                "limit": limit,
            }

            response = client.list_secret_versions(**kwargs)
            has_next_page = response.has_next_page
            next_page = response.next_page if hasattr(response, "next_page") else None

            data: list[oci.vault.models.SecretVersionSummary] = response.data
            for version_summary in data:
                versions.append(map_secret_version(version_summary))

        logger.info(f"Found {len(versions)} Secret Versions")
        return versions

    except Exception as e:
        logger.error(f"Error in list_secret_versions tool: {str(e)}")
        raise e


@mcp.tool(description="Gets the secret value for a specific version")
def get_secret_value(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret",
    ),
    version_number: Optional[int] = Field(
        None,
        description="The version number of the secret. If not specified, returns the current version.",
    ),
) -> dict:
    try:
        client = get_secrets_client()

        kwargs = {
            "secret_id": secret_id,
        }
        if version_number is not None:
            kwargs["version_number"] = version_number

        response = client.get_secret_bundle(**kwargs)
        secret_bundle = response.data

        result = {
            "secret_id": secret_bundle.secret_id,
            "version_number": secret_bundle.version_number,
            "stages": secret_bundle.stages,
            "time_created": str(secret_bundle.time_created)
            if secret_bundle.time_created
            else None,
            "content_type": secret_bundle.secret_bundle_content.content_type
            if secret_bundle.secret_bundle_content
            else None,
        }

        # Extract secret value if available
        if secret_bundle.secret_bundle_content:
            content = secret_bundle.secret_bundle_content
            if hasattr(content, "content"):
                # For base64 content, we typically don't return the actual content
                # but can return metadata instead
                result["has_content"] = True
            if hasattr(content, "name"):
                result["name"] = content.name

        logger.info(f"Retrieved secret value: {secret_id}")
        return result

    except Exception as e:
        logger.error(f"Error in get_secret_value tool: {str(e)}")
        raise e


@mcp.tool(description="Gets a complete secret with metadata and versions")
def get_secret(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret",
    ),
) -> Secret:
    try:
        # Get metadata
        vault_client = get_vault_client()
        metadata_response = vault_client.get_secret(secret_id=secret_id)
        metadata = map_secret_metadata(metadata_response.data)

        # Get versions
        secrets_client = get_secrets_client()
        versions_response = secrets_client.list_secret_versions(secret_id=secret_id)
        versions = [map_secret_version(v) for v in versions_response.data]

        logger.info(f"Retrieved complete secret: {secret_id}")
        return Secret(metadata=metadata, versions=versions)

    except Exception as e:
        logger.error(f"Error in get_secret tool: {str(e)}")
        raise e


@mcp.tool(description="Configure the default vault and compartment for all operations")
def configure_vault(
    vault_id: str = Field(
        ...,
        description="The OCID of the vault to use as default",
    ),
    compartment_id: str = Field(
        ..., description="The OCID of the compartment to use as default"
    ),
) -> dict:
    """Configure the default vault and compartment.

    These defaults will be used by list_secrets and search_secrets
    if vault_id and compartment_id parameters are not provided.
    """
    try:
        set_vault_config(vault_id, compartment_id)
        return {
            "status": "success",
            "message": "Vault configuration updated",
            "vault_id": vault_id,
            "compartment_id": compartment_id,
        }
    except Exception as e:
        logger.error(f"Error in configure_vault tool: {str(e)}")
        raise e


@mcp.tool(description="Get the current vault and compartment configuration")
def get_vault_config_tool() -> dict:
    """Get the currently configured default vault and compartment."""
    try:
        vault_id, compartment_id = get_vault_config()
        return {
            "vault_id": vault_id,
            "compartment_id": compartment_id,
            "configured": vault_id is not None and compartment_id is not None,
        }
    except Exception as e:
        logger.error(f"Error in get_vault_config_tool: {str(e)}")
        raise e


@mcp.tool(description="Creates a new secret in the vault")
def create_secret(
    name: str = Field(
        ...,
        description="The human-friendly name of the secret",
    ),
    secret_value: str = Field(
        ...,
        description="The secret value/content to store",
    ),
    description: Optional[str] = Field(
        None,
        description="A brief description of the secret",
    ),
    content_type: Optional[str] = Field(
        None,
        description="The content type of the secret (e.g., 'application/json', 'text/plain'). Defaults to 'application/octet-stream'.",
    ),
    vault_id: Optional[str] = Field(
        None,
        description="The OCID of the vault. If not provided, uses the configured default vault.",
    ),
    compartment_id: Optional[str] = Field(
        None,
        description="The OCID of the compartment. If not provided, uses the configured default compartment.",
    ),
) -> CreateSecretResponse:
    """Create a new secret in the vault."""
    try:
        # Use provided values or fall back to defaults
        effective_vault_id = vault_id or _default_vault_id
        effective_compartment_id = compartment_id or _default_compartment_id

        if not effective_vault_id:
            raise ValueError(
                "vault_id is required. Either provide vault_id parameter or set OCI_VAULT_ID environment variable"
            )
        if not effective_compartment_id:
            raise ValueError(
                "compartment_id is required. Either provide compartment_id parameter or set OCI_COMPARTMENT_ID environment variable"
            )

        client = get_vault_client()

        # Prepare secret content
        secret_content = oci.vault.models.SecretContentDetails(
            content_type=content_type or "application/octet-stream",
            content=secret_value,
        )

        # Create the secret
        create_secret_details = oci.vault.models.CreateSecretDetails(
            compartment_id=effective_compartment_id,
            secret_name=name,
            vault_id=effective_vault_id,
            secret_content=secret_content,
            description=description,
        )

        response = client.create_secret(
            create_secret_details=create_secret_details,
        )

        secret = response.data
        logger.info(f"Created secret: {name} (ID: {secret.id})")

        return CreateSecretResponse(
            status="success",
            message=f"Secret '{name}' created successfully",
            secret_id=secret.id,
            name=secret.secret_name,
            vault_id=secret.vault_id,
            compartment_id=secret.compartment_id,
            lifecycle_state=secret.lifecycle_state,
            time_created=str(secret.time_created) if secret.time_created else None,
        )

    except Exception as e:
        logger.error(f"Error in create_secret tool: {str(e)}")
        raise e


@mcp.tool(description="Creates a new version of an existing secret")
def update_secret(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret to update",
    ),
    secret_value: str = Field(
        ...,
        description="The new secret value/content",
    ),
    content_type: Optional[str] = Field(
        None,
        description="The content type of the secret (e.g., 'application/json', 'text/plain'). Defaults to 'application/octet-stream'.",
    ),
) -> CreateSecretVersionResponse:
    """Create a new version of an existing secret.

    Each update creates a new version, the previous version is not deleted.
    """
    try:
        client = get_secrets_client()

        # Prepare secret content
        secret_content = oci.vault.models.SecretContentDetails(
            content_type=content_type or "application/octet-stream",
            content=secret_value,
        )

        # Create new secret version
        create_secret_version_details = oci.vault.models.CreateSecretVersionDetails(
            secret_content=secret_content,
        )

        response = client.create_secret_version(
            secret_id=secret_id,
            create_secret_version_details=create_secret_version_details,
        )

        version = response.data
        logger.info(f"Created new version for secret: {secret_id}")

        return CreateSecretVersionResponse(
            status="success",
            message="Secret version created successfully",
            secret_id=secret_id,
            version_number=version.version_number,
            lifecycle_state=version.lifecycle_state,
            time_created=str(version.time_created) if version.time_created else None,
            stages=version.stages,
        )

    except Exception as e:
        logger.error(f"Error in update_secret tool: {str(e)}")
        raise e


@mcp.tool(description="Updates the metadata of a secret")
def update_secret_metadata(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret to update",
    ),
    description: Optional[str] = Field(
        None,
        description="The new description of the secret",
    ),
    freeform_tags: Optional[dict] = Field(
        None,
        description="Free-form tags as a key-value dictionary (e.g., {'environment': 'prod', 'team': 'platform'})",
    ),
    defined_tags: Optional[dict] = Field(
        None,
        description="Defined tags as a nested dictionary (e.g., {'namespace.key': {'subkey': 'value'}})",
    ),
) -> UpdateSecretMetadataResponse:
    """Update the metadata of a secret without creating a new version."""
    try:
        client = get_vault_client()

        # Build update details with only provided fields
        update_secret_details = oci.vault.models.UpdateSecretDetails()

        if description is not None:
            update_secret_details.description = description
        if freeform_tags is not None:
            update_secret_details.freeform_tags = freeform_tags
        if defined_tags is not None:
            update_secret_details.defined_tags = defined_tags

        response = client.update_secret(
            secret_id=secret_id,
            update_secret_details=update_secret_details,
        )

        secret = response.data
        logger.info(f"Updated secret metadata: {secret_id}")

        return UpdateSecretMetadataResponse(
            status="success",
            message="Secret metadata updated successfully",
            secret_id=secret.id,
            name=secret.secret_name,
            description=secret.description,
            freeform_tags=secret.freeform_tags,
            defined_tags=secret.defined_tags,
            lifecycle_state=secret.lifecycle_state,
        )

    except Exception as e:
        logger.error(f"Error in update_secret_metadata tool: {str(e)}")
        raise e


@mcp.tool(description="Schedules a secret for deletion")
def delete_secret(
    secret_id: str = Field(
        ...,
        description="The OCID of the secret to delete",
    ),
    time_of_deletion_in_days: Optional[int] = Field(
        None,
        description="Number of days until the secret is deleted (minimum 7, maximum 30). If not provided, uses OCI default (usually 30 days).",
        ge=7,
        le=30,
    ),
) -> DeleteSecretResponse:
    """Schedule a secret for deletion.

    Secrets in OCI Vault cannot be immediately deleted. They must be scheduled
    for deletion and are permanently deleted after the specified waiting period.
    """
    try:
        client = get_vault_client()

        # Build delete details
        delete_secret_details = oci.vault.models.ScheduleSecretDeletionDetails()

        if time_of_deletion_in_days is not None:
            # Calculate the deletion time
            deletion_time = datetime.utcnow() + timedelta(days=time_of_deletion_in_days)
            delete_secret_details.time_of_deletion = deletion_time

        response = client.schedule_secret_deletion(
            secret_id=secret_id,
            schedule_secret_deletion_details=delete_secret_details,
        )

        secret = response.data
        logger.info(f"Scheduled deletion for secret: {secret_id}")

        return DeleteSecretResponse(
            status="success",
            message="Secret scheduled for deletion",
            secret_id=secret.id,
            name=secret.secret_name,
            lifecycle_state=secret.lifecycle_state,
            time_of_deletion=str(secret.time_of_deletion)
            if secret.time_of_deletion
            else None,
        )

    except Exception as e:
        logger.error(f"Error in delete_secret tool: {str(e)}")
        raise e


def main():
    host = os.getenv("ORACLE_MCP_HOST")
    port = os.getenv("ORACLE_MCP_PORT")

    if host and port:
        mcp.run(transport="http", host=host, port=int(port))
    else:
        mcp.run()


if __name__ == "__main__":
    main()

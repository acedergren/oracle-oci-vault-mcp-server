"""
Copyright (c) 2025, Oracle and/or its affiliates.
Licensed under the Universal Permissive License v1.0 as shown at
https://oss.oracle.com/licenses/upl.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

import oci
from pydantic import BaseModel, Field


def _oci_to_dict(obj):
    """Best-effort conversion of OCI SDK model objects to plain dicts."""
    if obj is None:
        return None
    try:
        from oci.util import to_dict as oci_to_dict

        return oci_to_dict(obj)
    except Exception:
        pass
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "__dict__"):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    return None


# region SecretMetadata


class SecretMetadata(BaseModel):
    """
    The metadata for a secret.
    """

    id: Optional[str] = Field(None, description="The OCID of the secret metadata.")
    lifecycle_state: Optional[str] = Field(
        None, description="The current lifecycle state of the secret."
    )
    vault_id: Optional[str] = Field(
        None, description="The OCID of the vault that contains the secret."
    )
    compartment_id: Optional[str] = Field(
        None, description="The OCID of the compartment containing the secret."
    )
    name: Optional[str] = Field(
        None, description="A user-friendly name for the secret."
    )
    description: Optional[str] = Field(
        None, description="A brief description of the secret."
    )
    secret_version_count: Optional[int] = Field(
        None, description="The number of versions of the secret."
    )
    time_created: Optional[datetime] = Field(
        None, description="The date and time the secret was created."
    )
    time_of_current_version: Optional[datetime] = Field(
        None, description="The date and time the current version was created."
    )
    time_of_deletion: Optional[datetime] = Field(
        None, description="The scheduled deletion time of the secret."
    )
    rotation_config: Optional[Dict[str, Any]] = Field(
        None, description="The rotation configuration of the secret."
    )
    freeform_tags: Optional[Dict[str, str]] = Field(
        None,
        description="Free-form tags for this resource. "
        "Each tag is a simple key-value pair with no predefined name, type, or namespace.",
    )
    defined_tags: Optional[Dict[str, Dict[str, Any]]] = Field(
        None,
        description="Defined tags for this resource. Each key is predefined and scoped to a namespace.",
    )


def map_secret_metadata(
    sm: oci.vault.models.SecretSummary,
) -> SecretMetadata:
    """
    Convert an oci.vault.models.SecretSummary to SecretMetadata.
    """
    return SecretMetadata(
        id=getattr(sm, "id", None),
        lifecycle_state=getattr(sm, "lifecycle_state", None),
        vault_id=getattr(sm, "vault_id", None),
        compartment_id=getattr(sm, "compartment_id", None),
        name=getattr(sm, "name", None),
        description=getattr(sm, "description", None),
        secret_version_count=getattr(sm, "secret_version_count", None),
        time_created=getattr(sm, "time_created", None),
        time_of_current_version=getattr(sm, "time_of_current_version", None),
        time_of_deletion=getattr(sm, "time_of_deletion", None),
        rotation_config=_oci_to_dict(getattr(sm, "rotation_config", None)),
        freeform_tags=getattr(sm, "freeform_tags", None),
        defined_tags=getattr(sm, "defined_tags", None),
    )


# endregion

# region Secret


class SecretVersion(BaseModel):
    """
    A version of a secret.
    """

    version_number: Optional[int] = Field(
        None, description="The version number of the secret version."
    )
    time_created: Optional[datetime] = Field(
        None, description="The date and time the secret version was created."
    )
    time_of_deletion: Optional[datetime] = Field(
        None, description="The scheduled deletion time of the secret version."
    )
    lifecycle_state: Optional[str] = Field(
        None, description="The current lifecycle state of the secret version."
    )
    version_stage: Optional[List[str]] = Field(
        None, description="The stages associated with the secret version."
    )


def map_secret_version(
    sv: oci.vault.models.SecretVersionSummary,
) -> SecretVersion:
    """
    Convert an oci.vault.models.SecretVersionSummary to SecretVersion.
    """
    return SecretVersion(
        version_number=getattr(sv, "version_number", None),
        time_created=getattr(sv, "time_created", None),
        time_of_deletion=getattr(sv, "time_of_deletion", None),
        lifecycle_state=getattr(sv, "lifecycle_state", None),
        version_stage=getattr(sv, "version_stage", None),
    )


class Secret(BaseModel):
    """
    A secret stored in the OCI Vault.
    """

    metadata: SecretMetadata = Field(..., description="The metadata of the secret.")
    versions: Optional[List[SecretVersion]] = Field(
        None, description="The versions of the secret."
    )


# endregion

# region CreateSecretResponse


class CreateSecretResponse(BaseModel):
    """
    Response from creating a new secret.
    """

    status: str = Field(..., description="Status of the operation (e.g., 'success')")
    message: str = Field(..., description="Human-readable message about the operation")
    secret_id: str = Field(..., description="The OCID of the newly created secret")
    name: str = Field(..., description="The name of the created secret")
    vault_id: str = Field(
        ..., description="The OCID of the vault containing the secret"
    )
    compartment_id: str = Field(
        ..., description="The OCID of the compartment containing the secret"
    )
    lifecycle_state: str = Field(..., description="The lifecycle state of the secret")
    time_created: Optional[str] = Field(
        None, description="The creation time of the secret"
    )


# endregion

# region CreateSecretVersionResponse


class CreateSecretVersionResponse(BaseModel):
    """
    Response from creating a new secret version.
    """

    status: str = Field(..., description="Status of the operation (e.g., 'success')")
    message: str = Field(..., description="Human-readable message about the operation")
    secret_id: str = Field(..., description="The OCID of the secret")
    version_number: int = Field(
        ..., description="The version number of the new version"
    )
    lifecycle_state: str = Field(
        ..., description="The lifecycle state of the secret version"
    )
    time_created: Optional[str] = Field(
        None, description="The creation time of the secret version"
    )
    stages: Optional[List[str]] = Field(
        None, description="The stages associated with the secret version"
    )


# endregion

# region UpdateSecretMetadataResponse


class UpdateSecretMetadataResponse(BaseModel):
    """
    Response from updating secret metadata.
    """

    status: str = Field(..., description="Status of the operation (e.g., 'success')")
    message: str = Field(..., description="Human-readable message about the operation")
    secret_id: str = Field(..., description="The OCID of the secret")
    name: str = Field(..., description="The name of the secret")
    description: Optional[str] = Field(
        None, description="The description of the secret"
    )
    freeform_tags: Optional[Dict[str, str]] = Field(
        None, description="Free-form tags of the secret"
    )
    defined_tags: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description="Defined tags of the secret"
    )
    lifecycle_state: str = Field(..., description="The lifecycle state of the secret")


# endregion

# region DeleteSecretResponse


class DeleteSecretResponse(BaseModel):
    """
    Response from scheduling secret deletion.
    """

    status: str = Field(..., description="Status of the operation (e.g., 'success')")
    message: str = Field(..., description="Human-readable message about the operation")
    secret_id: str = Field(..., description="The OCID of the secret")
    name: str = Field(..., description="The name of the secret")
    lifecycle_state: str = Field(..., description="The lifecycle state of the secret")
    time_of_deletion: Optional[str] = Field(
        None, description="The scheduled deletion time of the secret"
    )


# endregion

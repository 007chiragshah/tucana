from pydantic import (
    BaseModel,
    IPvAnyAddress,
    model_validator,
    FilePath,
    StringConstraints,
    Field,
    field_validator,
)
from typing import Annotated, Optional
from pathlib import Path


DomainName = Annotated[
    str,
    Field(
        pattern=r"^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$",
        description="A valid domain name (e.g., example.com).",
    ),
]

UnixName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[a-z][-a-z0-9_]*\$?$"),
]

EmailString = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
    ),
]

NodePath = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^(?:[a-zA-Z]:\\|/)?(?:[^<>:\"/\\|?*\n]+(?:\\|/))*[^<>:\"/\\|?*\n]+$",
    ),
]


class K8sClusterConfigContext(BaseModel):
    ip_cp: IPvAnyAddress
    ip1: IPvAnyAddress
    ip2: IPvAnyAddress
    ip3: IPvAnyAddress

    @model_validator(mode="after")
    def check_ip_addresses_match(cls, values):
        if len({values.ip_cp, values.ip1, values.ip2, values.ip3}) < 4:
            raise ValueError("All IP addresses must be different")
        return values


class K8sLoadBalancerConfigContext(BaseModel):
    lb_domain: DomainName
    lb_ingress_ip: IPvAnyAddress
    lb_ingress_domain: DomainName
    lb_public_key: FilePath
    lb_private_key: FilePath

    @model_validator(mode="after")
    def check_ip_addresses_match(cls, values):
        ips = {
            db.installation_data.k8s_cluster_config.ip_cp,
            db.installation_data.k8s_cluster_config.ip1,
            db.installation_data.k8s_cluster_config.ip2,
            db.installation_data.k8s_cluster_config.ip3,
            values.lb_ingress_ip,
        }
        if len(ips) < 5:
            raise ValueError(
                "The load balancer ingress IP addresses must be different from the ones used for the Kubernetes cluster."
            )
        return values

    @model_validator(mode="after")
    @classmethod
    def check_domains_match(cls, values):
        if values.lb_domain == values.lb_ingress_domain:
            raise ValueError("The domains must be different.")
        return values


class DockerImageContext(BaseModel):
    version: str
    image_id: str


class SSHConfigContext(BaseModel):
    ssh_username: UnixName
    private_key_path: FilePath


class DiskConfigContext(BaseModel):
    data_disk_operations_enabled: bool
    data_disk_device_name: Annotated[
        Optional[str], StringConstraints(min_length=1, strip_whitespace=True)
    ]
    data_disk_manually_encrypted: bool
    data_disk_encryption_key: Optional[NodePath] = None

    @model_validator(mode="before")
    @classmethod
    def validate_disk_device_name(cls, values):
        data_disk_operations_enabled = values.get("data_disk_operations_enabled")
        data_disk_device_name = values.get("data_disk_device_name")

        if data_disk_operations_enabled and not data_disk_device_name:
            raise ValueError("The disk device name must be defined.")

        if not data_disk_device_name or not data_disk_operations_enabled:
            values["data_disk_device_name"] = None

        return values

    @model_validator(mode="before")
    @classmethod
    def validate_encryption_key_path_name(cls, values):
        data_disk_operations_enabled = values.get("data_disk_operations_enabled")
        data_disk_manually_encrypted = values.get("data_disk_manually_encrypted")
        data_disk_encryption_key = values.get("data_disk_encryption_key")

        if data_disk_manually_encrypted and not data_disk_encryption_key:
            raise ValueError("The disk encryption key path must be defined.")

        if not data_disk_operations_enabled or not data_disk_manually_encrypted:
            values["data_disk_encryption_key"] = None

        return values

    @field_validator("data_disk_encryption_key")
    @classmethod
    def validate_data_disk_encryption_key(cls, value) -> str:
        if value is not None:
            try:
                Path(value)
            except ValueError:
                raise ValueError(f"{value} is not a valid file path.")
        return value


class ITAuthContext(BaseModel):
    email: EmailString
    password: Annotated[str, StringConstraints(min_length=4, strip_whitespace=True)]


class ClinicalAuthContext(BaseModel):
    email: EmailString
    password: Annotated[str, StringConstraints(min_length=4, strip_whitespace=True)]


class SDCConfigContext(BaseModel):
    key_path: FilePath
    certificate_path: FilePath
    intermediate_certificate_path: FilePath
    certificate_password: Annotated[
        str, StringConstraints(min_length=1, strip_whitespace=True)
    ]

    @field_validator("key_path")
    @classmethod
    def validate_key_path(cls, value: FilePath) -> FilePath:
        if Path(value).name != "consumerLeaf1.key":
            raise ValueError("key_path must be named 'consumerLeaf1.key'")
        return value

    @field_validator("certificate_path")
    @classmethod
    def validate_certificate_path(cls, value: FilePath) -> FilePath:
        if Path(value).name != "consumerLeaf1.crt":
            raise ValueError("certificate_path must be named 'consumerLeaf1.crt'")
        return value

    @field_validator("intermediate_certificate_path")
    @classmethod
    def validate_intermediate_certificate_path(cls, value: FilePath) -> FilePath:
        if Path(value).name != "intermediateCA.crt":
            raise ValueError(
                "intermediate_certificate_path must be named 'intermediateCA.crt'"
            )
        return value


class InstallationData(BaseModel):
    docker_image_config: Optional[DockerImageContext] = None
    ssh_config: Optional[SSHConfigContext] = None
    k8s_cluster_config: Optional[K8sClusterConfigContext] = None
    k8s_lb_config: Optional[K8sLoadBalancerConfigContext] = None
    disk_config: Optional[DiskConfigContext] = None
    it_auth_config: Optional[ITAuthContext] = None
    clinical_auth_config: Optional[ClinicalAuthContext] = None
    sdc_config: Optional[SDCConfigContext] = None


class Database:
    def __init__(self):
        self.installation_data = InstallationData()


db = Database()

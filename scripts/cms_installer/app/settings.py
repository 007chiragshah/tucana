from ipaddress import IPv4Address
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    INGRESS_NODE_IP: IPv4Address
    CONTROL_PLANE_NODE_IP: IPv4Address
    WORKER_NODE_1_PUBLIC_IP: IPv4Address
    WORKER_NODE_2_PUBLIC_IP: IPv4Address
    WORKER_NODE_3_PUBLIC_IP: IPv4Address

    DOCKER_IMAGE_ID: str = "aba815ccfab8"
    DOCKER_IMAGE_VERSION: str = "v2.0.6.alpha.9-offline"

    SSH_CONFIG_USERNAME: str = "ubuntu"
    SSH_PRIVATE_KEY_PATH: Path = Path("./ci-cd-test-cli-installer.pem")
    SDC_KEY_PATH: Path = Path("./consumerLeaf1.key")
    SDC_CERTIFICATE_PATH: Path = Path("./consumerLeaf1.crt")
    SDC_INTERMEDIATE_CERTIFICATE_PATH: Path = Path("./intermediateCA.crt")
    SDC_CERTIFICATE_PASSWORD: str = "sibel"

    LB_PUBLIC_KEY: Path = Path("./k8_lb_public_key")
    LB_PRIVATE_KEY: Path = Path("./k8_lb_private_key")

    IT_ADMIN_EMAIL: str = "admin@sibelhealth.com"
    IT_ADMIN_PASSWORD: str = "adminpass"

    CLINICAL_ADMIN_EMAIL: str = "clinical@sibelhealth.com"
    CLINICAL_ADMIN_PASSWORD: str = "clinicalpass"

    CONTROL_PLANE_DOMAIN: str = "cp.temp.dev.tucana.sibel.health"
    LOAD_BALANCER_INGRESS_DOMAIN: str = "temp.dev.tucana.sibel.health"


config = Settings()

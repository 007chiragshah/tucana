from textual.app import App

from app.models import (
    DockerImageContext,
    SSHConfigContext,
    K8sClusterConfigContext,
    K8sLoadBalancerConfigContext,
    DiskConfigContext,
    InstallationData,
    ITAuthContext,
    ClinicalAuthContext,
    SDCConfigContext,
)
from app.models import db
from app.screens.installation import CommandLogScreen
from app.settings import config

db.installation_data = InstallationData(
    docker_image_config=DockerImageContext(
        version=config.DOCKER_IMAGE_VERSION,
        image_id=config.DOCKER_IMAGE_ID,
    ),
    ssh_config=SSHConfigContext(
        ssh_username=config.SSH_CONFIG_USERNAME,
        private_key_path=config.SSH_PRIVATE_KEY_PATH,
    ),
    k8s_cluster_config=K8sClusterConfigContext(
        ip_cp=config.CONTROL_PLANE_NODE_IP,
        ip1=config.WORKER_NODE_1_PUBLIC_IP,
        ip2=config.WORKER_NODE_2_PUBLIC_IP,
        ip3=config.WORKER_NODE_3_PUBLIC_IP,
    ),
    k8s_lb_config=None,
    disk_config=DiskConfigContext(
        data_disk_operations_enabled=False,
        data_disk_device_name=None,
        data_disk_manually_encrypted=False,
        data_disk_encryption_key=None,
    ),
    it_auth_config=ITAuthContext(
        email=config.IT_ADMIN_EMAIL, password=config.IT_ADMIN_PASSWORD
    ),
    clinical_auth_config=ClinicalAuthContext(
        email=config.CLINICAL_ADMIN_EMAIL, password=config.CLINICAL_ADMIN_PASSWORD
    ),
    sdc_config=SDCConfigContext(
        key_path=config.SDC_KEY_PATH,
        certificate_path=config.SDC_CERTIFICATE_PATH,
        intermediate_certificate_path=config.SDC_INTERMEDIATE_CERTIFICATE_PATH,
        certificate_password=config.SDC_CERTIFICATE_PASSWORD,
    ),
)

db.installation_data.k8s_lb_config = K8sLoadBalancerConfigContext(
    lb_domain=config.CONTROL_PLANE_DOMAIN,
    lb_ingress_ip=config.INGRESS_NODE_IP,
    lb_ingress_domain=config.LOAD_BALANCER_INGRESS_DOMAIN,
    lb_public_key=config.LB_PUBLIC_KEY,
    lb_private_key=config.LB_PRIVATE_KEY,
)


class CmsInstaller(App):
    ENABLE_COMMAND_PALETTE = False

    def on_mount(self) -> None:
        self.push_screen(CommandLogScreen())


app = CmsInstaller()

if __name__ == "__main__":
    app.run()

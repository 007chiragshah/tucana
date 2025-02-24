import asyncio
from ipaddress import IPv4Address
from pathlib import Path

import pytest
from loguru import logger
from textual.pilot import Pilot

from app.installer import get_installer_images_names
from app.main import CmsInstaller
from app.screens.auth_admin import ITAuthConfigScreen
from app.screens.auth_clinical import ClinicalAuthConfigScreen
from app.screens.confirmation import ConfirmationScreen
from app.screens.disk import DiskConfigScreen
from app.screens.docker_images import DockerImageSelectionScreen
from app.screens.installation import CommandLogScreen
from app.screens.k8s_lb import K8sLoadBalancerConfigScreen
from app.screens.k8s_nodes import K8sClusterConfigScreen
from app.screens.sdc import SDCConfigScreen
from app.screens.ssh import SSHConfigScreen
from app.screens.welcome import WelcomeScreen
from app.shortcut import config


class CmsInstallerUserAgent:
    def __init__(self, app: CmsInstaller, pilot: Pilot) -> None:
        self._app = app
        self._pilot = pilot

    async def submit(self):
        next_button = self._app.query_exactly_one("#next-button")
        next_button.press()
        await self._pilot.pause()

    async def fill_welcome_screen(self, key="n") -> None:
        assert isinstance(self._app.screen, WelcomeScreen)

        await self._pilot.press(key)
        await self._pilot.pause()

    async def fill_docker_image_selection_screen(self) -> None:
        # TODO: Accept image name to search and toggle
        assert isinstance(self._app.screen, DockerImageSelectionScreen)

        expected_available_images = set(get_installer_images_names())

        docker_images_options = self._app.query("RadioButton")
        for docker_image_option in docker_images_options:
            assert str(docker_image_option.label) in expected_available_images

        last_radio_button = docker_images_options.last()
        last_radio_button.toggle()
        await self._pilot.pause()
        await self.submit()

    async def fill_ssh_config_screen(
        self, ssh_user: str, ssh_private_key: str | Path
    ) -> None:
        assert isinstance(self._app.screen, SSHConfigScreen)

        ssh_user_input = self._app.query_exactly_one("#ssh_user_input")
        ssh_user_input.value = ssh_user

        ssh_private_key_path = self._app.query_exactly_one("#private_key_path_input")
        ssh_private_key_path.value = str(ssh_private_key)

        await self._pilot.pause()
        await self.submit()

    async def fill_k8s_cluster_config_screen(
        self,
        control_plane_ip: IPv4Address,
        worked_node_1_ip: IPv4Address,
        worked_node_2_ip: IPv4Address,
        worked_node_3_ip: IPv4Address,
    ) -> None:
        assert isinstance(self._app.screen, K8sClusterConfigScreen)

        ip_cp_input = self._app.query_exactly_one("#ip_cp_input")
        ip_cp_input.value = str(control_plane_ip)

        ip1_input = self._app.query_exactly_one("#ip1_input")
        ip1_input.value = str(worked_node_1_ip)

        ip2_input = self._app.query_exactly_one("#ip2_input")
        ip2_input.value = str(worked_node_2_ip)

        ip3_input = self._app.query_exactly_one("#ip3_input")
        ip3_input.value = str(worked_node_3_ip)

        await self._pilot.pause()
        await self.submit()

    async def fill_k8s_load_balancer_config_screen(
        self,
        control_plane_domain: str,
        ingress_load_balancer_node_ip: IPv4Address,
        ingress_load_balancer_domain: str,
        load_balancer_public_key_path: str | Path,
        load_balancer_private_key_path: str | Path,
    ) -> None:
        assert isinstance(self._app.screen, K8sLoadBalancerConfigScreen)

        control_plane_lb_domain_input = self._app.query_exactly_one(
            "#control_plane_lb_domain_input"
        )
        control_plane_lb_domain_input.value = control_plane_domain

        ip_lb_ingress_ip_input = self._app.query_exactly_one("#ip_lb_ingress_ip_input")
        ip_lb_ingress_ip_input.value = str(ingress_load_balancer_node_ip)

        lb_ingress_domain_input = self._app.query_exactly_one(
            "#lb_ingress_domain_input"
        )
        lb_ingress_domain_input.value = ingress_load_balancer_domain

        lb_public_key_path_input = self._app.query_exactly_one(
            "#lb_public_key_path_input"
        )
        lb_public_key_path_input.value = str(load_balancer_public_key_path)

        lb_private_key_path_input = self._app.query_exactly_one(
            "#lb_private_key_path_input"
        )
        lb_private_key_path_input.value = str(load_balancer_private_key_path)

        await self._pilot.pause()
        await self.submit()

    async def fill_disk_config_screen(self) -> None:
        assert isinstance(self._app.screen, DiskConfigScreen)

        data_disk_operation_enabled = self._app.query_exactly_one("#operation-enabled")
        data_disk_operation_enabled.value = False
        data_disk_manually_encrypted = self._app.query_exactly_one(
            "#manually-encrypted"
        )
        data_disk_manually_encrypted.value = False
        await self._pilot.pause()
        await self.submit()

    async def fill_it_auth_config_screen(
        self,
        it_email_address: str,
        it_password: str,
    ) -> None:
        assert isinstance(self._app.screen, ITAuthConfigScreen)

        it_admin_email_input = self._app.query_exactly_one("#it_admin_email_input")
        it_admin_email_input.value = str(it_email_address)
        it_admin_password_input = self._app.query_exactly_one(
            "#it_admin_password_input"
        )
        it_admin_password_input.value = str(it_password)
        await self._pilot.pause()
        await self.submit()

    async def fill_clinical_auth_config_screen(
        self, clinical_email: str, clinical_password: str
    ) -> None:
        assert isinstance(self._app.screen, ClinicalAuthConfigScreen)

        clinical_email_input = self._app.query_exactly_one("#clinical_email_input")
        clinical_email_input.value = str(clinical_email)
        clinical_password_input = self._app.query_exactly_one(
            "#clinical_password_input"
        )
        clinical_password_input.value = str(clinical_password)
        await self._pilot.pause()
        await self.submit()

    async def fill_sdc_config_screen(
        self,
        sdc_key_path: str | Path,
        sdc_crt_path: str | Path,
        sdc_intermediate_cert_path: str | Path,
        sdc_certificate_pass: str,
    ) -> None:
        assert isinstance(self._app.screen, SDCConfigScreen)

        sdc_key_path_input = self._app.query_exactly_one("#sdc_key_path_input")
        sdc_key_path_input.value = str(sdc_key_path)
        sdc_certificate_path_input = self._app.query_exactly_one(
            "#sdc_certificate_path_input"
        )
        sdc_certificate_path_input.value = str(sdc_crt_path)
        sdc_intermediate_certificate_path_input = self._app.query_exactly_one(
            "#sdc_intermediate_certificate_path_input"
        )
        sdc_intermediate_certificate_path_input.value = str(sdc_intermediate_cert_path)
        sdc_certificate_password_input = self._app.query_exactly_one(
            "#sdc_certificate_password_input"
        )
        sdc_certificate_password_input.value = str(sdc_certificate_pass)
        await self._pilot.pause()
        await self.submit()

    async def fill_confirmation_screen(self) -> None:
        assert isinstance(self._app.screen, ConfirmationScreen)
        await self._pilot.pause()
        await self.submit()


@pytest.mark.asyncio
async def test_installation_flow_basic():
    app = CmsInstaller()
    async with app.run_test() as pilot:
        await pilot.pause()

        installer_user = CmsInstallerUserAgent(app, pilot)
        await installer_user.fill_welcome_screen()

        await installer_user.fill_docker_image_selection_screen()

        await installer_user.fill_ssh_config_screen(
            config.SSH_CONFIG_USERNAME,
            config.SSH_PRIVATE_KEY_PATH,
        )

        await installer_user.fill_k8s_cluster_config_screen(
            config.CONTROL_PLANE_NODE_IP,
            config.WORKER_NODE_1_PUBLIC_IP,
            config.WORKER_NODE_2_PUBLIC_IP,
            config.WORKER_NODE_3_PUBLIC_IP,
        )

        await installer_user.fill_k8s_load_balancer_config_screen(
            config.CONTROL_PLANE_DOMAIN,
            config.INGRESS_NODE_IP,
            config.LOAD_BALANCER_INGRESS_DOMAIN,
            config.LB_PUBLIC_KEY,
            config.LB_PRIVATE_KEY,
        )

        await installer_user.fill_disk_config_screen()

        await installer_user.fill_it_auth_config_screen(
            config.IT_ADMIN_EMAIL,
            config.IT_ADMIN_PASSWORD,
        )

        await installer_user.fill_clinical_auth_config_screen(
            config.CLINICAL_ADMIN_EMAIL,
            config.CLINICAL_ADMIN_PASSWORD,
        )

        await installer_user.fill_sdc_config_screen(
            config.SDC_KEY_PATH,
            config.SDC_CERTIFICATE_PATH,
            config.SDC_INTERMEDIATE_CERTIFICATE_PATH,
            config.SDC_CERTIFICATE_PASSWORD,
        )

        await installer_user.fill_confirmation_screen()

        assert isinstance(app.screen, CommandLogScreen)

        screen: CommandLogScreen = app.screen
        while not screen.finished:
            await asyncio.sleep(5)
        for line in app.query_exactly_one("#log_area").lines:
            logger.info(line)
        await pilot.pause()

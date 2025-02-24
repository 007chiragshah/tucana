import asyncio
import os
import shutil
import stat
from asyncio.subprocess import Process
from datetime import datetime

from textual.widgets import Log

from app.models import Database

INSTALLATION_FOLDER_NAME = "cms_installer_data"
SSH_CERTIFICATE_FOLDER_NAME = "sdc_certificates"
LB_CERTIFICATE_FOLDER_NAME = "lb_certificates"
LOGS_FOLDER_NAME = "logs"


def write_to_file_sync(filename, file_path, data):
    file_location = os.path.join(file_path, filename)
    with open(file_location, "a") as file:
        file.write(f"{data}\n")


async def write_to_file_async(filename, file_path, data):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, write_to_file_sync, filename, file_path, data)


async def manage_docker_process_logs(
    process: Process, log_area: Log, root_folder: str
) -> None:
    log_file_name = generate_log_file_name()
    log_path = os.path.join(root_folder, LOGS_FOLDER_NAME)

    async for line in process.stdout:
        text = line.decode("utf-8").strip()
        log_area.write_line(text)
        await write_to_file_async(filename=log_file_name, file_path=log_path, data=text)
        await asyncio.sleep(0)

    async for line in process.stderr:
        text = line.decode("utf-8").strip()
        log_area.write_line(f"[ERROR] {text}")
        await write_to_file_async(filename=log_file_name, file_path=log_path, data=text)
        await asyncio.sleep(0)


def generate_folder_structure() -> str:
    installation_path = os.path.join(os.getcwd(), INSTALLATION_FOLDER_NAME)
    os.makedirs(installation_path, mode=0o777, exist_ok=True)

    logs_path = os.path.join(installation_path, LOGS_FOLDER_NAME)
    os.makedirs(logs_path, mode=0o777, exist_ok=True)

    ssh_certificate_files_path = os.path.join(
        installation_path, SSH_CERTIFICATE_FOLDER_NAME
    )
    os.makedirs(ssh_certificate_files_path, mode=0o700, exist_ok=True)

    lb_certificate_files_path = os.path.join(
        installation_path, LB_CERTIFICATE_FOLDER_NAME
    )
    os.makedirs(lb_certificate_files_path, mode=0o700, exist_ok=True)

    return installation_path


def generate_installation_env_file(db_info: Database, root_folder: str):
    file_name = ".env"
    file_location = os.path.join(root_folder, file_name)
    installer_variables = {
        "SSH_USER": db_info.installation_data.ssh_config.ssh_username,
        "PRIVATE_KEY_NAME": os.path.join(
            SSH_CERTIFICATE_FOLDER_NAME,
            db_info.installation_data.ssh_config.private_key_path.name,
        ),
        "K8S_CLUSTER_CONTROL_HOSTS": "1",
        "K8S_CLUSTER_IPS": f"{db_info.installation_data.k8s_cluster_config.ip_cp} {db_info.installation_data.k8s_cluster_config.ip1} {db_info.installation_data.k8s_cluster_config.ip2} {db_info.installation_data.k8s_cluster_config.ip3}",
        "LB_K8S_API_FQDN": db_info.installation_data.k8s_lb_config.lb_domain,
        "LB_INGRESS_IP": db_info.installation_data.k8s_lb_config.lb_ingress_ip,
        "LB_INGRESS_DOMAIN": db_info.installation_data.k8s_lb_config.lb_ingress_domain,
        "LB_INGRESS_CERT_PUBLIC_KEY": os.path.join(
            LB_CERTIFICATE_FOLDER_NAME,
            db_info.installation_data.k8s_lb_config.lb_public_key.name,
        ),
        "LB_INGRESS_CERT_PRIVATE_KEY": os.path.join(
            LB_CERTIFICATE_FOLDER_NAME,
            db_info.installation_data.k8s_lb_config.lb_private_key.name,
        ),
        "SDC_CERT_PASSWORD": db_info.installation_data.sdc_config.certificate_password,
        "CLINICAL_USER_EMAIL": db_info.installation_data.clinical_auth_config.email,
        "CLINICAL_USER_PASSWORD": db_info.installation_data.clinical_auth_config.password,
        "TECHICAL_USER_EMAIL": db_info.installation_data.it_auth_config.email,
        "TECHNICAL_USER_PASSWORD": db_info.installation_data.it_auth_config.password,
        "DATA_DISK_OPERATIONS_ENABLED": db_info.installation_data.disk_config.data_disk_operations_enabled,
        "DATA_DISK_DEVICE_NAME": db_info.installation_data.disk_config.data_disk_device_name,
        "DATA_DISK_MANUAL_ENCRYPTION": db_info.installation_data.disk_config.data_disk_manually_encrypted,
        "DATA_DISK_ENCRYPRTION_KEYFILE": db_info.installation_data.disk_config.data_disk_encryption_key,
        "HOSPITAL_TZ": "UTC",
        "SERVICE_MESH_ENABLED": "true",
        "MONITORING_ENABLED": "true",
    }

    with open(file_location, "w") as file:
        for key, value in installer_variables.items():
            file.write(f"{key}={value}\n")


def copy_installation_files(db_info: Database, root_folder):
    ssh_certificate_files_path = os.path.join(root_folder, SSH_CERTIFICATE_FOLDER_NAME)
    lb_certificate_files_path = os.path.join(root_folder, LB_CERTIFICATE_FOLDER_NAME)

    files_to_copy_in_root = (
        db_info.installation_data.sdc_config.key_path,
        db_info.installation_data.sdc_config.certificate_path,
        db_info.installation_data.sdc_config.intermediate_certificate_path,
    )

    ssh_files_to_copy = (db_info.installation_data.ssh_config.private_key_path,)

    lb_files_to_copy = (
        db_info.installation_data.k8s_lb_config.lb_public_key,
        db_info.installation_data.k8s_lb_config.lb_private_key,
    )

    for file in files_to_copy_in_root:
        destination = shutil.copy(file, root_folder)
        os.chmod(destination, stat.S_IRUSR | stat.S_IWUSR)

    for file in ssh_files_to_copy:
        destination = shutil.copy(file, ssh_certificate_files_path)
        os.chmod(destination, stat.S_IRUSR | stat.S_IWUSR)

    for file in lb_files_to_copy:
        destination = shutil.copy(file, lb_certificate_files_path)
        os.chmod(destination, stat.S_IRUSR | stat.S_IWUSR)


def generate_log_file_name() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"log_{timestamp}.log"

    return log_file_name


async def run_docker_process(installation_folder: str, image_id: str) -> Process:
    docker_command = f"docker run -i --rm  -v {installation_folder}:/tmp {image_id} task 20-install-all-offline"

    process = await asyncio.create_subprocess_shell(
        docker_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    return process

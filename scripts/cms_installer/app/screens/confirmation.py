from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Header, MarkdownViewer

from app.models import db
from app.screens.installation import CommandLogScreen


class ConfirmationScreen(Screen):
    TITLE = "Confirmation"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db

        self.installation_data_markdown = f"""\

## Docker Image

- Version: 
    ```
    {self.db.installation_data.docker_image_config.version}
    ```

- Image ID:
    ```
    {self.db.installation_data.docker_image_config.image_id}
    ```

## SSH Config

- Username: 
    ```
    {self.db.installation_data.ssh_config.ssh_username}
    ```

- Private key path:
    ```
    {self.db.installation_data.ssh_config.private_key_path}
    ```

## K8s Cluster Config

| Node            | IP                                                      |
| --------------- | ------------------------------------------------------- |
| `Control Plane` | `{self.db.installation_data.k8s_cluster_config.ip_cp}`  |
| `Node 1`        | `{self.db.installation_data.k8s_cluster_config.ip1}`    |
| `Node 2`        | `{self.db.installation_data.k8s_cluster_config.ip2}`    |
| `Node 3`        | `{self.db.installation_data.k8s_cluster_config.ip3}`    |

## K8s Load Balancer

- Control Plane Load Balancer: 
    ```
    {self.db.installation_data.k8s_lb_config.lb_domain}
    ```
       
- Load balancer ingress IP: 
    ```
    {self.db.installation_data.k8s_lb_config.lb_ingress_ip}
    ```
    
- Load balancer ingress domain: 
    ```
    {self.db.installation_data.k8s_lb_config.lb_ingress_domain}
    ```
    
- Load Balancer domain public key: 
    ```
    {self.db.installation_data.k8s_lb_config.lb_public_key}
    ```

- Load Balancer domain private key: 
    ```
    {self.db.installation_data.k8s_lb_config.lb_private_key}
    ```

## Disk Config

{"✅ " if self.db.installation_data.disk_config.data_disk_operations_enabled else "❌ "} Data disk operations enabled 
- Disk name:
    ```
    {self.db.installation_data.disk_config.data_disk_device_name}
    ```
    
{"✅ " if self.db.installation_data.disk_config.data_disk_manually_encrypted else "❌ "} Data disk manually encrypted
- Encryption key file path: 
    ```
    {self.db.installation_data.disk_config.data_disk_encryption_key}
    ```

## Auth IT Admin

- IT Admin Email
    ```
    {self.db.installation_data.it_auth_config.email}
    ```
    
- IT Admin Password
    ```
    {self.db.installation_data.it_auth_config.password}
    ```

## Auth Clinical User

- Clinical Email
    ```
    {self.db.installation_data.clinical_auth_config.email}
    ```
    
- Clinical Password
    ```
    {self.db.installation_data.clinical_auth_config.password}
    ```
    
## SDC Config
- SDC key path:
    ``` 
    {self.db.installation_data.sdc_config.key_path}
    ```
    
- SDC certificate path:
    ``` 
    {self.db.installation_data.sdc_config.certificate_path}
    ```

- SDC intermediate certificate path:
    ``` 
    {self.db.installation_data.sdc_config.intermediate_certificate_path}
    ```


- SDC certificate password:
    ```
    {self.db.installation_data.sdc_config.certificate_password}
    ```
    
"""

    def compose(self) -> ComposeResult:
        yield Header(id="header")

        yield MarkdownViewer(
            self.installation_data_markdown, show_table_of_contents=False
        )

        with Container(id="buttons-zone"):
            yield Button("Back", id="back-button")
            yield Button("Install", id="next-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.app.push_screen(CommandLogScreen())

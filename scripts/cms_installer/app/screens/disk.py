from pydantic import ValidationError
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.validation import Length, Function
from textual.widgets import Button, Input, Static, Header, Label, Checkbox

from textual.containers import Container, VerticalScroll

from app.models import DiskConfigContext, db
from app.validations import NodePathField
from app.screens.auth_admin import ITAuthConfigScreen

DISK_OPERATION_ENABLED_TEXT = """\
If the data disk should be encrypted during the installation process.
"""

DISK_DEVICE_NAME_TEXT = """\
It defines the name of the data disk to be used for the Central Hub data storage.
"""

DISK_MANUALLY_ENCRYPTED_TEXT = """\
It defines if the data disk should be encrypted during the installation process or it has been done manually.
"""

DISK_ENCRYPTION_KEYFILE_TEXT = """\
It defines the path to the keyfile to be used for the data disk encryption.
If the disk already encrypted following the provided documentation, this variable should be set to the path of the keyfile. Otherwise, the keyfile will be generated during the installation process and the path should be set to the desired location. The path should exists on the node, for example if the variable value is set to "/path/to/keyfile", the path "/path/to/" should exist on the node.
"""


class DiskConfigScreen(Screen):
    TITLE = "Disk Config"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db
        self.data_disk_operation_enabled = Checkbox(
            "Data disk operations enabled", True, id="operation-enabled"
        )
        self.data_disk_device_name_input = self.control_plane_lb_domain_input = Input(
            placeholder="Disk name, eg: sda1",
            validators=[
                Length(
                    minimum=1, maximum=None, failure_description="Invalid disk name."
                )
            ],
        )
        self.data_disk_manually_encrypted = Checkbox(
            "Data disk manually encrypted", True, id="manually-encrypted"
        )
        self.data_disk_encryption_key_file_input = Input(
            placeholder="Encryption key path, eg: /path/to/keyfile",
            validators=[
                Function(
                    NodePathField.from_input,
                    "Invalid path.",
                ),
            ],
        )
        self.submit_msg = Static("", id="submit_message", classes="submit_err_msg")

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="sidebar"):
            yield Label("Data disk operations enabled")
            yield Static(DISK_OPERATION_ENABLED_TEXT)
            yield Label("Data disk device name")
            yield Static(DISK_DEVICE_NAME_TEXT)
            yield Label("Data disk manually encrypted")
            yield Static(DISK_MANUALLY_ENCRYPTED_TEXT)
            yield Label("Data disk manually encryption key file")
            yield Static(DISK_ENCRYPTION_KEYFILE_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with VerticalScroll(id="main-zone"):
                yield self.data_disk_operation_enabled
                yield Label("Data disk device name", id="device-name-label")
                yield self.data_disk_device_name_input

                yield self.data_disk_manually_encrypted
                yield Label(
                    "Data disk manually encryption key file", id="key-file-label"
                )
                yield self.data_disk_encryption_key_file_input

            with Container(id="error-msg-zone"):
                yield self.submit_msg

            with Container(id="buttons-zone"):
                yield Button("Back", id="back-button")
                yield Button("Next", id="next-button")

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        self.submit_msg.update("")

    def validate_data(self):
        try:
            data = DiskConfigContext(
                data_disk_operations_enabled=self.data_disk_operation_enabled.value,
                data_disk_device_name=self.data_disk_device_name_input.value,
                data_disk_manually_encrypted=self.data_disk_manually_encrypted.value,
                data_disk_encryption_key=self.data_disk_encryption_key_file_input.value,
            )
            self.db.installation_data.disk_config = data

            self.submit_msg.update("")
            self.app.push_screen(ITAuthConfigScreen())
        except ValidationError:
            self.submit_msg.update(
                "Make sure the disk name is correct, and if it is manually encrypted, the path to the key file is valid."
            )

    def handle_data_disk_operation_enabled(self, value: bool) -> None:
        self.data_disk_device_name_input.disabled = not value
        label = self.query_one("#device-name-label", Label)
        label.toggle_class("text-disabled")

        self.data_disk_manually_encrypted.value = value
        self.data_disk_manually_encrypted.disabled = not value

    def handle_data_disk_manually_encrypted(self, value: bool) -> None:
        self.data_disk_encryption_key_file_input.disabled = not value
        label = self.query_one("#key-file-label", Label)
        label.toggle_class("text-disabled")

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        if event.checkbox.id == "operation-enabled":
            self.handle_data_disk_operation_enabled(event.value)

        if event.checkbox.id == "manually-encrypted":
            self.handle_data_disk_manually_encrypted(event.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.validate_data()

from pydantic import ValidationError
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input, Static, Label, Header
from textual.containers import Container, VerticalScroll

from app.models import SSHConfigContext, db
from app.validations import FilePathField, UnixNameField
from app.screens.k8s_nodes import K8sClusterConfigScreen

from textual.validation import Function
from textual import on


PRIVATE_KEY_PATH_TEXT = """\
This variable defines a name of the SSH private key to be used for the connection to various components' nodes during the install process. Should be a private key.
"""
USERNAME_TEXT = """\
This variable defines which is the SSH user to be used for the connection to various components' nodes during the install process.
"""


class SSHConfigScreen(Screen):
    TITLE = "SSH Config"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db
        self.ssh_user_input = Input(
            id="ssh_user_input",
            placeholder="SSH username, eg: ubuntu",
            validators=[
                Function(UnixNameField.from_input, "Invalid unix username."),
            ],
        )
        self.private_key_path = Input(
            id="private_key_path_input",
            placeholder="Key path, eg: ./key-folder/private.pem",
            validators=[
                Function(
                    FilePathField.from_input,
                    "Path does not point to a private key file.",
                ),
            ],
        )
        self.submit_msg = Static("", id="submit_message", classes="submit_err_msg")

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="sidebar"):
            yield Label("Username")
            yield Static(USERNAME_TEXT)
            yield Label("Private Key")
            yield Static(PRIVATE_KEY_PATH_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with VerticalScroll(id="main-zone"):
                yield Label("Username")
                yield self.ssh_user_input

                yield Label("Private Key Path")
                yield self.private_key_path

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
            data = SSHConfigContext(
                ssh_username=self.ssh_user_input.value,
                private_key_path=self.private_key_path.value,
            )
            self.db.installation_data.ssh_config = data

            self.submit_msg.update("")
            self.app.push_screen(K8sClusterConfigScreen())
        except ValidationError:
            self.submit_msg.update("Ensure you enter a valid username and private key.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.validate_data()

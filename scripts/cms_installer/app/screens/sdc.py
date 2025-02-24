from pydantic import ValidationError
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.validation import Length, Function
from textual.widgets import Button, Input, Static, Label, Header
from textual.containers import Container, VerticalScroll

from app.models import db, SDCConfigContext
from app.validations import (
    check_sdc_key_path,
    check_sdc_certificate_path,
    check_sdc_intermediate_certificate_path,
)
from app.screens.confirmation import ConfirmationScreen

SDC_CERTIFICATE_PATH_TEXT = """\
Path to SDC certificates. Certificates should include:
\n - consumerLeaf1.key
\n - consumerLeaf1.crt
\n - intermediateCA.crt
"""

SDC_CERTIFICATE_PASS_TEXT = """\
The encryption password for the SDC certificates.
"""


class SDCConfigScreen(Screen):
    TITLE = "SDC Config"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db
        self.sdc_key_path_input = Input(
            id="sdc_key_path_input",
            placeholder="path/to/consumerLeaf1.key",
            validators=[
                Function(check_sdc_key_path, "File must be named 'consumerLeaf1.key'.")
            ],
        )
        self.sdc_certificate_path_input = Input(
            id="sdc_certificate_path_input",
            placeholder="path/to/consumerLeaf1.crt",
            validators=[
                Function(
                    check_sdc_certificate_path,
                    "File must be named 'consumerLeaf1.crt'.",
                )
            ],
        )
        self.sdc_intermediate_certificate_path_input = Input(
            id="sdc_intermediate_certificate_path_input",
            placeholder="path/to/intermediateCA.crt",
            validators=[
                Function(
                    check_sdc_intermediate_certificate_path,
                    "File must be named 'intermediateCA.crt'.",
                )
            ],
        )
        self.sdc_certificate_password_input = Input(
            id="sdc_certificate_password_input",
            placeholder="Password",
            validators=[
                Length(
                    minimum=1, maximum=None, failure_description="Password too short."
                )
            ],
        )
        self.submit_msg = Static("", id="submit_message", classes="submit_err_msg")

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="sidebar"):
            yield Label("SDC certificate paths")
            yield Static(SDC_CERTIFICATE_PATH_TEXT)
            yield Label("SDC certificate password")
            yield Static(SDC_CERTIFICATE_PASS_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with VerticalScroll(id="main-zone"):
                yield Label("SDC key")
                yield self.sdc_key_path_input

                yield Label("SDC certificate")
                yield self.sdc_certificate_path_input

                yield Label("SDC intermediate certificate")
                yield self.sdc_intermediate_certificate_path_input

                yield Label("SDC certificate password")
                yield self.sdc_certificate_password_input

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
            data = SDCConfigContext(
                key_path=self.sdc_key_path_input.value,
                certificate_path=self.sdc_certificate_path_input.value,
                intermediate_certificate_path=self.sdc_intermediate_certificate_path_input.value,
                certificate_password=self.sdc_certificate_password_input.value,
            )
            self.db.installation_data.sdc_config = data

            self.submit_msg.update("")
            self.app.push_screen(ConfirmationScreen())
        except ValidationError:
            self.submit_msg.update(
                "Ensure you provide valid consumerLeaf1.key, consumerLeaf1.crt, and intermediateCA.crt files, "
                "and verify that the certificate password is correct."
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.validate_data()

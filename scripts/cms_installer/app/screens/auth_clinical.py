from pydantic import ValidationError
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.validation import Function, Length
from textual.widgets import Button, Input, Static, Label, Header
from textual.containers import Container, VerticalScroll

from app.models import db, ClinicalAuthContext
from app.validations import EmailStringField
from app.screens.sdc import SDCConfigScreen

CLINICAL_EMAIL_TEXT = """\
The email used to access Central Hub as a clinical user.
"""

CLINICAL_PASSWORD_TEXT = """\
The password used to access Central Hub as a clinical user.
"""


class ClinicalAuthConfigScreen(Screen):
    TITLE = "Clinical Authorization"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db
        self.clinical_email_input = Input(
            id="clinical_email_input",
            placeholder="Clinical email, eg: clinical@sibelhealth.com",
            validators=[
                Function(EmailStringField.from_input, "Invalid email."),
            ],
        )
        self.clinical_password_input = Input(
            id="clinical_password_input",
            placeholder="Password",
            validators=[
                Length(
                    minimum=4, maximum=None, failure_description="Password too short."
                )
            ],
        )
        self.submit_msg = Static("", id="submit_message", classes="submit_err_msg")

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="sidebar"):
            yield Label("Clinical Email")
            yield Static(CLINICAL_EMAIL_TEXT)
            yield Label("Clinical Password")
            yield Static(CLINICAL_PASSWORD_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with VerticalScroll(id="main-zone"):
                yield Label("Clinical Email")
                yield self.clinical_email_input

                yield Label("Clinical Password")
                yield self.clinical_password_input

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
            data = ClinicalAuthContext(
                email=self.clinical_email_input.value,
                password=self.clinical_password_input.value,
            )
            self.db.installation_data.clinical_auth_config = data

            self.submit_msg.update("")
            self.app.push_screen(SDCConfigScreen())
        except ValidationError:
            self.submit_msg.update(
                "Invalid email or password.\n" "Password must have 4 characters."
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.validate_data()

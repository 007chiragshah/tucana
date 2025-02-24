from pydantic import ValidationError
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.validation import Function, Length
from textual.widgets import Button, Input, Static, Label, Header
from textual.containers import Container, VerticalScroll

from app.models import db, ITAuthContext
from app.validations import EmailStringField
from app.screens.auth_clinical import ClinicalAuthConfigScreen

IT_ADMIN_EMAIL_TEXT = """\
The email used to access Central Hub as an IT admin.
"""

IT_ADMIN_PASSWORD_TEXT = """\
The password used to access Central Hub as IT admin. 
"""


class ITAuthConfigScreen(Screen):
    TITLE = "IT Authorization"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db
        self.it_admin_email_input = Input(
            id="it_admin_email_input",
            placeholder="IT admin email, eg: admin@sibelhealth.com",
            validators=[
                Function(EmailStringField.from_input, "Invalid email."),
            ],
        )
        self.it_admin_password_input = Input(
            id="it_admin_password_input",
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
            yield Label("IT Admin Email")
            yield Static(IT_ADMIN_EMAIL_TEXT)
            yield Label("IT Admin Password")
            yield Static(IT_ADMIN_PASSWORD_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with VerticalScroll(id="main-zone"):
                yield Label("IT Admin Email")
                yield self.it_admin_email_input

                yield Label("IT Admin Password")
                yield self.it_admin_password_input

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
            data = ITAuthContext(
                email=self.it_admin_email_input.value,
                password=self.it_admin_password_input.value,
            )
            self.db.installation_data.it_auth_config = data

            self.submit_msg.update("")
            self.app.push_screen(ClinicalAuthConfigScreen())
        except ValidationError:
            self.submit_msg.update(
                "Invalid email or password.\n" "Password must have 4 characters."
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.app.pop_screen()

        if event.button.id == "next-button":
            self.validate_data()

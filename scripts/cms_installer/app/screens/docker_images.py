from pydantic import ValidationError
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static, Label, Header, RadioSet, RadioButton
from textual.containers import Container, VerticalScroll, ScrollableContainer

from app.installer import get_installer_images, get_installer_images_names
from app.models import db, DockerImageContext
from app.screens.ssh import SSHConfigScreen
from docker.errors import DockerException

DOCKER_IMAGE_TEXT = """\
To install the Central Server, it is necessary to download the desired version of the Docker installer image and have the Docker engine running.
"""


class DockerImageSelectionScreen(Screen):
    TITLE = "Installer Image"
    CSS_PATH = "../styles/common.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = db

        self.images_set = RadioSet(id="images-set")
        self.submit_msg = Static("", id="submit_message", classes="submit_err_msg")

        try:
            self.image_mapping = dict(
                zip(get_installer_images_names(), get_installer_images())
            )
        except DockerException:
            self.image_mapping = {}

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="sidebar"):
            yield Label("Available Docker Images")
            yield Static(DOCKER_IMAGE_TEXT)

        yield Header(id="header")

        with Container(id="app-grid"):
            with ScrollableContainer(id="main-zone"):
                with self.images_set:
                    images_names = self.image_mapping.keys()
                    for img_name in images_names:
                        yield RadioButton(img_name)

            with Container(id="error-msg-zone"):
                yield self.submit_msg

            with Container(id="buttons-zone"):
                yield Button("Next", id="next-button", disabled=True)

        if not images_names:
            self.images_set.visible = False
            self.submit_msg.update(
                "Docker is not running or there are not available images to install."
            )

    @on(RadioSet.Changed)
    def set_img_value(self, event: RadioSet.Changed) -> None:
        self.query_one("#next-button", Button).disabled = False

    def validate_data(self):
        try:
            img_name = str(self.images_set.pressed_button.label)
            img_id = self.image_mapping.get(img_name).id

            data = DockerImageContext(
                version=img_name,
                image_id=img_id,
            )
            self.db.installation_data.docker_image_config = data

            self.submit_msg.update("")
            self.app.push_screen(SSHConfigScreen())
        except ValidationError:
            self.submit_msg.update(
                "There is a problem with the selected docker image. Please try again."
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "next-button":
            self.validate_data()

from datetime import datetime

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label
from textual.containers import Center, Container
from app.screens.docker_images import DockerImageSelectionScreen
from app.version import SIBEL_VERSION


class WelcomeScreen(Screen):
    CSS_PATH = "../styles/welcome.tcss"

    def compose(self) -> ComposeResult:
        yield Container(
            Center(
                Label(
                    "Welcome to Central Server installer \n The Installer will guide you through the installation process.",
                    classes="welcome-message",
                ),
                Label("Please press any key to continue.", id="click-instruction"),
            ),
            id="content-container",
        )

        yield Label(
            f"© {datetime.now().year} Sibel Health, Inc",
            classes="centered-footer",
            id="copyright-label",
        )
        yield Label(SIBEL_VERSION, classes="centered-footer")

    def on_key(self, event) -> None:
        self.app.push_screen(DockerImageSelectionScreen())

    def on_click(self, event) -> None:
        self.app.push_screen(DockerImageSelectionScreen())

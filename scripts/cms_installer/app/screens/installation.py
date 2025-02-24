import asyncio

from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Header, Button, Log

from app.installer_tools import (
    generate_folder_structure,
    generate_installation_env_file,
    copy_installation_files,
    run_docker_process,
    manage_docker_process_logs,
)
from app.models import db
from app.screens.quit import QuitScreen


class CommandLogScreen(Screen):
    TITLE = "Running Installation"
    CSS_PATH = ["../styles/common.tcss", "../styles/installation.tcss"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db
        self.log_area = Log(
            id="log_area",
            highlight=True,
            auto_scroll=True,
        )
        self.retry_button = Button("Retry", disabled=True, id="back-button")
        self.exit_button = Button("Exit", disabled=True, id="next-button")
        self.finished = False

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(id="app-grid"):
            with Container():
                yield self.log_area

            with Container(id="buttons-zone"):
                yield self.retry_button
                yield self.exit_button

    async def on_mount(self) -> None:
        self.log_area = self.query_one("#log_area", Log)
        asyncio.create_task(self.run_command())

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-button":
            self.retry_button.disabled = True
            self.exit_button.disabled = True
            self.log_area.clear()
            asyncio.create_task(self.run_command())

        if event.button.id == "next-button":
            await self.app.push_screen(QuitScreen())

    async def run_command(self) -> None:
        self.log_area.write("Running command...\n")

        try:
            installation_root_folder = generate_folder_structure()
            generate_installation_env_file(self.db, installation_root_folder)
            copy_installation_files(self.db, installation_root_folder)
            img_id = self.db.installation_data.docker_image_config.image_id

            docker_command = f"docker run -i --rm -v {installation_root_folder}:/tmp {img_id} task 20-install-all-offline \n"
            self.log_area.write(docker_command)

            process = await run_docker_process(installation_root_folder, img_id)
            await manage_docker_process_logs(
                process, self.log_area, installation_root_folder
            )
            await process.wait()

            if process.returncode != 0:
                self.retry_button.disabled = False

        except Exception as e:
            self.retry_button.disabled = False
            self.log_area.write(f"\n[ERROR] {str(e)}")

        finally:
            self.log_area.write("\n\nCommand finished.\n")
            self.exit_button.disabled = False
            self.finished = True

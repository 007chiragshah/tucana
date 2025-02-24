from textual.app import App

from app.screens.welcome import WelcomeScreen


class CmsInstaller(App):
    ENABLE_COMMAND_PALETTE = False

    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())


app = CmsInstaller()

if __name__ == "__main__":
    app.run()

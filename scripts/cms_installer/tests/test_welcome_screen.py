import pytest

from app.screens.docker_images import DockerImageSelectionScreen
from app.main import CmsInstaller


@pytest.mark.asyncio
async def test_press_a_key():
    app = CmsInstaller()
    async with app.run_test() as pilot:
        await pilot.press("return")
        await pilot.pause()

        assert isinstance(app.screen, DockerImageSelectionScreen)


@pytest.mark.asyncio
async def test_click_screen():
    app = CmsInstaller()
    async with app.run_test() as pilot:
        await pilot.click()
        await pilot.pause()

        assert isinstance(app.screen, DockerImageSelectionScreen)

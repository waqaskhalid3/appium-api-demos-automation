import pytest
from drivers.appium_driver import init_driver
from utils.helpers import take_screenshot, setup_logger

logger = setup_logger("test_01_launch")

@pytest.fixture(scope="function")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

def test_launch_app(driver):
    try:
        logger.info("Verifying app installation")
        assert driver.is_app_installed("io.appium.android.apis")
        logger.info("App is installed successfully.")
    except Exception as e:
        logger.error(f"Launch test failed: {e}")
        take_screenshot(driver, "test_launch_app")
        raise

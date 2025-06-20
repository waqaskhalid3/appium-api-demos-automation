from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import take_screenshot, setup_logger

logger = setup_logger("test_03_select_item")

def test_select_item(driver):
    try:
        logger.info("Navigating to People Names")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter").click()
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']").click()

        logger.info("Checking for 'Arnold'")
        arnold = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arnold']")
        assert arnold.is_displayed()
        logger.info("'Arnold' is displayed successfully.")
    except Exception as e:
        logger.error(f"Select item test failed: {e}")
        take_screenshot(driver, "test_select_item")
        raise

from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import take_screenshot, setup_logger

logger = setup_logger("test_02_product_list")

def test_product_list(driver):
    try:
        logger.info("Navigating to Expandable Lists > Custom Adapter")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter").click()

        logger.info("Verifying 'People Names' exists")
        assert driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")
        logger.info("'People Names' found successfully.")
    except Exception as e:
        logger.error(f"Product list test failed: {e}")
        take_screenshot(driver, "test_product_list")
        raise

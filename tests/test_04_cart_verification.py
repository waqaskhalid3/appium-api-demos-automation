from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import take_screenshot, setup_logger
import time

logger = setup_logger("test_04_cart_verification")

def test_cart_verification(driver):
    try:
        logger.info("Navigating to Views > Expandable Lists > Custom Adapter")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter").click()

        logger.info("Tapping 'People Names' to expand list")
        people_names = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")
        people_names.click()

        logger.info("Waiting for child items to appear")
        time.sleep(1)  # Allow UI to expand

        logger.info("Verifying that sub-item 'Arnold' is visible")
        arnold = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arnold']")
        assert arnold.is_displayed(), "'Arnold' sub-item is not displayed"
        logger.info("Sub-item 'Arnold' is visible. Cart verification passed.")

    except Exception as e:
        logger.error(f"Cart verification test failed: {e}")
        take_screenshot(driver, "test_cart_verification")
        raise

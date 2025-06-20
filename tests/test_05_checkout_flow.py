from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import take_screenshot, setup_logger

logger = setup_logger("test_05_checkout_flow")

def test_checkout_flow(driver):
    try:
        logger.info("Navigating to Controls > Light Theme")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Controls").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()

        logger.info("Filling out form")
        name = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
        name.send_keys("John Doe")

        checkbox = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1")
        checkbox.click()

        radio = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio1")
        radio.click()

        logger.info("Verifying form fields")
        assert name.text == "John Doe"
        assert checkbox.get_attribute("checked") == 'true'
        assert radio.get_attribute("checked") == 'true'
        logger.info("Checkout form filled and validated.")
    except Exception as e:
        logger.error(f"Checkout flow test failed: {e}")
        take_screenshot(driver, "test_checkout_flow")
        raise

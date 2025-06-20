from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import take_screenshot, setup_logger

logger = setup_logger("test_06_order_confirmation")

def test_order_confirmation(driver):
    try:
        logger.info("Re-opening Light Theme form for order confirmation")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Controls").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()

        logger.info("Validating form state post submission")
        name = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
        checkbox = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1")
        radio = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio1")

        assert name.text == "John Doe"
        assert checkbox.get_attribute("checked") == 'true'
        assert radio.get_attribute("checked") == 'true'
        logger.info("Order confirmed successfully with previous selections retained.")
    except Exception as e:
        logger.error(f"Order confirmation test failed: {e}")
        take_screenshot(driver, "test_order_confirmation")
        raise

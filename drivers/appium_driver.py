import os
from appium import webdriver

def init_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "app": os.path.expanduser("~/Downloads/android-apidemos/apks/ApiDemos-debug.apk"),
        "appWaitActivity": "*.*",
        "newCommandTimeout": 300,
        "autoGrantPermissions": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    return driver

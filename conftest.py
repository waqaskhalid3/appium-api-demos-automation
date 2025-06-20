import pytest
from drivers.appium_driver import init_driver 

@pytest.fixture(scope="function")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()
    
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'API Demos Appium Tests'
        config._metadata['Tester'] = 'Waqas'

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Appium UI Test Report"
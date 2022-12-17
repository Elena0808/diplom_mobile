import os
import allure
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser

from utils import attach


@pytest.fixture(scope='function', autouse=False)
def driver_management_local():
    load_dotenv()
    option = UiAutomator2Options().load_capabilities({
        "app": os.getenv('APP_LOCAL')
    })
    browser.config.timeout = float(os.getenv('selene.timeout', '20'))

    with allure.step('set up app session'):
        browser.config.driver = webdriver.Remote(
            os.getenv('REMOTE_URL'), options=option
        )

    yield
    attach.add_video(browser)
    attach.add_screenshot(browser)
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def driver_management_remote():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        "app": os.getenv('appRemote'),
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "locale": "RU",
        "language": "rus",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": os.getenv('userName'),
            "accessKey": os.getenv('accessKey')
        }
    })
    browser.config.timeout = float(os.getenv('selene.timeout', '20'))
    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub", options=options)

    yield
    attach.add_video(browser)
    browser.quit()

from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_manager():

    browser.config.window_width = 1680
    browser.config.window_height = 1050
    browser.config.timeout = 2
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
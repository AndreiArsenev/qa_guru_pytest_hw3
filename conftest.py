from selene import browser
import pytest

@pytest.fixture(autouse=True)
def browser_size():
    browser.config.window_height = 1024
    browser.config.window_width = 2000
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()
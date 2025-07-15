import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.window_height = 1024
    browser.config.window_width = 768
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()


def test_success():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene'))
    print("Тест завершен!")


def test_not_success():
    browser.element('[name="q"]').should(be.blank).type('Енггнйцегунеiuyewiuqwye').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))
    print('не найдено')

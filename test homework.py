from selene import browser, be, have


def test_success():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene'))
    print("Тест завершен!")


def test_not_success():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('Енггнйцегунеiuyewiuqwye').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))
    print('Тест завершен, ничего не найдено')

from selene import browser, have

def test_google_search():
    browser.open('https://google.com ')
    browser.element('[name=q]').type('selene python').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
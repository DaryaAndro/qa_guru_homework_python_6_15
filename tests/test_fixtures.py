import pytest
from selene import browser, have

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(scope='function', autouse=False, params=[(1366, 768), (1680, 1050), (1920, 1080)],
                ids=['1366 * 768', '1680 * 1050', '1920 * 1080'])
def desktop_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=False, params=[(360, 740), (390, 844), (768, 1024)],
                ids=['360 * 740', '390 * 844', '768 * 1024'])
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))

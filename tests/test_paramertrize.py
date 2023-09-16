import pytest
from selene import browser, have

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(params=[(1366, 768), (1680, 1050), (1920, 1080), (360, 740), (390, 844), (768, 1024)])
def browser_manager(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.mark.parametrize('browser_manager', [(1366, 768), (1680, 1050), (1920, 1080)],
                         ids=['1366 * 768', '1680 * 1050', '1920 * 1080'], indirect=True)
def test_github_desktop(browser_manager):
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_manager', [(360, 740), (390, 844), (768, 1024)],
                         ids=['360 * 740', '390 * 844', '768 * 1024'], indirect=True)
def test_github_mobile(browser_manager):
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))

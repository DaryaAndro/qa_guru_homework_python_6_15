import pytest
from selene import browser, have

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


def mobile(width):
    return width < 995


@pytest.fixture(
    scope='function',
    autouse=True,
    params=[(1366, 768), (1680, 1050), (1920, 1080), (360, 740), (390, 844), (768, 1024)],
    ids=['1366 * 768', '1680 * 1050', '1920 * 1080', '360 * 740', '390 * 844', '768 * 1024']
)
def browser_manager(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop():
    if mobile(browser.config.window_width):
        pytest.skip('Тест только для десктопа')
    browser.open('/')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile():
    if not mobile(browser.config.window_width):
        pytest.skip('Тест только для мобильных устройств')
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))

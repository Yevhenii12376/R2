import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def new_page(browser):
    page = browser.new_page()
    yield page
    page.close()

def navigate_to_login_page(page):
    page.goto("https://mystat.itstep.org/ua/auth/login/index?returnUrl=%2Fua%2Fmain%2Fdashboard%2Fpage%2Findex")

def test_open_website(new_page):
    page = new_page
    navigate_to_login_page(page)
    page.wait_for_selector(".col-3.align-self-center.custom-form .login-logo")
    assert page.is_visible(".col-3.align-self-center.custom-form .login-logo"), "Website is not open"

def test_login_and_check_user_login(browser, new_page):
    page = new_page
    navigate_to_login_page(page)
    page.get_by_placeholder("Логін").click()
    page.get_by_placeholder("Логін").fill("Xonen_go75")
    page.get_by_placeholder("Логін").press("Tab")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("H66QZ4e1")
    page.get_by_role("button", name="Вхід").click()
    page.wait_for_load_state('load', timeout=20000)
    logout_selector = '.pos-f-t .right-block .img-logout-block'
    page.locator(logout_selector).click()
    page.wait_for_load_state('load', timeout=20000)
    browser.close()

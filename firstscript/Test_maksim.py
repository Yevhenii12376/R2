
from playwright.sync_api import Playwright


def test_web(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mystat.itstep.org/ru/auth/login/index?returnUrl=%2Fru%2Fmain%2Fdashboard%2Fpage%2Findex")
    page.wait_for_selector('[src="/assets/images/logo.png?v=cce222be7d237f6d95418ecb8c5529b8"]')
    assert page.is_visible('[src="/assets/images/logo.png?v=cce222be7d237f6d95418ecb8c5529b8"]')
    context.close()
    browser.close()




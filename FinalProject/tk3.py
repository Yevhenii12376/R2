from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
    page.wait_for_timeout(1500)
    page.get_by_role("link", name="Тіло і ванна").click()
    page.wait_for_timeout(1500)
    page.locator("#popularinput-checkbox-2243-29953").click()
    page.wait_for_timeout(1500)
    page.goto("https://makeup.com.ua/ua/categorys/321073/#o[2243][]=29953")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

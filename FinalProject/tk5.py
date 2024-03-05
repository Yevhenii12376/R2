from playwright.sync_api import Playwright, sync_playwright, expect


def Perevirka_vhodu_bez_parolu(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
    page.wait_for_timeout(1000)
    page.locator(".header-office").click()
    page.wait_for_timeout(1000)
    page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
    page.get_by_role("button", name="Увійти").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    Perevirka_vhodu_bez_parolu(playwright)

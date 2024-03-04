from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("13052000n")
    page.get_by_role("button", name="Увійти").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

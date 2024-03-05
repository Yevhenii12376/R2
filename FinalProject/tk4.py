from playwright.sync_api import Playwright, sync_playwright, expect


def Perevirka_zmina_parolu(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_text("Забули пароль?").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="E-mail").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="E-mail").fill("o.ionenko129@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Нагадати").click()
    page.locator("#popup__window div").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    Perevirka_zmina_parolu(playwright)

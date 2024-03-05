from playwright.sync_api import sync_playwright

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/categorys/3/")
    page.click(".header-office")
    page.click('a[href="/ua/register/"]')
    page.check('input[name="roistat-checkbox-1"]')

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect


def Poshuk_tovaru(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
  #  page.wait_for_timeout(1500)
    page.locator(".search-button").first.click()
   # page.wait_for_timeout(1500)
    page.get_by_placeholder("Понад 249 000 товарів").fill("крем для рук")
  #  page.wait_for_timeout(1500)
    page.get_by_placeholder("Понад 249 000 товарів").press("Enter")
 #   page.wait_for_timeout(1500)
    page.goto("https://makeup.com.ua/ua/product/32739/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    Poshuk_tovaru(playwright)

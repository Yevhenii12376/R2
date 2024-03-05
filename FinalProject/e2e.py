from playwright.sync_api import Playwright, sync_playwright, expect

def e2e(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://makeup.com.ua/ua/")
    page.wait_for_timeout(5000)
    page.locator(".header-office").click()
    page.wait_for_timeout(1000)
    page.get_by_label("E-mail").click()
    page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
    page.wait_for_timeout(2000)
    page.get_by_label("E-mail").press("Tab")
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Пароль").fill("13052000n")
    page.get_by_placeholder("Пароль").press("Enter")
    page.get_by_role("link", name="Парфумерія", exact=True).click()
    page.goto("https://makeup.com.ua/ua/product/977/")
    page.wait_for_timeout(2000)
    page.get_by_title("В обране").click()
    page.wait_for_timeout(2000)
    page.locator("#popup__window").get_by_text("Не спостерігати за зміною ціни").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="2", exact=True).click()
    page.locator(".product__remove-button").first.click()
    page.get_by_text("Купити").nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_text("Оформити замовлення").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="MAKEUP").click()
    page.wait_for_timeout(2000)
    # Перевірка сторінки Доставка та оплата
    page.get_by_role("link", name="Доставка та Оплата").click()
    page.wait_for_timeout(2000)
    # Перевірка сторінки Про нас
    page.get_by_role("link", name="Про нас").click()
    page.wait_for_timeout(2000)
    page.goto("https://makeup.com.ua/ua/articles/")
    # Перевірка сторінки Акції
    page.get_by_role("link", name="Акції").click()
    # Перевірка сторінки Про магазин
    page.get_by_role("link", name="Про магазин").click()
    page.locator(".header-basket").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    e2e(playwright)

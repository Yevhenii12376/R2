import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()
def test_e2e(page):
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

# @pytest.fixture
# def test_product_search(page):
#
#     page.goto("https://makeup.com.ua/ua/")
#     page.locator(".search-button").first.click()
#     page.get_by_placeholder("Понад 249 000 товарів").fill("крем для рук")
#     page.get_by_placeholder("Понад 249 000 товарів").press("Enter")
#     page.goto("https://makeup.com.ua/ua/product/32739/")
#
# @pytest.fixture
# def test_filter_check(page):
#
#     page.goto("https://makeup.com.ua/ua/")
#     page.wait_for_timeout(1500)
#     page.get_by_role("link", name="Тіло і ванна").click()
#     page.wait_for_timeout(1500)
#     page.locator("#popularinput-checkbox-2243-29953").click()
#     page.wait_for_timeout(1500)
#     page.goto("https://makeup.com.ua/ua/categorys/321073/#o[2243][]=29953")
# #
# @pytest.fixture
# def test_password_change_verification():
#     page.goto("https://makeup.com.ua/ua/")
#     page.locator(".header-office").click()
#     page.get_by_text("Забули пароль?").click()
#     page.wait_for_timeout(1000)
#     page.get_by_role("textbox", name="E-mail").click()
#     page.wait_for_timeout(1000)
#     page.get_by_role("textbox", name="E-mail").fill("o.ionenko129@gmail.com")
#     page.wait_for_timeout(1000)
#     page.get_by_role("button", name="Нагадати").click()
#     page.locator("#popup__window div").first.click()
#
# @pytest.fixture
# def test_email_change_verification():
#
#     page.goto("https://makeup.com.ua/ua/")
#     page.wait_for_timeout(1000)
#     page.locator(".header-office").click()
#     page.wait_for_timeout(1000)
#     page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
#     page.get_by_role("button", name="Увійти").click()
#
# @pytest.fixture
# def test_verification_without_login():
#
#     page.goto("https://makeup.com.ua/ua/")
#     page.wait_for_timeout(1000)
#     page.locator(".header-office").click()
#     page.wait_for_timeout(1000)
#     page.get_by_placeholder("Пароль").click()
#     page.wait_for_timeout(1000)
#     page.get_by_placeholder("Пароль").fill("13052000n")
#     page.get_by_role("button", name="Увійти").click()
#
#




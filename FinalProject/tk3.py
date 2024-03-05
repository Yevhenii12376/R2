from playwright.sync_api import sync_playwright

def test_makeup_website():
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переходим на веб-сайт makeup.com.ua
        page.goto("https://makeup.com.ua/ua/")

        # Проверяем заголовок страницы
        assert page.title() == "MakeUp - інтернет-магазин декоративної косметики та парфумерії"

        # Проверяем наличие основных элементов на странице
        assert page.inner_text("body") != ""

        # Закрываем браузер
        context.close()
        browser.close()

# Запускаем тест
if __name__ == "__main__":
    test_makeup_website()

# import unittest
#
# from R2.classes.tester import Calculator
#
#
# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calculator = Calculator()
#     def test_add(self):
#         self.assertEqual(self.calculator.add(2,3),5)
#         self.assertEqual(self.calculator.add(-1,1),0)
#         self.assertEqual(self.calculator.add(0,0),0)
#     def test_subtract(self):
#         self.assertEqual(self.calculator.subtract(5,3),2)
#         self.assertEqual(self.calculator.subtract(10,5),5)
#         self.assertEqual(self.calculator.subtract(0, 0),0)
#
#
#     if __name__=='__main__':
#         unittest.main()
# class WebPage:
#         def __init__(self, browser):
#             self.page = browser.new_page()
#
#         def visit(self, url):
#             self.page.goto(url):
#
#         def search(self, query):
#             self.page.fill('input[name=«q»]', query)
#             self.page.click('input[value=«Google Search»]')
#
#         def get_search_results(self):
#             return self.page.inner_text(«g»)

class WebPage:
    def __init__(self, browser):
        self.page = browser.new_page()

    def visit(self, url):
        self.page.goto(url)

    def search(self, query):
        self.page.fill('input[name="q"]', query)
        self.page.click('input[value="Google Search"]')

    def get_search_results(self):
        return self.page.inner_text('g')

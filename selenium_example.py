import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/Tom/Documents/chromedriver')

    def test_search_in_python_org(self):

        browser = self.browser
        browser.get("http://www.python.org")
        self.assertIn("Python", browser.title)
        elem = browser.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source
        browser.close()

    def tearDown(self):
        self.browser.close


if __name__ == '__main__':
    unittest.main()

# browser.get('https://automatetheboringstuff.com')
#
# elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(4) > center > a:nth-child(3)')
# elem.click()
#
# elems = browser.find_elements_by_css_selector('p')
# searchElem = browser.find_element_by_css_selector('#twotabsearchtextbox')
# searchElem.send_keys('Automate the boring stuff')
# searchElem.submit()
#
# resultsElems = browser.find_element_by_css_selector('span')
# print(resultsElems.text)
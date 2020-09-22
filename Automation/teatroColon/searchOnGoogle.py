import unittest
from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.keys import Keys

teatroColonXpath = '/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/div/cite'

path='C:\\Automation\\geckodriver'
driver = Firefox(executable_path=path)


class SearchCases(unittest.TestCase):

    def test_centrosDeAtencion(self):
        driver.get('https://www.google.com/')
        driver.find_element_by_name('q').send_keys('teatro colon')
        driver.find_element_by_name('q').send_keys(Keys.ENTER)
        self.assertTrue('teatrocolon.org.ar' in driver.find_element_by_xpath(teatroColonXpath).text)
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()


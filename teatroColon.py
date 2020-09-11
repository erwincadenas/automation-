import unittest
from selenium import webdriver
from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.keys import Keys

#path='C:\\Automation\\geckodriver'
#driver = Firefox(executable_path=path)
#driver.implicitly_wait(10)

class TeatroColon(unittest.TestCase):
    def setUp(self):
        path='C:\\Automation\\geckodriver'
        driver = Firefox(executable_path=path)
        driver.implicitly_wait(10)
        driver.get('https://teatrocolon.org.ar/es')

        
    def test_donaciones(self):
        driver.find_element_by_css_selector('.nav-entradas').click()
        self.assertEqual(driver.find_element_by_css_selector('h1.page-header > span:nth-child(1)').text, 'DONACIONES')
    
    def test_busqueda_orquesta(self):
        driver.find_element_by_class_name('btn-search').click()
        driver.find_element_by_name('keys').send_keys('orquesta')
        driver.find_element_by_name('keys').send_keys(Keys.ENTER)
        driver.find_element_by_css_selector('div.item_search:nth-child(4) > span:nth-child(1) > h4:nth-child(1) > strong:nth-child(1) > a:nth-child(1)').click()
        self.assertEqual(driver.find_element_by_css_selector('h1.page-header > span:nth-child(1)').text, 'ORQUESTA FILARMÓNICA DE BUENOS AIRES')

    def test_noticias(self):
        driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/nav[2]/ul/li[9]/a').click()
        driver.find_element_by_css_selector('.link-vermas').click()
        driver.find_element_by_name('categories[23]').click()
        self.assertTrue('ISATC en Mar del Plata' in driver.find_element_by_partial_link_text('ISATC en Mar del Plata').text)



    def tearDown(self):
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()
        
import unittest
from selenium import webdriver
from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.keys import Keys
from pageIndex import PageIndex


class TeatroColon(unittest.TestCase):
    
    def setUp(self):
        path='C:\\Automation\\geckodriver'
        self.driver = Firefox(executable_path=path)
        self.driver.implicitly_wait(10)
        self.driver.get('https://teatrocolon.org.ar/es')
        self.indexPage = PageIndex(self.driver)

        
    def test_donaciones(self):
        self.driver.find_element_by_css_selector('.nav-entradas').click()
        self.assertEqual(self.driver.find_element_by_css_selector('h1.page-header > span:nth-child(1)').text, 'DONACIONES')
    
    def test_busqueda_orquesta(self):
        #self.driver.find_element_by_class_name('btn-search').click()
        #self.driver.find_element_by_name('keys').send_keys('orquesta')
        #self.driver.find_element_by_name('keys').send_keys(Keys.ENTER)
        self.indexPage.search('orquesta')
        self.driver.find_element_by_css_selector('div.item_search:nth-child(4) > span:nth-child(1) > h4:nth-child(1) > strong:nth-child(1) > a:nth-child(1)').click()
        self.assertEqual(self.driver.find_element_by_css_selector('h1.page-header > span:nth-child(1)').text, 'ORQUESTA FILARMÓNICA DE BUENOS AIRES')

    def test_noticias(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/nav[2]/ul/li[9]/a').click()
        self.driver.find_element_by_css_selector('.link-vermas').click()
        self.driver.find_element_by_name('categories[23]').click()
        self.assertTrue('ISATC en Mar del Plata' in self.driver.find_element_by_partial_link_text('ISATC en Mar del Plata').text)



    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
        
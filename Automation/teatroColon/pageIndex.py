from selenium.webdriver.common.keys import Keys

class PageIndex():
    def __init__(self, my_driver):
        self.search_button = 'btn-search'
        self.search_bar = 'keys'
        self.driver = my_driver
    
    def search(self, item):
        self.driver.find_element_by_class_name(self.search_button).click()
        self.driver.find_element_by_name(self.search_bar).send_keys(item)
        self.driver.find_element_by_name(self.search_bar).send_keys(Keys.ENTER)

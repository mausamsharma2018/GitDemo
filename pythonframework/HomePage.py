
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
     self.driver= driver


    shop = (By.XPATH, "//input[@minlength='2']")

    def loginData(self):
        return self.driver.find_element(HomePage.shop)
import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pythonframework.HomePage import HomePage
from utilities.Baseclass import Baseclass


class Tests(Baseclass):

    def test_e2e(self,setup):

       self.driver.find_element(By.XPATH, "//input[@minlength='2']").send_keys("mausam")
       self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("maasum190@gmail.com")
       self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("Qwerty@3820")
       self.driver.find_element(By.ID, "exampleCheck1").click()
       assert self.driver.find_element(By.ID, "exampleCheck1").is_selected()

       # static dropdown
       dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
       dropdown.select_by_visible_text("Female")

       self.driver.find_element(By.XPATH, "//label[.='Student']").click()
       assert not self.driver.find_element(By.XPATH, "//label[.='Student']").is_selected()
       self.driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("28/10/1990")
       self.driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
       time.sleep(3)
       print(self.driver.current_url)
       print(self.driver.title)
       Success_text = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
       assert "Success! " in Success_text

       self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()

       # dynamic list.
       elements = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
       for ele in elements:
           # Cahaining of locators.
           # //div[@class='card h-100']/div/h4/a
           product = ele.find_element(By.XPATH, "div/h4/a").text
           if product == "iphone X":
               # //div[@class='card h-100']/div/button
               ele.find_element(By.XPATH, "div/button").click()
       time.sleep(2)
       # driver.execute_script("window.scrollBy(500,0);")
       self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
       self.driver.find_element(By.XPATH, "//button[contains(.,'Checkout')]").click()
       self.driver.find_element(By.ID, "country").send_keys("ind")

       # Explicit wait
       wait = WebDriverWait(self.driver, 10)
       wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

       # dynamic dropdown
       self.driver.find_element(By.LINK_TEXT, "India").click()
       self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
       self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
       success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
       assert "Success! " in success_text




import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name= request.config.getoption("browser_name")
    if browser_name == "chrome":
        serv_obj = Service('C:/Drivers/chromedriver-win64/chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("maximize")
        driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
        driver.implicitly_wait(5)

    elif browser_name== "firefox":
        serv_obj = Service('C:/Drivers/geckodriver-v0.34.0-win64/geckodriver.exe')
        driver = webdriver.Firefox(service=serv_obj)
    elif browser_name== "Edge":
        serv_obj = Service('C:/Drivers/edgedriver_win64/msedgedriver.exe')
        driver = webdriver.Edge(service=serv_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(3) #ожидание

        self.driver.maximize_window()
        self.driver.get(address)


    def find_element(self, mode, path):
        # поиск элементов
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        # изменение свойств
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
    #закрытие соединения
        self.driver.close()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):     #драйвер инициализировали в conftest
        self.driver = driver
        #зададим базовый адрес сайта
        self.base_url = "https://test-stand.gb.ru/login"

    def find_element(self, locator, time=10): #locator путь к объекту, time - время ожидания
        # поиск элементов. После until, ждем появление элементов, которые должны будем найти
        # message появляется, в случае, если элемент не найден
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        # изменение свойств
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        #метод возвращает открытую страницу
        return self.driver.get(self.base_url)

    def alert(self):
        return self.driver.switch_to.alert

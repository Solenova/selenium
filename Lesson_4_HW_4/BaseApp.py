import logging

import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from zeep import Client, Settings


class BasePage:
    def __init__(self, driver):  # драйвер инициализировали в conftest
        self.driver = driver
        # зададим базовый адрес сайта
        self.base_url = "https://test-stand.gb.ru/login"
        # s = requests.Session
        self.session = requests.Session

    def find_element(self, locator, time=10):  # locator путь к объекту, time - время ожидания
        # поиск элементов. После until, ждем появление элементов, которые должны будем найти
        # message появляется, в случае, если элемент не найден
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            # в случае вызова исключения element = None
            element = None
        return element

    def get_element_property(self, locator, property):
        # изменение свойств
        element = self.find_element(locator)
        # т.к. ссылаемся на предыдущую функцию, а в ней ошибки обработаны, то можно использовать обработку исключений,
        # только в случае когда элемент не найден
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
            return None

    def go_to_site(self):
        # метод возвращает открытую страницу
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browser = None
        return start_browser

    def alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except:
            logging.exception("Exception with alert")
            return None


class BasePageAPI:
    def __init__(self):  # драйвер инициализировали в conftest
        self.base_url = "https://test-stand.gb.ru/gateway/login"
        self.url_post = "https://test-stand.gb.ru/api/posts"
        # s = requests.Session
        self.session = requests.Session()

    def user_token(self, login:str, password:str):
        try:
            result = self.session.post(url=self.base_url, data=dict(username=login, password=password))
            response_json = result.json()
            token = response_json.get('token')
            return token
        except:
            logging.exception("Exception user token")
            return None

    def get_list_post(self, token, owner):
        try:
            result = self.session.get(url=self.url_post, headers={'X-Auth-Token': token},
                                params={'owner': owner}).json()['data']
            print(result)
            return result
        except:
            logging.exception("Exception list post")
            return None

    def post_create(self, token, title, description, content, headers_value):
        # Создаем пост на тест-стенде GB
        try:
            result = self.session.post(url=self.url_post, headers={'X-Auth-Token': token}, data={
                'title': title,
                'description': description,
                'content': content
            }).json()[headers_value]
            print(result)
            return result
        except:
            logging.exception("Exception create post")
            return None

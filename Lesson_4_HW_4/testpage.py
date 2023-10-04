from BaseApp import BasePage, BasePageAPI
from selenium.webdriver.common.by import By
import logging
import time
import yaml
import requests

S = requests.Session()

class TestSearchLocators:
    #тип поиска будем хранить в локаторе
    # поиск элемента по имени. Зведем словарь для хранения пары тип пути(id, xpath, css..) и самого пути
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)

    #     создадим циклы, чтобы определить локаторы: внешний для xpath, внутренний для css
    for locator in locators["xpath"].keys():
        # в элемент словаря с ключом locator заносим значение из By.XPATH и заносим значение,
        # которое соответствует ключу из раздела "xpath" и подраздела с ключом locator
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    #спользует базовые операции из BasePage

    def enter_text_info_fild(self, locator, word, description=None):
        #функция для обработки ошибок в методах ввода данных. description - удобочитемое обозначение локатора
        #сначла находим поле по локатору. find_element обработан на более низком уровне
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug((f"Send {word} to element {element_name}"))
        field = self.find_element(locator)
        if not field:
            logging.exception(f"Element {locator} not fount")
            return False
        #else не будет т.к. уже вернули False
        #необходимо очистить, может быть ошибка
        try:
            # field.clear()
            time.sleep(1)
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Excaption with click")
            return False
        logging.debug(f"Click {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=5)

        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Excaption while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

        #ENTER TEXT методы ввода текста

    def enter_login(self, word):
        # поиск элемента и обработка исключений в методе enter_text_info_fild Поэтому вызовем его
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, word):
        time.sleep(1)
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_TITLE_FILD"], word, description="title fild")
        # сначала найдем элемент

    def enter_description(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], word, description="description fild")

    def enter_content(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_CONTENT_FILD"], word, description="content fild")

    def enter_your_name_fild(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_YOUR_NAME_FILD"], word, description="your_name form")

    def enter_your_email_fild(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_FIELD"], word, description="your_email form")

    def enter_content_contact_fild(self, word):
        self.enter_text_info_fild(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT_FILD"], word, description="content_contact form")

    #CLICK metod
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")# нашли кнопку и кликнули по кнопке

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BTN"], description="create post") # нашли кнопку и кликнули по кнопке

    def click_save_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save post") # нашли кнопку и кликнули по кнопке

    def click_contact_href(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_HREF"], description="contact") # нашли кнопку и кликнули по кнопке
        # time.sleep(1)

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact send")
        time.sleep(1)


    #GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error_text")

    def get_title_text(self):
        # time.sleep(3)
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_TITLE_FILD"], description="title field")

    def get_title_post_text(self):
        # time.sleep(3)
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_TITLE_POST_TEXT"], description="title_post")

    def login_success(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_SUCCESS"], description="login_success")

    def alert_contact_text(self):
        logging.info("Go to alert")
        alert = self.alert().text
        logging.info("вызов алерт")
        logging.info("text alert")
        return alert


class OperationsHelperAPI(BasePageAPI):


    # REST
    def selection_from_list_post(self, login, password, owner, header_field):
        logging.info("Go to selection_from_list_post")
        result = self.get_list_post(self.user_token(login, password), owner=owner)
        result_header = [i[header_field] for i in result]
        return result_header

    def create_new_post_headers_value(self, login, password, title, description, content, headers_value):
        logging.info("Go to create_new_post_headers_value")
        self.post_create(self.user_token(login, password), title, description, content, headers_value)

    # def selection_from_list_newpost(self, login, password, title, description, content, header_field):
    #     logging.info("Go to selection_from_list_newpost")
    #     self.post_create(self.user_token(login, password), title, description, content, header_field)



#
# data=
# 'title': testdata['title'],
# 'description': testdata['description'],
# 'content': testdata['content']
# }
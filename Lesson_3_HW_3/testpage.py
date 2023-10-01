from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class TestSearchLocators:
    #тип поиска будем хранить в локаторе
    # поиск элемента по имени
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_SUCCESS = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FILD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FILD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_TITLE_POST_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_HREF = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FILD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_CONTACT_FILD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    #спользует базовые операции из BasePage
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        #ввод логина
        #сначала найдем элемент
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        #ввод пароля
        #сначала найдем элемент
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click() # нашли кнопку и кликнули по кнопке

    def get_error_text(self):
        logging.error(f"start find error text")
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text{text} in error field{TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        #возвращаем текст ошибки
        return text

    def login_success(self):
        logging.error(f"start find success text")
        success_filed = self.find_element(TestSearchLocators.LOCATOR_SUCCESS, time=2)
        text = success_filed.text
        logging.info(f"We find text{text} in error field{TestSearchLocators.LOCATOR_SUCCESS[1]}")
        return text

    def click_create_post_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN).click()  # нашли кнопку и кликнули по кнопке

    def enter_title(self, word):
        logging.info(f"Send title post to element {TestSearchLocators.LOCATOR_TITLE_FILD[1]}")
        # сначала найдем элемент
        description_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FILD)
        time.sleep(1)
        # вводим текст
        description_field.send_keys(word)
        text = description_field.text
        logging.info(f"We find text{word} in error field{TestSearchLocators.LOCATOR_TITLE_FILD[1]}")
        return text

    def enter_description(self, text):
        logging.info(f"Send description post to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}")
        #сначала найдем элемент
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        # вводим текст
        description_field.send_keys(text)

    def enter_content(self, text):
        logging.info(f"Send {text} to element {TestSearchLocators.LOCATOR_CONTENT_FILD[1]}")
        #ввод логина
        #сначала найдем элемент
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FILD)
        content_field.send_keys(text)

    def click_save_button(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click() # нашли кнопку и кликнули по кнопке

    def get_title_post_text(self):
        logging.error(f"start title_post_text")
        time.sleep(3)
        title_post_text = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST_TEXT, time=3)
        text = title_post_text.text
        logging.info(f"We find text{text} in error field{TestSearchLocators.LOCATOR_TITLE_POST_TEXT[1]}")
        #возвращаем текст ошибки
        return text

    def click_contact_href(self):
        logging.info("Click contact_href")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_HREF).click() # нашли кнопку и кликнули по кнопке

    def enter_your_name_fild(self, word):
        logging.info(f"Send name contact to element {TestSearchLocators.LOCATOR_YOUR_NAME_FILD[1]}")
        # сначала найдем элемент
        time.sleep(1)
        your_name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FILD)
        # вводим текст
        your_name_field.send_keys(word)

        logging.info(f"We find text{word} in error field{TestSearchLocators.LOCATOR_YOUR_NAME_FILD[1]}")

    def enter_your_email_fild(self, text):
        logging.info(f"Send your_email contact to element {TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD[1]}")
        # сначала найдем элемент
        your_email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD)
        # вводим текст
        your_email_field.send_keys(text)

    def enter_content_contact_fild(self, text):
        logging.info(f"Send content contact to element {TestSearchLocators.LOCATOR_CONTENT_CONTACT_FILD[1]}")
        # ввод логина
        # сначала найдем элемент
        content_contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT_FILD)
        content_contact_field.send_keys(text)

    def click_contact_us_btn(self):
        logging.info("Click Contact Us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()
        time.sleep(5)
        # time.sleep(2)
                    # нашли кнопку и кликнули по кнопке

    def alert_contact_text(self):
        logging.info("Go to alert")

        alert = self.alert().text

        logging.info("вызов алерт")

        logging.info("text alert")

        return alert

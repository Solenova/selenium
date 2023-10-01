from testpage import OperationsHelper
import logging
import yaml
import time

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("start test_login_negative starting")  # логирование
    # инициализируем объект класса OperationsHelper и передадим ему фикстуру browser, которя вернет driver
    testpage = OperationsHelper(browser)
    # открываем страницу
    testpage.go_to_site()
    # туда вводим логин
    testpage.enter_login("test")
    # туда вводим password
    testpage.enter_pass("test")
    # клик по кнопке
    testpage.click_login_button()

    # при проверке сверяем, чо находится в элементе с ошибкой с текстом ожидаемой ошибки
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_login_positive(browser):
    logging.info("start test_login_positive starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    # туда вводим логин
    testpage.enter_login(testdata["login"])
    # туда вводим password
    testpage.enter_pass(testdata["password"])

    testpage.click_login_button()

    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"


def test_create_new_post(browser):
    logging.info("start test_create_new_post starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    # туда вводим логин
    testpage.enter_login(testdata["login"])
    # туда вводим password
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    # зашли на страницу со своими постами
    testpage.click_create_post_button()

    testpage.enter_title(testdata["title"])
    testpage.enter_description(testdata["description"])
    testpage.enter_content(testdata["content"])
    testpage.click_save_button()

    # time.sleep(testdata["sleep_time"])

    assert testpage.get_title_post_text() == testdata["title"], "test_step1 FAILED"


def test_add_contact(browser):
    logging.info("start test_add_contact starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    # туда вводим логин
    testpage.enter_login(testdata["login"])
    # туда вводим password
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    # зашли на страницу со своими постами
    testpage.click_contact_href()

    testpage.enter_your_name_fild(testdata["name"])
    testpage.enter_your_email_fild(testdata["email"])
    testpage.enter_content_contact_fild(testdata["content"])
    testpage.click_contact_us_btn()


    assert testpage.alert_contact_text() == testdata["text_alert_contact"], "test_add_contact FAILED"

# css_selector = "span.mdc-text-field__ripple" # выбрали на сайте через инструмент разработчика "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))

import time
from lib2to3.pgen2 import driver

import yaml
from isodate import Duration
from selenium.webdriver.support.wait import WebDriverWait

from module import Site


with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):
    #поиск элемента по имени
    input1 = site.find_element("xpath", x_selector1)
    # отправим не правильную информацию с неправильным логином
    input1.send_keys("test")

    # туда тоже внесем тест
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn = site.find_element("css", btn_selector)
    #клик по кнопке
    btn.click()

    #надо получить оттуда текст и поверить, что текст = 401
        #сначала найдем элемент. после закрытия браузера, не можем обращаться к свойствам элемента(например, совйства text)
    err_label = site.find_element("xpath", x_selector3).text


    assert err_label == error_code, "test_step1 FAILED"


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, account_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])

    btn = site.find_element("css", btn_selector)
    btn.click()

    code_label = site.find_element("xpath", x_selector4).text

    assert code_label == account_name, "test_step1 FAILED"


def test_create_new_post(x_selector1, x_selector2, btn_selector,
                         btn_create_selector, title_selector, description_selector, content_selector,
                         title_post_selector, btn_save_selector):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    btn_create = site.find_element("xpath", btn_create_selector)
    btn_create.click()

    time.sleep(testdata["sleep_time"])
    input3 = site.find_element("xpath", title_selector)
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", description_selector)
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", content_selector)
    input5.send_keys(testdata["content"])

    btn_save = site.find_element("xpath", btn_save_selector)
    btn_save.click()

    time.sleep(testdata["sleep_time"])
    code_label = site.find_element("xpath", title_post_selector).text

    assert code_label == testdata["title"], "test_step1 FAILED"



# css_selector = "span.mdc-text-field__ripple" # выбрали на сайте через инструмент разработчика "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))
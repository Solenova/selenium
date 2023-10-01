import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="session") #фикстура будет действовать всю сессию, указали параметр
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    # закрытие браузера
    yield driver
    driver.quit()


@pytest.fixture()
def x_selector1():
    #для заполнения selector переходим на форму тестируемую, выбираем элемент(например, поле ввода) copy xpath
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def x_selector2():
    #поле для пароля занесем в x_selector2
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    #найти код   ошибки тоже в среде разработчика и копируем xpath
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def x_selector4():
    #найти код   ошибки тоже в среде разработчика и копируем xpath
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def btn_selector():
    #проверим кнопку.Она на форме одна, поэтому идентификатор просто button
    return "button"

@pytest.fixture()
def error_code():
    return "401"

@pytest.fixture()
def account_name():
    return f"Hello, {testdata['login']}"

@pytest.fixture()
def btn_create_selector():
    # Создаем пост на тест-стенде GB
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label"""
    # // *[ @ id = "create-item"] / div / div / div[1] / div / label / inp
    # // *[ @ id = "create-item"] / div / div / div[1] / div / label / span    # error
# //*[@id="create-item"]/div/div/div[1]/div/label   # Title
# //*[@id="create-item"]/div/div/div[1]/div/label/input  #none
# //*[@id="create-item"]/div/div/div[1]/div #error

@pytest.fixture()
def description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def btn_save_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def title_post_selector():
    return """//*[@id="app"]/main/div/div[1]/h1"""

from testpage import OperationsHelperAPI
import requests
import yaml
import logging

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

S = requests.Session()


def test_validation_account():
    logging.info("start test_login_negative starting")
    testpage = OperationsHelperAPI()

    result_title = testpage.selection_from_list_post(testdata['login'], testdata['password'], 'notMe', 'title')
    assert testdata['title_sample'] in result_title, 'test_step1 FAIL'


def test_create_post():
    logging.info("start test_login_negative starting")
    testpage = OperationsHelperAPI()
    testpage.create_new_post_headers_value(testdata['login'], testdata['password'],testdata['title'],
                                                           testdata['description'], testdata['content'], 'description')
    list_posts = testpage.selection_from_list_post(testdata['login'], testdata['password'], None, 'description')

    assert testdata['description'] in list_posts, 'test_step1 FAIL'

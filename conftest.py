import allure

from data import URLS
from pages.personal_account_page import PersonalAccountPage

import pytest 
import requests
from selenium import webdriver
from data import URLS, Browser
import helpers

@pytest.fixture(params=[Browser.Firefox, Browser.Firefox])
def driver(request): 
    with allure.step(f'Запускаем браузер {request.param}'): 
        if request.param == Browser.Firefox:
            driver = webdriver.Firefox() 
        elif request.param == Browser.Chrome: 
            driver = webdriver.Chrome() 
        driver.get(URLS.BASE_URL)

    yield driver
    driver.quit()

@pytest.fixture
def create_user(): 
    user = helpers.generate_user_info()
    response = requests.post(URLS.CREATE_USER, json=user)
    del user['name']
    yield user
    token = response.json()['accessToken']
    requests.delete(URLS.DELETE_USER, headers={'Authorization': token})

@pytest.fixture
def login_user(driver, create_user): 
    login_page = PersonalAccountPage(driver)
    login_page.open_login_url()
    login_page.authorization_user(create_user['email'], create_user['password'])

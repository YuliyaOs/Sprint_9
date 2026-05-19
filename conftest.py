from selenium import webdriver
import pytest
import configuration
import data
from api_framework.user_api import UserApi
import pytest
from helpers import generate_data


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.set_capability('selenoid:options', {
        'enableVNC': True,
        'enableVideo': False,
        'screenResolution': '1920x1080x24',
        'sessionTimeout': '15m'
    })
    return options


@pytest.fixture
def data_for_create_user():
    first_name = generate_data.generate_random_string(10)
    last_name = generate_data.generate_random_string(10)
    username = generate_data.generate_random_string(10)
    email = generate_data.generate_email()
    password = generate_data.generate_random_string(11)
    return first_name, last_name, username, email, password


@pytest.fixture
def data_for_create_receipt():
    name, ingredient, amount, time, description, file = data.data_for_receipt.values()
    return name, ingredient, amount, time, description, file


@pytest.fixture
def driver():
    options = get_default_chrome_options()
    driver = webdriver.Remote(
        command_executor=configuration.SELENOID_REMOTE_URL, options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.get(configuration.URL)
    yield driver
    driver.quit()


@pytest.fixture
def driver_for_auth(data_for_create_user):
    options = get_default_chrome_options()
    driver = webdriver.Remote(
        command_executor=configuration.SELENOID_REMOTE_URL, options=options)
    driver.get(configuration.URL)
    user = UserApi()
    user.create_user(*data_for_create_user)
    username, password = data_for_create_user[2], data_for_create_user[4]
    yield driver, username, password
    driver.quit()


@pytest.fixture
def driver_with_auth(data_for_create_user):
    options = get_default_chrome_options()
    driver = webdriver.Remote(
        command_executor=configuration.SELENOID_REMOTE_URL, options=options)
    driver.get(configuration.URL)
    user = UserApi()
    user.create_user(*data_for_create_user)
    response = user.login_user(
        data_for_create_user[2], data_for_create_user[4])
    token = response.json()['auth_token']
    driver.execute_script(
        f'window.localStorage.setItem("token", "{token}");')
    driver.refresh()
    yield driver
    driver.quit()

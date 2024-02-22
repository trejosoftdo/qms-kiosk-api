"""Integration tests environment setup"""

from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.main import app
from app.environment import (
    test_auth_application,
    test_auth_username,
    test_auth_password,
)
from app.features import constants

# pylint: disable=W0613


@fixture
def setup_web_driver(context, *args, **kwargs):
    """Sets up the web driver"""
    options = Options()
    options.add_argument(constants.DRIVER_HEADLESS_MODE_OPTION)
    options.add_argument(constants.DRIVER_NO_SANDBOX_OPTION)
    options.add_argument(constants.DRIVER_DISABLE_DEV_SHM_OPTION)
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )


@fixture
def setup_api_client(context, *args, **kwargs):
    """Sets up Test API Client"""
    context.client = TestClient(app)


@fixture
def setup_headers(context, *args, **kwargs):
    """Sets up Test headers"""
    context.common_headers = {
        "application": test_auth_application,
    }


@fixture
def setup_user_credentials(context, *args, **kwargs):
    """Sets up user credentials"""
    context.credentials = {
        "username": test_auth_username,
        "password": test_auth_password,
    }


@fixture
def setup_payloads(context, *args, **kwargs):
    """Sets up Test Payloads"""
    context.invalid_token = constants.INVALID_TOKEN
    context.payloads = {
        constants.AUTH_DEVICE_PATH: {},
        constants.AUTH_TOKENS_PATH: {
            "VALID": {},
            "INVALID": {},
        },
        constants.AUTH_REFRESH_TOKEN_PATH: {
            "VALID": {},
            "INVALID": {},
        },
    }


def before_feature(context, feature):
    """Run setup steps before running feature files"""
    use_fixture(setup_api_client, context)
    use_fixture(setup_headers, context)
    use_fixture(setup_payloads, context)
    use_fixture(setup_web_driver, context)
    use_fixture(setup_user_credentials, context)

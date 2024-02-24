"""Auth API helpers
"""

import requests
from .. import environment
from .. import constants
from .constants import (
    AUTH_DEVICE_EXTERNAL_PATH,
    AUTH_TOKENS_EXTERNAL_PATH,
    AUTH_TOKEN_VALIDATE_EXTERNAL_PATH,
    AUTH_TOKEN_REFRESH_EXTERNAL_PATH,
)


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: Common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.iam_api_key,
    }


def get_common_payload() -> dict:
    """Gets the request common payload

    Returns:
        dict: Common payload
    """
    return {
        "clientId": environment.app_client_id,
        "clientSecret": environment.app_client_secret,
    }


def auth_device(
    application: str, scopes=constants.DEVICE_TOKEN_SCOPES
) -> requests.Response:
    """Authorizes a device to a application in context via the auth API

    Args:
        application (str): The application in context

    Returns:
        requests.Response: The response from the auth API.
    """
    auth_device_url = f"{environment.auth_api_base_url}{AUTH_DEVICE_EXTERNAL_PATH}"
    payload = {
        **get_common_payload(),
        "scope": constants.SCOPES_SEPARATOR.join(scopes),
    }
    headers = {**get_common_headers(), "application": application}
    return requests.post(
        auth_device_url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )


def get_auth_tokens(application: str, device_code: str) -> requests.Response:
    """Gets the authorization tokens for the given device code and application in context

    Args:
        application (str): The application in context
        device_code (str): The code of the device to authorize

    Returns:
        requests.Response: The response from the auth API.
    """
    get_auth_tokens_url = f"{environment.auth_api_base_url}{AUTH_TOKENS_EXTERNAL_PATH}"
    payload = {
        **get_common_payload(),
        "deviceCode": device_code,
    }
    headers = {**get_common_headers(), "application": application}
    return requests.post(
        get_auth_tokens_url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )


def validate_token(
    application: str, authorization: str, expected_scope: str
) -> requests.Response:
    """Gets information such as scope and active from the given token

    Args:
        application (str): The application in context
        authorization (str): The access token to validate
        expected_scope (str): The expected scope

    Returns:
        requests.Response: The response from the auth API.
    """
    validate_token_url = (
        f"{environment.auth_api_base_url}{AUTH_TOKEN_VALIDATE_EXTERNAL_PATH}"
    )
    payload = {
        **get_common_payload(),
        "expectedScope": expected_scope,
    }
    headers = {
        **get_common_headers(),
        "application": application,
        "authorization": authorization,
    }
    return requests.post(
        validate_token_url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )


def get_new_access_token(application: str, refresh_token: str) -> requests.Response:
    """Gets a new access token

    Args:
        application (str): The application in context
        refresh_token (str): The refresh token

    Returns:
        requests.Response: The response from the auth API.
    """
    refresh_token_url = (
        f"{environment.auth_api_base_url}{AUTH_TOKEN_REFRESH_EXTERNAL_PATH}"
    )
    payload = {
        **get_common_payload(),
        "refreshToken": refresh_token,
    }
    headers = {**get_common_headers(), "application": application}
    return requests.post(
        refresh_token_url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )

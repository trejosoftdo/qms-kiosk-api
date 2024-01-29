import requests
from urllib.parse import urlencode
from .. import environment
from .. import constants


common_headers = {
  'Content-Type': 'application/json',
  'api_key': environment.iam_api_key,
}

common_payload = {
  'clientId': environment.app_client_id,
  'clientSecret': environment.app_client_secret,
}

def auth_device(application: str) -> requests.Response:
  """Authorizes a device to a application in context via the auth API

  Args:
      application (str): The application in context

  Returns:
      requests.Response: The response from the auth API.
  """
  auth_device_url = f"{environment.auth_api_base_url}/api/v1/auth/device"
  payload = {
    **common_payload,
    'scope': constants.SCOPES_SEPARATOR.join(constants.DEVICE_TOKEN_SCOPES),
  }
  headers = {
    **common_headers,
    'application': application
  }
  return requests.request('POST', auth_device_url, headers = headers, json = payload)


def get_auth_tokens(application: str, device_code: str) -> requests.Response:
  """Gets the authorization tokens for the given device code and application in context

  Args:
      application (str): The application in context
      device_code (str): The code of the device to authorize

  Returns:
      requests.Response: The response from the auth API.
  """
  get_auth_tokens_url = f"{environment.auth_api_base_url}/api/v1/auth/tokens"
  payload = {
    **common_payload,
    'deviceCode': device_code,
  }
  headers = {
    **common_headers,
    'application': application
  }
  return requests.request('POST', get_auth_tokens_url, headers = headers, json = payload)


def validate_token(application: str, authorization: str, expected_scope: str) -> requests.Response:
  """Gets information such as scope and active from the given token

  Args:
      application (str): The application in context
      authorization (str): The access token to validate
      expected_scope (str): The expected scope

  Returns:
      requests.Response: The response from the auth API.
  """
  validate_token_url = f"{environment.auth_api_base_url}/api/v1/auth/token/validate"
  payload = {
    **common_payload,
    'expectedScope': 'expected_scope',
  }
  headers = {
    **common_headers,
    'application': application,
    'authorization': authorization, 
  }
  return requests.request('POST', validate_token_url, headers = headers, json = payload)


def get_new_access_token(application: str, refresh_token: str) -> requests.Response:
  """Gets a new access token

  Args:
      application (str): The application in context
      refresh_token (str): The refresh token

  Returns:
      requests.Response: The response from the auth API.
  """
  refresh_token_url = f"{environment.auth_api_base_url}/api/v1/auth/token/refresh"
  payload = {
    **common_payload,
    'refreshToken': refresh_token,
  }
  headers = {
    **common_headers,
    'application': application
  }
  return requests.request('POST', refresh_token_url, headers = headers, json = payload)

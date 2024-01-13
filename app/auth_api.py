import requests
from urllib.parse import urlencode
from . import environment


common_headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def auth_device(realm: str) -> requests.Response:
  """Authorizes a device to a realm in context via the auth API

  Args:
      realm (str): The realm in context

  Returns:
      requests.Response: The response from the auth API.
  """
  auth_device_url = f"{environment.auth_api_base_url}/realms/{realm}/protocol/openid-connect/auth/device"
  payload = urlencode({
    'client_id': environment.auth_api_client_id,
    'client_secret': environment.auth_api_client_secret,
  })
  return requests.request('POST', auth_device_url, headers = common_headers, data = payload)


def get_auth_tokens(realm: str, device_code: str) -> requests.Response:
  """Gets the authorization tokens for the given device code and realm in context

  Args:
      realm (str): The realm in context
      device_code (str): The code of the device to authorize

  Returns:
      requests.Response: The response from the auth API.
  """
  get_auth_tokens_url = f"{environment.auth_api_base_url}/realms/{realm}/protocol/openid-connect/token"
  payload = urlencode({
    'device_code': device_code,
    'grant_type': 'urn:ietf:params:oauth:grant-type:device_code',
    'client_id': environment.auth_api_client_id,
    'client_secret': environment.auth_api_client_secret,
  })
  return requests.request('POST', get_auth_tokens_url, headers = common_headers, data = payload)


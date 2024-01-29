from fastapi import HTTPException
from . import models
from . import api

INTERNAL_ERROR = HTTPException(
  status_code = 500,
  detail = {
    'message': 'Unexpected error',
    'code': 'INTERNAL_ERROR',
  }
)

def authorize_device(application: str) -> models.AuthorizeDeviceResponseData:
  """Authorizes a device to a application in context via the auth API

  Args:
      application (str): the application in context

  Returns:
      models.AuthorizeDeviceResponseData: Authorization information such as deviceCode, and userCode.
  """
  response = api.auth_device(application)
  data = response.json().get('data', {})
  return models.AuthorizeDeviceResponse(
    data = models.AuthorizeDeviceResponseData(
      deviceCode = data.get('deviceCode'),
      userCode = data.get('userCode'),
      expiresIn = data.get('expiresIn'),
      interval = data.get('interval'),
      verificationURI = data.get('verificationURI'),
    )
  )


def get_auth_tokens(application: str, device_code: str) -> models.GetTokensResponse:
  """Gets the authorization tokens for the given device code and application in context

  Args:
      application (str): The application in context
      device_code (str): The device code to authorize

  Raises:
      HTTPException: When validation errors are encountered.
      HTTPException: When unexpected errors are encountered

  Returns:
      models.GetTokensResponse: The authorization tokens information
  """
  response = api.get_auth_tokens(application, device_code)
  
  if (response.status_code == 400):
    detail = response.json().get('detail', {})
    raise HTTPException(
      status_code = 400,
      detail = detail,
    )
  
  if response.status_code > 400:
    raise INTERNAL_ERROR

  data = response.json().get('data', {})
  return models.GetTokensResponse(
    data = models.GetTokensResponseData(
      accessToken = data.get('accessToken'),
      refreshToken = data.get('refreshToken'),
      expiresIn = data.get('expiresIn'),
      refreshExpiresIn = data.get('refreshExpiresIn'),
    )
  )

def get_new_access_token(application: str, refresh_token: str) -> models.GetNewAccessTokenResponse:
  """Gets a new authorization token for the given refresh token and application in context

  Args:
      application (str): The application in context
      refresh_token (str): The refresh token

  Raises:
      HTTPException: When validation errors are encountered.
      HTTPException: When unexpected errors are encountered

  Returns:
      models.GetNewAccessTokenResponse: The new access token data
  """
  response = api.get_new_access_token(application, refresh_token)
  
  if (response.status_code == 400):
    detail = response.json().get('detail', {})
    raise HTTPException(
      status_code = 400,
      detail = detail,
    )
  
  if response.status_code > 400:
    raise INTERNAL_ERROR

  data = response.json().get('data', {})
  return models.GetNewAccessTokenResponse(
    data = models.GetNewAccessTokenResponseData(
      accessToken = data.get('accessToken'),
      expiresIn = data.get('expiresIn'),
    )
  )

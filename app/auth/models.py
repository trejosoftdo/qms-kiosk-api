"""Auth API models
"""

from pydantic import BaseModel


class GetTokensPayload(BaseModel):
    """Payload to get the device tokens

    Args:
        BaseModel (class): Base model class
    """

    deviceCode: str


class AuthorizeDeviceResponseData(BaseModel):
    """Authorize device response data

    Args:
        BaseModel (class): Base model class
    """

    deviceCode: str
    userCode: str
    expiresIn: int
    interval: int
    verificationURI: str


class AuthorizeDeviceResponse(BaseModel):
    """Authorize device response

    Args:
        BaseModel (class): Base model class
    """

    data: AuthorizeDeviceResponseData


class GetTokensResponseData(BaseModel):
    """Get tokens response data

    Args:
        BaseModel (class): Base model class
    """

    accessToken: str
    refreshToken: str
    expiresIn: int
    refreshExpiresIn: int


class GetTokensResponse(BaseModel):
    """Get tokens response

    Args:
        BaseModel (class): Base model class
    """

    data: GetTokensResponseData


class GetNewAccessTokenPayload(BaseModel):
    """Get new access token payload

    Args:
        BaseModel (class): Base model class
    """

    refreshToken: str


class GetNewAccessTokenResponseData(BaseModel):
    """Get new access token response data

    Args:
        BaseModel (class): Base model class
    """

    accessToken: str
    expiresIn: int


class GetNewAccessTokenResponse(BaseModel):
    """Get new access token response

    Args:
        BaseModel (class): Base model class
    """

    data: GetNewAccessTokenResponseData

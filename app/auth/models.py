from pydantic import BaseModel

class GetTokensPayload(BaseModel):
    deviceCode: str

class AuthorizeDeviceResponseData(BaseModel):
    deviceCode: str
    userCode: str
    expiresIn: int
    interval: int
    verificationURI: str

class AuthorizeDeviceResponse(BaseModel):
    data: AuthorizeDeviceResponseData

class GetTokensResponseData(BaseModel):
    accessToken: str
    refreshToken: str
    expiresIn: int
    refreshExpiresIn: int

class GetTokensResponse(BaseModel):
    data: GetTokensResponseData

"""Auth API constants
"""

TAGS = ["auth"]

# Operation Ids
AUTHORIZE_DEVICE_OPERATION_ID = "authorizeDevice"
GET_AUTH_TOKENS_OPERATION_ID = "getAuthTokens"
GET_NEW_ACCESS_TOKEN_OPERATION_ID = "getNewAccessToken"


# Route Internal paths
DEVICE_ROUTE_PATH = "/device"
TOKENS_ROUTE_PATH = "/tokens"
TOKEN_REFRESH_PATH = "/token/refresh"

# External paths
AUTH_DEVICE_EXTERNAL_PATH = "/api/v1/auth/device"
AUTH_TOKENS_EXTERNAL_PATH = "/api/v1/auth/tokens"
AUTH_TOKEN_VALIDATE_EXTERNAL_PATH = "/api/v1/auth/token/validate"
AUTH_TOKEN_REFRESH_EXTERNAL_PATH = "/api/v1/auth/token/refresh"

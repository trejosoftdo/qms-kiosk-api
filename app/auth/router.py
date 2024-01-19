from fastapi import APIRouter, Header
from . import handlers
from . import models
from . import constants


router = APIRouter()


@router.get(
    "/device",
    tags = constants.TAGS,
    operation_id = constants.AUTHORIZE_DEVICE_OPERATION_ID,
    response_model = models.AuthorizeDeviceResponse
)
def authorize_device(application: str = Header(..., convert_underscores = False)) -> models.AuthorizeDeviceResponse:
    """Authorize a device to an application in context

    Args:
        application (str, optional): The application in context. Defaults to Header(..., convert_underscores = False).

    Returns:
        models.AuthorizeDeviceResponse: Authorization information such as deviceCode, and userCode.
    """
    return handlers.authorize_device(application)


@router.post(
    "/tokens",
    tags = constants.TAGS,
    operation_id = constants.GET_AUTH_TOKENS_OPERATION_ID,
    response_model = models.GetTokensResponse
)
async def get_auth_tokens(item: models.GetTokensPayload, application: str = Header(..., convert_underscores = False)) -> models.GetTokensResponse:
    """Gets the authorization tokens for the given device code and application in context
    
    Args:
        application (str, optional): The application in context. Defaults to Header(..., convert_underscores = False).
        item (models.GetTokensPayload): The required payload

    Returns:
        models.GetTokensResponse: The authorization tokens information
    """
    return handlers.get_auth_tokens(application, item.deviceCode)


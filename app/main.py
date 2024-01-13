from fastapi import FastAPI
from . import auth_handlers
from . import models

app = FastAPI()


@app.get("/auth/{realm}/device", tags=["auth"], response_model = models.AuthorizeDeviceResponse)
def authorize_device(realm: str) -> models.AuthorizeDeviceResponse:
    """Authorize a device to a realm in context

    Args:
        realm (str): The realm in context

    Returns:
        models.AuthorizeDeviceResponse: Authorization information such as deviceCode, and userCode.
    """
    return auth_handlers.authorize_device(realm)


@app.post("/auth/{realm}/tokens", tags=["auth"], response_model = models.GetTokensResponse)
async def get_auth_tokens(realm: str, item: models.GetTokensPayload) -> models.GetTokensResponse:
    """Gets the authorization tokens for the given device code and realm in context
    
    Args:
        realm (str): The realm in context
        item (models.GetTokensPayload): The required payload

    Returns:
        models.GetTokensResponse: The authorization tokens information
    """
    return auth_handlers.get_auth_tokens(realm, item.deviceCode)

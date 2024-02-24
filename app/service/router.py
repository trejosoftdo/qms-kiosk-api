"""Service API router
"""

from fastapi import APIRouter, Depends, Header
from .. import constants
from .constants import TAGS, CREATE_SERVICE_TURN_OPERATION_ID, SERVICE_TURNS_PATH
from .. import helpers
from . import handlers
from . import models

router = APIRouter()


@router.post(
    SERVICE_TURNS_PATH,
    dependencies=[Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE))],
    tags=TAGS,
    operation_id=CREATE_SERVICE_TURN_OPERATION_ID,
    response_model=models.CreateServiceTurnResponse,
)
def create_service_turn(
    service_id: int,
    payload: models.CreateServiceTurnPayload,
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service

    Args:
        service_id (int): ID of service to create a turn from
        payload (models.CreateServiceTurnPayload): The required payload
        application (str, optional): The application in context.
        authorization (str, optional): The access token for the user in context

    Returns:
        models.CreateServiceTurnResponse: Basic information of the created service turn
    """
    request = models.CreateServiceTurnRequest(
        headers=models.CommonHeaders(
            application=application, authorization=authorization
        ),
        payload=payload,
        serviceId=service_id,
    )
    return handlers.create_service_turn(request)

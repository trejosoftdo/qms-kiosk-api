from fastapi import APIRouter, Header
from . import handlers
from . import models

router = APIRouter()

@router.post("/{serviceId}/serviceturns", tags=["services"], operation_id = "createServiceTurn", response_model = models.CreateServiceTurnResponse)
async def create_service_turn(
    serviceId: int,
    item: models.CreateServiceTurnPayload,
    application: str = Header(..., convert_underscores = False)
) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service
    
    Args:
        serviceId (int): ID of service to create a turn from
        item (models.CreateServiceTurnPayload): The required payload
        application (str, optional): The application in context.
        
    Returns:
        models.CreateServiceTurnResponse: Basic information of the created service turn
    """
    return handlers.create_service_turn(application, serviceId, item)

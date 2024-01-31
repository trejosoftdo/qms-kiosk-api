from . import models
from . import api
from . import mappers

def create_service_turn(request: models.CreateServiceTurnRequest) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service
    
    Args:
        request (models.CreateServiceTurnRequest): Request for creating the service turn

    Returns:
        models.CreateServiceTurnResponse: Created service turn
    """
    response = api.create_service_turn(request)
    return mappers.map_service_turn(response.json())

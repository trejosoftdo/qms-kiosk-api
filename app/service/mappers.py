"""Service API mappers
"""

from . import models

def map_service_turn(data: dict) -> models.CreateServiceTurnResponse:
    """Maps the service turn response from data
    
    Args:
        data (dict): response data

    Returns:
        models.CreateServiceTurnResponse: Created service turn data
    """
    return models.CreateServiceTurnResponse(
      id = data.get('id'),
      customerName = data.get('customerName'),
      ticketNumber = data.get('ticketNumber'),
      peopleInQueue = data.get('peopleInQueue'),
    )

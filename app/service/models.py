"""Service API models
"""

from pydantic import BaseModel


class CreateServiceTurnPayload(BaseModel):
    """Create service turn payload

    Args:
        BaseModel (class): Base model class
    """

    customerName: str


class CommonHeaders(BaseModel):
    """Common headers data

    Args:
        BaseModel (class): Base model class
    """

    authorization: str
    application: str


class CreateServiceTurnRequest(BaseModel):
    """Create service turn request

    Args:
        BaseModel (class): Base model class
    """

    serviceId: int
    headers: CommonHeaders
    payload: CreateServiceTurnPayload


class CreateServiceTurnResponse(BaseModel):
    """Create Service turn response

    Args:
        BaseModel (class): Base model class
    """

    id: int
    customerName: str
    ticketNumber: str
    peopleInQueue: int

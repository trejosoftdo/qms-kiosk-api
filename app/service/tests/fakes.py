"""Services fakes"""

from pydantic_factories import ModelFactory
from app.service.models import (
    CreateServiceTurnResponse,
    CreateServiceTurnPayload,
    CreateServiceTurnRequest,
)


class CreateServiceTurnResponseFactory(ModelFactory):
    """CreateServiceTurnResponse factory"""

    __model__ = CreateServiceTurnResponse


class CreateServiceTurnPayloadFactory(ModelFactory):
    """CreateServiceTurnPayload factory"""

    __model__ = CreateServiceTurnPayload


class CreateServiceTurnRequestFactory(ModelFactory):
    """CreateServiceTurnRequest factory"""

    __model__ = CreateServiceTurnRequest

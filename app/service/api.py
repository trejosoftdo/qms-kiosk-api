"""Service API helpers
"""

import requests
from .. import environment
from .. import constants
from . import models
from .constants import SERVICES_EXTERNAL_PATH, TURNS_EXTERNAL_PATH


def get_common_headers() -> dict:
    """Gets the common headers

    Returns:
        dict: common headers data
    """
    return {
        "Content-Type": "application/json",
        "api_key": environment.core_api_key,
    }


def create_service_turn(request: models.CreateServiceTurnRequest) -> requests.Response:
    """Creates a service turn for the given service

    Args:
        request (models.CreateServiceTurnRequest): Request to create the service turn

    Returns:
        requests.Response: The response from the core api.
    """
    url = f"{environment.core_api_base_url}{SERVICES_EXTERNAL_PATH}{request.serviceId}{TURNS_EXTERNAL_PATH}"
    headers = {
        **get_common_headers(),
        "application": request.headers.application,
        "authorization": request.headers.authorization,
    }
    payload = {
        "customerName": request.payload.customerName,
    }
    return requests.post(url, headers=headers, json=payload, timeout=constants.TIMEOUT)

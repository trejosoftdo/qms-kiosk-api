"""Category API helpers
"""

import requests
from .. import environment
from .. import constants
from . import models
from .constants import CATEGORIES_EXTERNAL_PATH, SERVICES_EXTERNAL_PATH


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.core_api_key,
    }


def get_categories(req: models.GetCategoriesRequest) -> requests.Response:
    """Gets the list of available categories for the application in context

    Args:
        req (models.GetCategoriesRequest): Request to get categories

    Returns:
        requests.Response: The response from the core api.
    """
    categories_url = f"{environment.core_api_base_url}{CATEGORIES_EXTERNAL_PATH}"
    params = {
        "active": req.params.active,
        "offset": req.params.offset,
        "limit": req.params.limit,
    }
    headers = {
        **get_common_headers(),
        "application": req.headers.application,
        "authorization": req.headers.authorization,
    }
    return requests.get(
        categories_url, headers=headers, params=params, timeout=constants.TIMEOUT
    )


def get_category_services(
    req: models.GetCategoryServicesRequest,
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        req (models.GetCategoryServicesRequest): Request to get the services of a category

    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    services_url = (
        f"{environment.core_api_base_url}{CATEGORIES_EXTERNAL_PATH}{req.categoryId}{SERVICES_EXTERNAL_PATH}"
    )
    params = {
        "active": req.params.active,
        "offset": req.params.offset,
        "limit": req.params.limit,
    }
    headers = {
        **get_common_headers(),
        "application": req.headers.application,
        "authorization": req.headers.authorization,
    }
    return requests.get(
        services_url, headers=headers, params=params, timeout=constants.TIMEOUT
    )

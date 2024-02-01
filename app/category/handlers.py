"""Category API handlers
"""

from . import models
from . import api
from . import mappers


def get_categories(req: models.GetCategoriesRequest) -> models.CategoriesListResponse:
    """Get list of categories

    Args:
        req (str): The request to get the list of categories

    Returns:
        models.CategoriesListResponse: List of categories
    """
    response = api.get_categories(req)
    categories = response.json()
    return list(map(mappers.map_category, categories))


def get_category_services(
    req: models.GetCategoryServicesRequest,
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        req (str): The request to get the list of services for a category

    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    response = api.get_category_services(req)
    category_services = response.json()
    return list(map(mappers.map_category_service, category_services))

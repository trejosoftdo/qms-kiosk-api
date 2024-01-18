from fastapi import APIRouter, Header
from . import handlers
from . import models

router = APIRouter()

@router.get("/", tags=["categories"], response_model = models.CategoriesListResponse)
def get_categories(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    application: str = Header(..., convert_underscores = False)
) -> models.CategoriesListResponse:
    """Gets a list of categories for the application in context

    Args:
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The number of items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The number of items to return. Defaults to 10.
        application (str, optional): The application in context.

    Returns:
        models.CategoriesListResponse: The list of categories
    """
    return handlers.get_categories(
        application,
        active,
        offset,
        limit
    )

@router.get("/{categoryId}/services", tags=["categories"], response_model = models.CategoryServicesListResponse)
def get_category_services(
    categoryId: int,
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    application: str = Header(..., convert_underscores = False)
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        categoryId (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The number of items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The number of items to return. Defaults to 10.
        application (str, optional): The application in context.

    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    return handlers.get_category_services(
        application,
        categoryId,
        active,
        offset,
        limit
    )

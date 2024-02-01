"""Category API router
"""

from fastapi import APIRouter, Depends, Header
from .. import helpers
from .. import constants
from .constants import (
    TAGS,
    GET_CATEGORIES_OPERATION_ID,
    GET_CATEGORY_SERVICES_OPERATION_ID,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(helpers.validate_token(constants.READ_CATEGORIES_SCOPE))],
    tags=TAGS,
    operation_id=GET_CATEGORIES_OPERATION_ID,
    response_model=models.CategoriesListResponse,
)
def get_categories(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
) -> models.CategoriesListResponse:
    """Gets a list of categories for the application in context

    Args:
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The items to return. Defaults to 10.
        application (str, optional): The application in context.
        authorization (str, optional): The access token for the user in context

    Returns:
        models.CategoriesListResponse: The list of categories
    """
    request = models.GetCategoriesRequest(
        headers=models.CommonHeaders(
            application=application, authorization=authorization
        ),
        params=models.ListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_categories(request)


@router.get(
    "/{category_id}/services",
    dependencies=[Depends(helpers.validate_token(constants.READ_SERVICES_SCOPE))],
    tags=TAGS,
    operation_id=GET_CATEGORY_SERVICES_OPERATION_ID,
    response_model=models.CategoryServicesListResponse,
)
def get_category_services(  # pylint: disable=R0913
    category_id: int,
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        category_id (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The items to return. Defaults to 10.
        application (str, optional): The application in context.
        authorization (str, optional): The access token for the user in context

    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    request = models.GetCategoryServicesRequest(
        categoryId=category_id,
        headers=models.CommonHeaders(
            application=application, authorization=authorization
        ),
        params=models.ListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_category_services(request)

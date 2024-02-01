"""Category API models
"""

from typing import List
from pydantic import BaseModel


class Status(BaseModel):
    """Status data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    type: str
    isActive: bool


class Category(BaseModel):
    """Category data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    iconUrl: str
    status: Status
    isActive: bool


class CategoryService(BaseModel):
    """Category service data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    prefix: str
    iconUrl: str
    status: Status
    category: Category
    isActive: bool


class ListParams(BaseModel):
    """List params data

    Args:
        BaseModel (class): Base model class
    """

    active: bool
    offset: int
    limit: int


class CommonHeaders(BaseModel):
    """Common headers data

    Args:
        BaseModel (class): Base model class
    """

    authorization: str
    application: str


class GetCategoriesRequest(BaseModel):
    """Get categories request

    Args:
        BaseModel (class): Base model class
    """

    headers: CommonHeaders
    params: ListParams


class GetCategoryServicesRequest(BaseModel):
    """Get category services request

    Args:
        BaseModel (class): Base model class
    """

    headers: CommonHeaders
    params: ListParams
    categoryId: int


CategoriesListResponse = List[Category]
CategoryServicesListResponse = List[CategoryService]

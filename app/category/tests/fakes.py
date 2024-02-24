"""Category fakes"""

from pydantic_factories import ModelFactory
from app.category.models import (
    GetCategoriesRequest,
    GetCategoryServicesRequest,
    Category,
    CategoryService,
)


class GetCategoriesRequestFactory(ModelFactory):
    """GetCategoriesRequest factory"""

    __model__ = GetCategoriesRequest


class GetCategoryServicesRequestFactory(ModelFactory):
    """GetCategoryServicesRequest factory"""

    __model__ = GetCategoryServicesRequest


class CategoryFactory(ModelFactory):
    """Category factory"""

    __model__ = Category


class CategoryServiceFactory(ModelFactory):
    """CategoryService factory"""

    __model__ = CategoryService

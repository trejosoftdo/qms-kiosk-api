"""API Handlers tests
"""

import unittest
from unittest.mock import Mock, patch
from fastapi import status
from requests import Response
from app.category.tests.fakes import (
    GetCategoriesRequestFactory,
    CategoryFactory,
    CategoryServiceFactory,
    GetCategoryServicesRequestFactory,
)
from app.category.handlers import get_categories, get_category_services


class HandlersTest(unittest.TestCase):
    """Category Handlers functions tests"""

    def setUp(self):
        self.realm = "test-realm"
        self.access_token = "test-access-token"

    @patch("app.category.mappers.map_category")
    @patch("app.category.api.get_categories")
    def test_get_categories(self, get_categories_mock, map_category_mock):
        """get_categories: It gets a list of categories"""
        json_data = [{"id": 1234}]
        get_categories_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value=json_data),
        )
        map_category_mock.return_value = CategoryFactory.build()
        request = GetCategoriesRequestFactory.build()
        response = get_categories(request)
        self.assertEqual(response, [map_category_mock.return_value])
        get_categories_mock.assert_called_with(request)
        map_category_mock.assert_called_with(json_data[0])

    @patch("app.category.mappers.map_category_service")
    @patch("app.category.api.get_category_services")
    def test_get_category_services(self, get_category_services_mock, map_category_service_mock):
        """get_category_services: It gets a list of category services"""
        json_data = [{"id": 1234}]
        get_category_services_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value=json_data),
        )
        map_category_service_mock.return_value = CategoryServiceFactory.build()
        request = GetCategoryServicesRequestFactory.build()
        response = get_category_services(request)
        self.assertEqual(response, [map_category_service_mock.return_value])
        get_category_services_mock.assert_called_with(request)
        map_category_service_mock.assert_called_with(json_data[0])


if __name__ == "__main__":
    unittest.main()

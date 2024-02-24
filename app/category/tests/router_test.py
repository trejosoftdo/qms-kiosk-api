"""API Router tests
"""

import unittest
from unittest.mock import Mock, patch
from requests import Response
from fastapi import status
from fastapi.testclient import TestClient
from app import main, constants
from app.category.constants import CATEGORIES_PATH
from app.category.tests.fakes import CategoryFactory, CategoryServiceFactory


# pylint: disable=R0801

class RouterTest(unittest.TestCase):
    """Category Router functions tests"""

    def setUp(self):
        self.client = TestClient(main.app)
        self.application = "test-application"
        self.authorization = "Bearer test-token"
        self.headers = {
            "application": self.application,
            "authorization": self.authorization,
        }
        self.valid_token_response = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(
                return_value={
                    "data": {
                        "isValid": True,
                        "isAuthorized": True,
                    }
                }
            ),
        )

    @patch("app.auth.api.validate_token")
    @patch("app.category.handlers.get_categories")
    def test_get_categories(self, get_categories_mock, validate_token_mock):
        """get_categories: It should be able to list categories"""
        validate_token_mock.return_value = self.valid_token_response

        get_categories_mock.return_value = [CategoryFactory.build()]
        response = self.client.get(
            f"{constants.CATEGORIES_ROUTE_PREFIX}{CATEGORIES_PATH}?offset=1&limit=2",
            headers=self.headers,
        )
        self.assertEqual(response.json(), get_categories_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        get_categories_mock.assert_called()

    @patch("app.auth.api.validate_token")
    @patch("app.category.handlers.get_category_services")
    def test_get_category_services(
        self, get_category_services_mock, validate_token_mock
    ):
        """get_category_services: It should be able to list category services"""
        validate_token_mock.return_value = self.valid_token_response

        get_category_services_mock.return_value = [CategoryServiceFactory.build()]
        response = self.client.get(
            f"{constants.CATEGORIES_ROUTE_PREFIX}/1/services?offset=1&limit=2",
            headers=self.headers,
        )
        self.assertEqual(response.json(), get_category_services_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        get_category_services_mock.assert_called()


if __name__ == "__main__":
    unittest.main()

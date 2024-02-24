"""Helpers tests
"""

import unittest
from unittest.mock import Mock, patch
from app.category.tests.fakes import (
    GetCategoriesRequestFactory,
    GetCategoryServicesRequestFactory,
)
from app.constants import (
    TIMEOUT,
    CONTENT_TYPE_JSON,
)
from app.category.api import get_categories, get_category_services
from app.category.constants import CATEGORIES_EXTERNAL_PATH, SERVICES_EXTERNAL_PATH


BASE_URL = "http://base-url.test"
TEST_API_KEY = "test-api-key"

mock_environment = Mock(
    core_api_base_url=BASE_URL,
    core_api_key=TEST_API_KEY,
)


class CategoryAPITest(unittest.TestCase):
    """Category API functions tests"""

    def setUp(self):
        self.base_path = BASE_URL
        self.common_headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "api_key": mock_environment.core_api_key,
        }
        self.application = "test-application"
        self.authorization = "Bearer test-token"

    @patch("app.category.api.requests.get")
    @patch(
        "app.category.api.environment",
        mock_environment,
    )
    def test_get_categories(self, get_mock):
        """get_categories: It can list categories"""
        get_mock.return_value = Mock(status_code=200)
        request = GetCategoriesRequestFactory.build()
        response = get_categories(request)
        self.assertEqual(response, get_mock.return_value)
        get_mock.assert_called_with(
            f"{self.base_path}{CATEGORIES_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": request.headers.application,
                "authorization": request.headers.authorization,
            },
            params={
                "active": request.params.active,
                "offset": request.params.offset,
                "limit": request.params.limit,
            },
            timeout=TIMEOUT,
        )

    @patch("app.category.api.requests.get")
    @patch(
        "app.category.api.environment",
        mock_environment,
    )
    def test_get_category_services(self, get_mock):
        """get_category_services: It can list category services"""
        get_mock.return_value = Mock(status_code=200)
        request = GetCategoryServicesRequestFactory.build()
        response = get_category_services(request)
        self.assertEqual(response, get_mock.return_value)
        base_path = f"{self.base_path}{CATEGORIES_EXTERNAL_PATH}{request.categoryId}"
        get_mock.assert_called_with(
            f"{base_path}{SERVICES_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": request.headers.application,
                "authorization": request.headers.authorization,
            },
            params={
                "active": request.params.active,
                "offset": request.params.offset,
                "limit": request.params.limit,
            },
            timeout=TIMEOUT,
        )


if __name__ == "__main__":
    unittest.main()

"""Helpers tests
"""

import unittest
from unittest.mock import Mock, patch
from fakes import CreateServiceTurnRequestFactory
from app.constants import (
    TIMEOUT,
    CONTENT_TYPE_JSON,
)
from app.service.api import create_service_turn
from app.service.constants import SERVICES_EXTERNAL_PATH, TURNS_EXTERNAL_PATH


BASE_URL = "http://base-url.test"
TEST_API_KEY = "test-api-key"

mock_environment = Mock(
    core_api_base_url=BASE_URL,
    core_api_key=TEST_API_KEY,
)


class ServiceAPITest(unittest.TestCase):
    """Service API functions tests"""

    def setUp(self):
        self.base_path = BASE_URL
        self.common_headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "api_key": mock_environment.core_api_key,
        }
        self.application = "test-application"
        self.authorization = "Bearer test-token"

    @patch("app.service.api.requests.post")
    @patch(
        "app.service.api.environment",
        mock_environment,
    )
    def test_create_service_turn(self, post_mock):
        """auth_device: It can create a service turn for the given data"""
        post_mock.return_value = Mock(status_code=200)
        request = CreateServiceTurnRequestFactory.build()
        response = create_service_turn(request)
        self.assertEqual(response, post_mock.return_value)
        post_mock.assert_called_with(
            f"{self.base_path}{SERVICES_EXTERNAL_PATH}{request.serviceId}{TURNS_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": request.headers.application,
                "authorization": request.headers.authorization,
            },
            json={"customerName": request.payload.customerName},
            timeout=TIMEOUT,
        )


if __name__ == "__main__":
    unittest.main()

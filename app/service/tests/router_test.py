"""API Router tests
"""

import unittest
from unittest.mock import Mock, patch
from requests import Response
from fastapi import status
from fastapi.testclient import TestClient
from app import main, constants
from fakes import CreateServiceTurnResponseFactory, CreateServiceTurnPayloadFactory


class RouterTest(unittest.TestCase):
    """Service Router functions tests"""

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
    @patch("app.service.handlers.create_service_turn")
    def test_create_service_turn(self, create_service_turn_mock, validate_token_mock):
        """create_service_turn: It should be able to create a service turn for a customer"""
        validate_token_mock.return_value = self.valid_token_response

        create_service_turn_mock.return_value = CreateServiceTurnResponseFactory.build()
        payload = CreateServiceTurnPayloadFactory.build()
        response = self.client.post(
            f"{constants.SERVICES_ROUTE_PREFIX}/1/serviceturns",
            headers=self.headers,
            json=payload.dict(),
        )
        self.assertEqual(response.json(), create_service_turn_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        create_service_turn_mock.assert_called()


if __name__ == "__main__":
    unittest.main()

"""API Handlers tests
"""

import unittest
from unittest.mock import Mock, patch
from fastapi import status
from requests import Response
from app.service.tests.fakes import (
    CreateServiceTurnRequestFactory,
    CreateServiceTurnResponseFactory,
)
from app.service.handlers import create_service_turn


class HandlersTest(unittest.TestCase):
    """Service Handlers functions tests"""

    def setUp(self):
        self.realm = "test-realm"
        self.access_token = "test-access-token"

    @patch("app.service.mappers.map_service_turn")
    @patch("app.service.api.create_service_turn")
    def test_create_service_turn(self, create_service_turn_mock, map_service_turn_mock):
        """create_service_turn: It can create a service turn for a customer"""
        json_data = {"customerName": "test-customer"}
        create_service_turn_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value={"data": json_data}),
        )
        map_service_turn_mock.return_value = CreateServiceTurnResponseFactory.build()
        request = CreateServiceTurnRequestFactory.build()
        response = create_service_turn(request)
        self.assertEqual(response, map_service_turn_mock.return_value)
        create_service_turn_mock.assert_called_with(request)
        map_service_turn_mock.assert_called_with({"data": json_data})


if __name__ == "__main__":
    unittest.main()

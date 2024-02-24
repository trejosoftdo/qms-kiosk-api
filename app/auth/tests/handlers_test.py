"""API Handlers tests
"""

import unittest
from unittest.mock import Mock, patch
from fastapi import status
from requests import Response
from app.auth.handlers import (
    authorize_device,
    get_auth_tokens,
    get_new_access_token,
)
from app.auth import models


class HandlersTest(unittest.TestCase):
    """Auth Handlers functions tests"""

    def setUp(self):
        self.realm = "test-realm"
        self.access_token = "test-access-token"

    @patch("app.helpers.handle_error_response")
    @patch("app.auth.api.auth_device")
    def test_authorize_device(self, auth_device_mock, handle_error_response_mock):
        """authorize_device: It can authorize a device"""
        json_data = {
            "deviceCode": "test-device-code",
            "userCode": "test-user-code",
            "expiresIn": 1800,
            "interval": 10,
            "verificationURI": "http://test-ver.test",
        }
        auth_device_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value={ "data": json_data }),
        )
        response = authorize_device(self.realm)

        self.assertEqual(response.data.deviceCode, json_data["deviceCode"])
        self.assertEqual(response.data.userCode, json_data["userCode"])
        self.assertEqual(response.data.expiresIn, json_data["expiresIn"])
        self.assertEqual(response.data.interval, json_data["interval"])
        self.assertEqual(
            response.data.verificationURI, json_data["verificationURI"]
        )
        auth_device_mock.assert_called_with(self.realm)
        handle_error_response_mock.assert_called_with(auth_device_mock.return_value)

    @patch("app.helpers.handle_error_response")
    @patch("app.auth.api.get_auth_tokens")
    def test_get_auth_tokens(self, get_auth_tokens_mock, handle_error_response_mock):
        """get_auth_tokens: It can retrieve access tokens"""
        json_data = {
            "accessToken": self.access_token,
            "refreshToken": "test-refresh-token",
            "expiresIn": 1800,
            "refreshExpiresIn": 3600,
        }
        get_auth_tokens_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value={ "data": json_data }),
        )
        payload = models.GetTokensPayload(
            deviceCode="test-device-code",
        )
        response = get_auth_tokens(self.realm, payload)
        self.assertEqual(response.data.accessToken, json_data["accessToken"])
        self.assertEqual(response.data.refreshToken, json_data["refreshToken"])
        self.assertEqual(response.data.expiresIn, json_data["expiresIn"])
        self.assertEqual(
            response.data.refreshExpiresIn, json_data["refreshExpiresIn"]
        )
        get_auth_tokens_mock.assert_called_with(self.realm, payload)
        handle_error_response_mock.assert_called_with(get_auth_tokens_mock.return_value)

    @patch("app.helpers.handle_error_response")
    @patch("app.auth.api.get_new_access_token")
    def test_get_new_access_token(
        self, get_new_access_token_mock, handle_error_response_mock
    ):
        """get_new_access_token: It can get a new access token"""
        json_data = {
            "accessToken": self.access_token,
            "expiresIn": 1800,
        }
        get_new_access_token_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value={ "data": json_data }),
        )
        payload = models.GetNewAccessTokenPayload(
            refreshToken="test-refresh-token",
        )
        response = get_new_access_token(self.realm, payload)

        self.assertEqual(response.data.accessToken, json_data["accessToken"])
        self.assertEqual(response.data.expiresIn, json_data["expiresIn"])

        get_new_access_token_mock.assert_called_with(self.realm, payload)
        handle_error_response_mock.assert_called_with(
            get_new_access_token_mock.return_value
        )


if __name__ == "__main__":
    unittest.main()

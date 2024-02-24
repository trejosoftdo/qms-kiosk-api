"""API Router tests
"""

import unittest
from unittest.mock import Mock, patch
from requests import Response
from fastapi import status
from fastapi.testclient import TestClient
from app import main, constants
from app.auth import models
from app.auth.constants import DEVICE_ROUTE_PATH, TOKENS_ROUTE_PATH, TOKEN_REFRESH_PATH


class RouterTest(unittest.TestCase):
    """Auth Router functions tests"""

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
    @patch("app.auth.handlers.authorize_device")
    def test_authorize_device(self, auth_device_mock, validate_token_mock):
        """authorize_device: It can authorize a device"""
        validate_token_mock.return_value = self.valid_token_response

        auth_device_mock.return_value = models.AuthorizeDeviceResponse(
            data=models.AuthorizeDeviceResponseData(
                deviceCode="test-device-code",
                userCode="test-user-code",
                expiresIn=1800,
                interval=10,
                verificationURI="http://test-ver.test",
            ),
        )

        response = self.client.get(
            f"{constants.AUTH_ROUTE_PREFIX}{DEVICE_ROUTE_PATH}",
            headers=self.headers,
        )
        self.assertEqual(response.json(), auth_device_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        auth_device_mock.assert_called_with(self.application)

    @patch("app.auth.api.validate_token")
    @patch("app.auth.handlers.get_auth_tokens")
    def test_get_auth_tokens(self, get_auth_tokens_mock, validate_token_mock):
        """get_auth_tokens: It can get device auth tokens"""
        validate_token_mock.return_value = self.valid_token_response

        get_auth_tokens_mock.return_value = models.GetTokensResponse(
            data=models.GetTokensResponseData(
                accessToken="test-access-token",
                refreshToken="test-refresh-token",
                expiresIn=1800,
                refreshExpiresIn=36000,
            ),
        )
        payload = models.GetTokensPayload(
            clientId="test-client-id",
            clientSecret="test-client-secret",
            deviceCode="test-device-code",
        )
        response = self.client.post(
            f"{constants.AUTH_ROUTE_PREFIX}{TOKENS_ROUTE_PATH}",
            headers=self.headers,
            json=payload.dict(),
        )
        self.assertEqual(response.json(), get_auth_tokens_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        get_auth_tokens_mock.assert_called_with(self.application, payload.deviceCode)

    @patch("app.auth.api.validate_token")
    @patch("app.auth.handlers.get_new_access_token")
    def test_get_new_access_token(self, get_new_access_token_mock, validate_token_mock):
        """get_new_access_token: It can get refresh a token"""
        validate_token_mock.return_value = self.valid_token_response

        get_new_access_token_mock.return_value = models.GetNewAccessTokenResponse(
            data=models.GetNewAccessTokenResponseData(
                accessToken="test-access-token",
                expiresIn=1800,
            ),
        )
        payload = models.GetNewAccessTokenPayload(
            refreshToken="test-refresh-token",
        )
        response = self.client.post(
            f"{constants.AUTH_ROUTE_PREFIX}{TOKEN_REFRESH_PATH}",
            headers=self.headers,
            json=payload.dict(),
        )
        self.assertEqual(response.json(), get_new_access_token_mock.return_value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        get_new_access_token_mock.assert_called_with(
            self.application, payload.refreshToken
        )


if __name__ == "__main__":
    unittest.main()

"""Helpers tests
"""

import unittest
from unittest.mock import Mock, patch
from app.constants import (
    TIMEOUT,
    CONTENT_TYPE_JSON,
    DEVICE_TOKEN_SCOPES,
)
from app.auth.api import (
    auth_device,
    get_auth_tokens,
    validate_token,
    get_new_access_token,
)
from app.auth import constants as paths


BASE_URL = "http://base-url.test"
TEST_CLIENT_ID = "test-app-client-id"
TEST_CLIENT_SECRET = "test-app-client-secret"
TEST_API_KEY = "test-api-key"

mock_environment = Mock(
    auth_api_base_url=BASE_URL,
    app_client_id=TEST_CLIENT_ID,
    app_client_secret=TEST_CLIENT_SECRET,
    iam_api_key=TEST_API_KEY,
)


class AuthAPITest(unittest.TestCase):
    """Auth API functions tests"""

    def setUp(self):
        self.realm = "test-realm"
        self.base_path = BASE_URL
        self.common_headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "api_key": mock_environment.iam_api_key,
        }
        self.authorization = "Bearer test-token"

    @patch("app.auth.api.requests.post")
    @patch(
        "app.auth.api.environment",
        mock_environment,
    )
    def test_auth_device(self, post_mock):
        """auth_device: It can authorize a device against the external auth service as expected"""
        post_mock.return_value = Mock(status_code=200)
        response = auth_device(self.realm)
        self.assertEqual(response, post_mock.return_value)
        post_mock.assert_called_with(
            f"{self.base_path}{paths.AUTH_DEVICE_EXTERNAL_PATH}",
            headers={**self.common_headers, "application": self.realm},
            json={
                "clientId": mock_environment.app_client_id,
                "clientSecret": mock_environment.app_client_secret,
                "scope": " ".join(DEVICE_TOKEN_SCOPES),
            },
            timeout=TIMEOUT,
        )

    @patch("app.auth.api.requests.post")
    @patch(
        "app.auth.api.environment",
        mock_environment,
    )
    def test_get_auth_tokens(self, post_mock):
        """get_auth_tokens: It can get auth tokens from the external auth service as expected"""
        post_mock.return_value = Mock(status_code=200)
        device_code = "test-device-code"
        response = get_auth_tokens(self.realm, device_code)
        self.assertEqual(response, post_mock.return_value)
        post_mock.assert_called_with(
            f"{self.base_path}{paths.AUTH_TOKENS_EXTERNAL_PATH}",
            headers={**self.common_headers, "application": self.realm},
            json={
                "deviceCode": device_code,
                "clientId": mock_environment.app_client_id,
                "clientSecret": mock_environment.app_client_secret,
            },
            timeout=TIMEOUT,
        )

    @patch("app.auth.api.requests.post")
    @patch(
        "app.auth.api.environment",
        mock_environment,
    )
    def test_validate_token(self, post_mock):
        """validate_token: It can get token info from the auth service as expected"""
        post_mock.return_value = Mock(status_code=200)
        test_scope = "test-scope"
        response = validate_token(self.realm, self.authorization, test_scope)
        self.assertEqual(response, post_mock.return_value)
        post_mock.assert_called_with(
            f"{self.base_path}{paths.AUTH_TOKEN_VALIDATE_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": self.realm,
                "authorization": self.authorization,
            },
            json={
                "expectedScope": test_scope,
                "clientId": mock_environment.app_client_id,
                "clientSecret": mock_environment.app_client_secret,
            },
            timeout=TIMEOUT,
        )

    @patch("app.auth.api.requests.post")
    @patch(
        "app.auth.api.environment",
        mock_environment,
    )
    def test_get_new_access_token(self, post_mock):
        """get_new_access_token: It can get a new token from the auth service as expected"""
        post_mock.return_value = Mock(status_code=200)
        test_refresh_token = "test-refresh-token"
        response = get_new_access_token(self.realm, test_refresh_token)
        self.assertEqual(response, post_mock.return_value)
        post_mock.assert_called_with(
            f"{self.base_path}{paths.AUTH_TOKEN_REFRESH_EXTERNAL_PATH}",
            headers={
                **self.common_headers,
                "application": self.realm,
            },
            json={
                "refreshToken": test_refresh_token,
                "clientId": mock_environment.app_client_id,
                "clientSecret": mock_environment.app_client_secret,
            },
            timeout=TIMEOUT,
        )


if __name__ == "__main__":
    unittest.main()

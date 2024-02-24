"""Helpers tests
"""

import unittest
from unittest.mock import Mock, patch
from fastapi import status, HTTPException
from requests import Response
from app.helpers import handle_error_response, validate_token


class HelpersTest(unittest.TestCase):
    """Helpers functions tests"""

    def setUp(self):
        self.data = {"title": "Test title"}
        self.authorization = "Bearer test-token"
        self.application = "test-application"
        self.scope = "test-scope"

    def test_handle_error_response_not_error(self):
        """handle_error_response: It does not fail when the status code is not an error"""
        response_mock = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(return_value=self.data),
        )
        self.assertIsNone(handle_error_response(response_mock))

    def test_handle_error_response_validation_error(self):
        """handle_error_response: it returns a validation error when the error status is 400"""
        response_mock = Mock(
            spec=Response,
            status_code=status.HTTP_400_BAD_REQUEST,
            json=Mock(return_value=self.data),
        )
        self.assertRaises(HTTPException, handle_error_response, response_mock)

    def test_handle_error_response_unexpected_error(self):
        """handle_error_response: it returns an internal error when status is greater than 400"""
        response_mock = Mock(
            spec=Response,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            json=Mock(return_value=self.data),
        )
        self.assertRaises(HTTPException, handle_error_response, response_mock)

    @patch("app.auth.api.validate_token")
    def test_validate_token_valid_and_authorized(self, validate_token_mock):
        """validate_token: It does not fail when token is valid and authorized"""
        validate_token_mock.return_value = Mock(
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
        validator = validate_token(self.scope)

        self.assertIsNone(validator(self.application, self.authorization))
        validate_token_mock.assert_called_with(
            self.application, self.authorization, self.scope
        )

    @patch("app.auth.api.validate_token")
    def test_validate_token_valid_but_unauthorized(self, validate_token_mock):
        """validate_token: It fails when token is valid but unauthorized"""
        validate_token_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(
                return_value={
                    "data": {
                        "isValid": True,
                        "isAuthorized": False,
                    }
                }
            ),
        )
        validator = validate_token(self.scope)
        self.assertRaises(
            HTTPException, validator, self.application, self.authorization
        )
        validate_token_mock.assert_called_with(
            self.application, self.authorization, self.scope
        )

    @patch("app.auth.api.validate_token")
    def test_validate_token_authorized_but_invalid(self, validate_token_mock):
        """validate_token: It fails when token is authorized but invalid"""
        validate_token_mock.return_value = Mock(
            spec=Response,
            status_code=status.HTTP_200_OK,
            json=Mock(
                return_value={
                    "data": {
                        "isValid": False,
                        "isAuthorized": True,
                    }
                }
            ),
        )
        validator = validate_token(self.scope)
        self.assertRaises(
            HTTPException, validator, self.application, self.authorization
        )
        validate_token_mock.assert_called_with(
            self.application, self.authorization, self.scope
        )

    @patch("app.auth.api.validate_token")
    def test_validate_token_unexpected_error(self, validate_token_mock):
        """validate_token: It handles unexpected errors properly"""
        validate_token_mock.return_value = Exception("Unexpected error")
        validator = validate_token(self.scope)
        self.assertRaises(
            HTTPException, validator, self.application, self.authorization
        )
        validate_token_mock.assert_called_with(
            self.application, self.authorization, self.scope
        )

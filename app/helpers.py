"""General helpers
"""

from fastapi import Header, status, HTTPException
from requests import Response
from .auth import api
from . import constants
from . import exceptions


def handle_error_response(response: Response) -> None:
    """Handles error responses

    Args:
        response (Response): The API response

    Raises:
        HTTPException(status_code=400): validation error
        HTTPException(status_code=500): Internal server error
    """
    if response.status_code == status.HTTP_400_BAD_REQUEST:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=response.json(),
        )

    if response.status_code > status.HTTP_400_BAD_REQUEST:
        raise exceptions.INTERNAL_SERVER_ERROR


def validate_token(expected_scope: str):
    """Validates the authorization token checking its valididy and scopes

    Args:
        expected_scope (str): The expected scope
    """

    def _validate(
        application: str = Header(..., convert_underscores=False),
        authorization: str = Header(..., convert_underscores=False),
    ):
        """Token validation internal function

        Args:
            application (str, optional): Application id
            authorization (str, optional): Authorization token

        Raises:
            HTTPException: Internal server error when something unexpected happens.
            HTTPException: Authorization error when token is invalidd.
            HTTPException: Forbidden error when the lacking the expected scope.
        """
        is_valid = False
        is_authorized = False

        try:
            response = api.validate_token(application, authorization, expected_scope)
            data = response.json().get("data", {})
            is_valid = data.get(constants.IS_VALID_PROPERTY) is True
            is_authorized = data.get(constants.IS_AUTHORIZED_PROPERTY) is True
        except Exception as exc:
            raise exceptions.INTERNAL_SERVER_ERROR from exc

        if not is_valid:
            raise exceptions.INVALID_TOKEN_ERROR

        if not is_authorized:
            raise exceptions.FORBIDDEN_ERROR

    return _validate

"""API exceptions
"""

from fastapi import HTTPException, status
from . import constants
from . import models


INTERNAL_SERVER_ERROR = HTTPException(
    status_code=constants.INTERNAL_SERVER_ERROR_CODE,
    detail=constants.INTERNAL_SERVER_ERROR_MESSAGE,
)

INVALID_TOKEN_ERROR = HTTPException(
    status_code=constants.INVALID_TOKEN_ERROR_CODE,
    detail=constants.INVALID_TOKEN_ERROR_MESSAGE,
)

FORBIDDEN_ERROR = HTTPException(
    status_code=constants.FORBIDDEN_ERROR_CODE,
    detail=constants.FORBIDDEN_ERROR_MESSAGE,
)


def get_validation_error(data: dict) -> HTTPException:
    """Gets a validation error from given data

    Args:
        data (dict): error data

    Returns:
        HTTPException: 400 HTTP Exception
    """
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=models.APIResponse(
            message=data.get("error_description"),
            code=data.get("error"),
            type=constants.VALIDATION_ERROR_TYPE,
        ).dict(),
    )

"""App Entry
"""

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .auth import router as authorize
from .category import router as category
from .service import router as service
from . import constants
from . import exceptions

# pylint: disable=W0613

app = FastAPI(
    title=constants.API_TITLE,
    description=constants.API_DESCRIPTION,
    summary=constants.API_SUMMARY,
    version=constants.API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=constants.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=constants.ALLOWED_METHODS,
    allow_headers=constants.ALLOWED_HEADERS,
)

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    """Handles HTTP exceptions

    Args:
        request (Request): HTTP Request
        exc (HTTPException): HTTP Exception

    Returns:
        JSONResponse: Error response
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )


@app.exception_handler(RequestValidationError)
def request_validation_error_handler(request: Request, exc: RequestValidationError):
    """Request validation error handler

    Args:
        request (Request): HTTP Request
        exc (RequestValidationError): Request validation error

    Returns:
        JSONResponse: Error response
    """
    errors = [f"{err['msg']} ({'.'.join(err['loc'])})" for err in exc.errors()]
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exceptions.get_validation_error(
            {
                "error_description": ". ".join(errors),
                "error": constants.BAD_REQUEST_ERROR_CODE,
            }
        ).detail,
    )


app.include_router(authorize.router, prefix=constants.AUTH_ROUTE_PREFIX)
app.include_router(category.router, prefix=constants.CATEGORIES_ROUTE_PREFIX)
app.include_router(service.router, prefix=constants.SERVICES_ROUTE_PREFIX)

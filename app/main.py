from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as authorize
from .category import router as category
from .service import router as service
from . import constants


app = FastAPI(
    title = constants.API_TITLE,
    description = constants.API_DESCRIPTION,
    summary = constants.API_SUMMARY,
    version = constants.API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = constants.ALLOWED_ORIGINS,
    allow_credentials = True,
    allow_methods = constants.ALLOWED_METHODS,
    allow_headers = constants.ALLOWED_HEADERS,
)

app.include_router(authorize.router, prefix = constants.AUTH_ROUTE_PREFIX)
app.include_router(category.router, prefix = constants.CATEGORIES_ROUTE_PREFIX)
app.include_router(service.router, prefix = constants.SERVICES_ROUTE_PREFIX)

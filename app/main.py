from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as authorize
from .category import router as category
from .service import router as service


app = FastAPI(
    title = 'QMS Kiosk API',
    description = 'The API for the QMS Kiosk Application.',
    summary = 'The API for the QMS Kiosk Application.',
    version = '1.0.0',
)

origins = [
    'http://localhost',
    'http://localhost:8081',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(authorize.router, prefix = '/api/v1/auth', tags=['auth'])
app.include_router(category.router, prefix = '/api/v1/categories', tags=['categories'])
app.include_router(service.router, prefix = '/api/v1/services', tags=['services'])

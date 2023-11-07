from fastapi import FastAPI
from starlette import middleware
from starlette.middleware.cors import CORSMiddleware

from api import setup_all_routes
from app_config import tags_metadata, app_title, app_description, app_version


app = FastAPI()


def get_origins():
    return [
        "http://127.0.0.1:8000",
        "http://127.0.0.1",
    ]


def get_middleware(origins):
    return [
        middleware.Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]


def create_app():
    fa_app = FastAPI(
        middleware=get_middleware(get_origins()),
        openapi_tags=tags_metadata,
        title=app_title,
        description=app_description,
        version=app_version,
    )

    setup_all_routes(fa_app)
    return fa_app


app = create_app()

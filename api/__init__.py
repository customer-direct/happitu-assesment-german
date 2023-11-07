from fastapi import APIRouter

from .index import router as docs
from .test import setup_test


def setup_all_routes(app):
    router = APIRouter()
    router.include_router(docs)

    setup_test(router)

    app.include_router(router)

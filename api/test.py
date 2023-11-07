from fastapi import APIRouter
import traceback
from schemas import PayloadSchema


def setup_test(app):
    test_router = APIRouter(prefix="/test")

    @test_router.post(
        "",
        tags=["/test"],
    )
    async def test(payload: PayloadSchema):
        try:
            return payload

        except Exception as e:
            traceback.print_exc()

    app.include_router(test_router)

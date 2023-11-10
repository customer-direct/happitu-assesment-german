from fastapi import APIRouter
import traceback
from schemas import PayloadSchema
from exercise import find_closest_number
import time

expected_result = 8


def setup_test(app):
    test_router = APIRouter(prefix="/test")

    @test_router.post(
        "",
        tags=["/test"],
    )
    async def test(payload: PayloadSchema):
        try:
            result = find_closest_number(payload.target_number)

            # Do not change the following logic
            if result == expected_result:
                print(f"Correct result. Going to sleep for 60 seconds.")
                time.sleep(60)
            else:
                print("Incorrect result")

        except Exception as e:
            traceback.print_exc()

    app.include_router(test_router)

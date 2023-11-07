from pydantic import BaseModel


class PayloadSchema(BaseModel):
    target_number: int

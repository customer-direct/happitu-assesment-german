from pydantic import BaseModel


class PayloadSchema(BaseModel):
    text1: str
    text2: str

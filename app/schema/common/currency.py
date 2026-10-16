from pydantic import BaseModel

class GetCurrency(BaseModel):

    id: int
    code: str
    currency: str
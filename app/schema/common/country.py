from pydantic import BaseModel

class GetCountry(BaseModel):

    id: int
    code: str
    country: str

    model_config = {
        "from_attributes": True,
    }
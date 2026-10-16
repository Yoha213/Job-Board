from pydantic import BaseModel

class GetState(BaseModel):

    id: int
    state: str

    model_config = {
        "from_attributes": True,
    }
from pydantic import BaseModel

class Profession(BaseModel):

    id: int
    profession: str
from pydantic import BaseModel

class GetSkill(BaseModel):

    id: int
    skill: str
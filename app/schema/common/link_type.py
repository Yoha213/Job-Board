from pydantic import BaseModel

class GetLinkType(BaseModel):

    id: int
    link_type: str
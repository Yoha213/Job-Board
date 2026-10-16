from pydantic import BaseModel, EmailStr, HttpUrl
from app.enum.gender import Gender
from datetime import date

class AddUser(BaseModel):

    first_name: str
    last_name: str
    username: str
    registered_email: EmailStr
    registered_phone: str
    password: str
    date_of_birth: date
    about: str | None = None
    profile_picture_url: HttpUrl | None = None
    gender: Gender
    state_id: int

class UserProfile(BaseModel):
    pass
from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class UserProfession(Base):

    __tablename__ = "users_professions"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    profession: Mapped[int] = mapped_column(ForeignKey("professions.id"), primary_key=True)
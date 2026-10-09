from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Enum as SQLEnum
from enum.level import Level

class UserSkill(Base):

    __tablename__ = "users_skills"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    skill: Mapped[str] = mapped_column(ForeignKey("skills.skill"), primary_key=True)
    level: Mapped[Level] = mapped_column(SQLEnum(Level), nullable=False)
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Enum as SQLEnum
from app.enum.level import Level

class UserLanguage(Base):

    __tablename__ = "user_languages"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    language_code: Mapped[str] = mapped_column(ForeignKey("languages.code"), primary_key=True)
    level: Mapped[Level] = mapped_column(SQLEnum(Level), nullable=False)
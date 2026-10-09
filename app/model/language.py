from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Language(Base):

    __tablename__ = "languages"

    code: Mapped[str] = mapped_column(primary_key=True)
    language: Mapped[str] = mapped_column(unique=True, nullable=False)
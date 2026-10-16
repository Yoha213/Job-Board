from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Language(Base):

    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True, nullable=False)
    language: Mapped[str] = mapped_column(unique=True, nullable=False)
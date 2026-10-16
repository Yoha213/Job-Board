from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Profession(Base):

    __tablename__ = "professions"

    id: Mapped[int] = mapped_column(primary_key=True)
    profession: Mapped[str] = mapped_column(unique=True, nullable=False)
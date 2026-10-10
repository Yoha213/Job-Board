from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Skill(Base):

    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    skill: Mapped[str] = mapped_column(unique=True, nullable=False)
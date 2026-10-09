from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Skill(Base):

    __tablename__ = "skills"

    skill: Mapped[str] = mapped_column(primary_key=True)
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class State(Base):

    __tablename__ = "states"

    id: Mapped[int] = mapped_column(primary_key=True)
    state: Mapped[str]
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"), nullable=False)
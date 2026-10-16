from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Country(Base):

    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True, nullable=False)
    country: Mapped[str] = mapped_column(unique=True, nullable=False)
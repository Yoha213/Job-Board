from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Country(Base):

    __tablename__ = "countries"

    code: Mapped[str] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(unique=True, nullable=False)
    falg_url: Mapped[str] = mapped_column(unique=True, nullable=False)
from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class City(Base):

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str]
    country_code: Mapped[str] = mapped_column(ForeignKey("countries.code"))
from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
class Company(Base):

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_email: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]
    about: Mapped[str | None]
    founded_year: Mapped[int | None]
    profile_picture_url: Mapped[str | None]
    primary_headquarter_id: Mapped[int] = mapped_column(ForeignKey("company_headquarters.id"))
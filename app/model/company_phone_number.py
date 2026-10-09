from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanyPhoneNumber(Base):

    __tablename__ = "comapanies_phone_numbers"

    comapny_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    phone_number: Mapped[int] = mapped_column(primary_key=True, unique=True)
    label: Mapped[str]
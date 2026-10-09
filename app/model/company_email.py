from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanyEmail(Base):

    __tablename__ = "companies_emails"

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    email: Mapped[int] = mapped_column(primary_key=True, unique=True)
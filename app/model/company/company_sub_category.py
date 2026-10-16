from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanySubCategory(Base):

    __tablename__ = "company_sub_categories"

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    sub_category_id: Mapped[int] = mapped_column(ForeignKey("sub_categories.id"), primary_key=True)
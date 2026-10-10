from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class ComapanyCategory(Base):

    __tablename__ = "company_categories"

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)
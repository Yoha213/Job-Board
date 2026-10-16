from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class SubCategory(Base):

    __tablename__ = "sub_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    sub_category: Mapped[str] = mapped_column(unique=True, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Category(Base):

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(unique=True, nullable=False)
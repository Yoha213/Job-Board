from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Currency(Base):

    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(unique=True, nullable=False)
    currency: Mapped[str] = mapped_column(unique=True, nullable=False)
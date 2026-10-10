from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Currency(Base):

    __tablename__ = "currencies"

    code: Mapped[str] = mapped_column(primary_key=True)
    currency: Mapped[str] = mapped_column(unique=True, nullable=False)
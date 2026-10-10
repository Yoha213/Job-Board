from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class LinkType(Base):

    __tablename__ = "link_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    link_type: Mapped[str] = mapped_column(unique=True, nullable=False)
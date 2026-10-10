from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class UserLink(Base):

    __tablename__ = "users_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    link_type_id: Mapped[int] = mapped_column(ForeignKey("link_types.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
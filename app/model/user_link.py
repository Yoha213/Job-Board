from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanyLink(Base):

    __tablename__ = "companies_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    link_type: Mapped[str] = mapped_column(ForeignKey("link_types.link_type"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanyLink(Base):

    __tablename__ = "company_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    link_type_id: Mapped[int] = mapped_column(ForeignKey("link_types.id"), nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
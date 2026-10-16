from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CompanyHeadquarter(Base):

    __tablename__ = "company_headquarters"
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"), primary_key=True)
    location_url: Mapped[str | None]
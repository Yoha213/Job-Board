from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TIMESTAMP, CheckConstraint, func
from datetime import datetime

class Company(Base):

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_email: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]
    about: Mapped[str | None]
    founded_year: Mapped[int | None]
    profile_picture_url: Mapped[str | None]
    min_members: Mapped[int | None]
    max_members: Mapped[int | None]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)

    # constraint

    __table_args__ = (
        CheckConstraint(
            "(min_members IS NOT NULL AND max_members IS NOT NULL AND (min_members > max_members)) OR (min_members IS NULL AND max_members IS NULL)",
            name="check_company_size"
            ),
    )
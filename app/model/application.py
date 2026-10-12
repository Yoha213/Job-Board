from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.enum.application_status import ApplicationStatus
from sqlalchemy import TIMESTAMP, func, ForeignKey, Enum as SQLEnum
from datetime import datetime

class Application(Base):

    __tablename__ = "applications"

    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), primary_key=True)
    applier_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    status: Mapped[ApplicationStatus] = mapped_column(SQLEnum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
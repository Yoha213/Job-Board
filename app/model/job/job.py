from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.enum.employment_type import EmploymentType
from app.enum.work_location import WorkLocation
from app.enum.job_status import JobStatus
from sqlalchemy import TIMESTAMP, func, ForeignKey, CheckConstraint, Enum as SQLEnum
from datetime import datetime

class Job(Base):

    __tablename__ = "jobs"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    company_headquarder_id: Mapped[int] = mapped_column("company_headquarters.id")
    title: Mapped[str]
    min_salary: Mapped[int | None]
    max_salary: Mapped[int | None]
    currency_id: Mapped[id] = mapped_column(ForeignKey("currencies.id"))
    employment_type: Mapped[EmploymentType] = mapped_column(SQLEnum(EmploymentType), nullable=False)
    work_location: Mapped[WorkLocation] = mapped_column(SQLEnum(WorkLocation), nullable=False)
    status: Mapped[JobStatus] = mapped_column(SQLEnum(JobStatus), default=JobStatus.OPEN.value, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # constraints

    __table_args__ = (
        CheckConstraint("(min_salary IS NOT NULL AND max_salary IS NOT NULL AND currency_id IS NOT NULL AND (min_salary < max_salary)) OR (min_salary IS NULL AND max_salary IS NULL AND currency_id IS NULL)",
                        name="check_salary"),
    )
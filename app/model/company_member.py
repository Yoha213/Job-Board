from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Enum as SQLEnum
from app.enum.member_role import MemberRole

class CompanyMember(Base):

    __tablename__ = "company_members"

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    member_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role: Mapped[MemberRole] = mapped_column(SQLEnum(MemberRole), default=MemberRole.MEMBER.value, nullable=False)
from app.database.base import Base
from sqlalchemy import ForeignKey, TIMESTAMP, Enum as SQLEnum
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql.expression import text
from datetime import date, datetime
from app.enum.gender import Gender
from app.enum.role import Role

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_email: Mapped[str] = mapped_column(unique=True, nullable=False)
    registered_phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]
    date_of_birth: Mapped[date | None]
    about: Mapped[str | None]
    profile_picture_url: Mapped[str | None]
    gender: Mapped[Gender] = mapped_column(SQLEnum(Gender))
    role: Mapped[Role] = mapped_column(SQLEnum(Role), default=Role.REGULAR.value, nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'), onupdate=text('now()'))
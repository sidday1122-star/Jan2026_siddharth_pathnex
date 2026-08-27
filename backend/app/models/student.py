from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    phone = Column(
        String(20),
        nullable=False
    )

    course = Column(
        String(150),
        nullable=False
    )

    enrollment_date = Column(
        Date,
        nullable=False
    )

    status = Column(
        String(30),
        default="ACTIVE"
    )


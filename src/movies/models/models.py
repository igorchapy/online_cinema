import uuid
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True)

    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)

    imdb = Column(Float)
    votes = Column(Integer)

    description = Column(Text)

    certification_id = Column(
        Integer,
        ForeignKey("certifications.id")
    )

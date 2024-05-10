
from sqlalchemy import Column, Integer, String

from app.models.database import Base


class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    correo_electronico = Column(String, unique=True, index=True)

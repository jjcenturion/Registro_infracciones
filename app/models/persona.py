

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    correo_electronico = Column(String, unique=True, index=True)


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.database import Base


class Persona(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    correo_electronico = Column(String, unique=True, index=True)

    # Definición de la relación con Vehiculo
    vehiculos = relationship("Vehiculo", back_populates="propietario")


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.database import Base

class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    id = Column(Integer, primary_key=True, index=True)
    placa_patente = Column(String, index=True)
    marca = Column(String)
    color = Column(String)

    # Definición de la relación con Persona
    propietario_id = Column(Integer, ForeignKey('personas.id'))
    propietario = relationship("Persona", back_populates="vehiculos")

    # Definición de la relación con Infraccion
    infracciones = relationship("Infraccion", back_populates="vehiculo")


from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from app.models.database import Base

class Infraccion(Base):
    __tablename__ = 'infracciones'

    id = Column(Integer, primary_key=True, index=True)
    placa_patente = Column(String, ForeignKey('vehiculos.placa_patente'), index=True)
    timestamp = Column(DateTime, index=True)
    comentario = Column(Text)

    # Definición de la relación con Vehículo
    vehiculo = relationship("Vehiculo", back_populates="infracciones")

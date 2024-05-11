from sqlalchemy import Column, Integer, String
from app.models.database import Base

class Oficial(Base):
    __tablename__ = 'oficiales'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    numero_identificatorio = Column(String, unique=True, index=True)
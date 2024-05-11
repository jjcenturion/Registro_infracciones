from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.persona import Persona
from app.models.infraccion import Infraccion
from app.models.oficial import Oficial
from app.models.vehiculo import Vehiculo
import app.schemas as schemas


class BaseRepo:
    def __init__(self, model):
        self.model = model
    
    def create(self, db: Session, obj_data):
        db_obj = self.model(**obj_data.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def find_by_id(self, db: Session, obj_id):
        return db.query(self.model).filter(self.model.id == obj_id).first()
    
    def find_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def update(self, db: Session, obj_data):
        updated_obj = db.merge(obj_data)
        db.commit()
        return updated_obj
    
    def delete(self, db: Session, obj_id):
        db_obj = self.find_by_id(db, obj_id)
        db.delete(db_obj)
        db.commit()

class PersonaRepo(BaseRepo):
    def __init__(self):
        super().__init__(Persona)
    
    def find_by_name(self, db: Session, nombre):
        return db.query(Persona).filter(Persona.nombre == nombre).first()

class VehiculoRepo(BaseRepo):
    def __init__(self):
        super().__init__(Vehiculo)

    def find_by_patente(self, db: Session, patente):
        return db.query(Vehiculo).filter(Vehiculo.placa_patente == patente).first()

class OficialRepo(BaseRepo):
    def __init__(self):
        super().__init__(Oficial)

    def find_by_numero(self, db: Session, numero_identificatorio):
        return db.query(Oficial).filter(Oficial.numero_identificatorio == numero_identificatorio).first()

class InfraccionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Infraccion)

    def obtener_infracciones_por_correo(self, db: Session, correo_electronico):
        # Primero, obtenemos la persona asociada al correo electrónico proporcionado
        persona = db.query(Persona).filter(Persona.correo_electronico == correo_electronico).first()

        if not persona:
            return []

        # Luego, obtenemos todos los vehículos asociados a esa persona
        vehiculos = persona.vehiculos

        infracciones_totales = []

        # Iteramos sobre cada vehículo para obtener sus infracciones
        for vehiculo in vehiculos:
            # Obtenemos las infracciones asociadas a este vehículo y las agregamos a la lista total
            infracciones_vehiculo = vehiculo.infracciones
            infracciones_totales.extend(infracciones_vehiculo)

        return infracciones_totales
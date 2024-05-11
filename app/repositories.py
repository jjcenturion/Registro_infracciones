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

class InfraccionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Infraccion)
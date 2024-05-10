from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.persona import Persona
import app.schemas as schemas

class PersonaRepo:

    def create(db: Session, persona: schemas.PersonaCreate):
        db_persona = Persona(nombre=persona.nombre, correo_electronico=persona.correo_electronico)
        db.add(db_persona)
        db.commit()
        db.refresh(db_persona)
        return db_persona

    def find_by_name(db: Session, nombre):
        return db.query(Persona).filter(Persona.nombre == nombre).first()
    
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Persona).offset(skip).limit(limit).all()
    
    def find_by_id(db: Session, _id):
        return db.query(Persona).filter(Persona.id == _id).first()
    
    def update(db: Session, persona_data):
        updated_persona = db.merge(persona_data)
        db.commit()
        return updated_persona
    
    def delete(db: Session, persona_id):
        db_persona = db.query(Persona).filter_by(id=persona_id).first()
        db.delete(db_persona)
        db.commit()
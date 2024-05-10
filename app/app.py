from typing import Union

from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from app.models.persona import Persona
from app.models.database import get_db
from app.repositories import PersonaRepo
import app.schemas as schemas

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/personas', response_model=List[schemas.Persona])
def get_personas(db: Session = Depends(get_db)):

    personas = PersonaRepo.find_all(db)
    if personas:
        return personas
    raise HTTPException(status_code=400, detail="Ninguna persona fue encontrada")


@app.post("/persona/", response_model=schemas.Persona)
def create_persona(persona_request: schemas.PersonaCreate, db: Session = Depends(get_db)):
    
    db_persona = PersonaRepo.find_by_name(db, nombre= persona_request.nombre)
    if db_persona:
        raise HTTPException(status_code=400, detail=" La persona ya existe")
    else:
        return PersonaRepo.create(db, persona=persona_request)
    
    
@app.put('/persona/{persona_id}', response_model=schemas.Persona)
def update_persona(persona_id: int, persona_request: schemas.Persona, db: Session = Depends(get_db)):

    db_persona = PersonaRepo.find_by_id(db, persona_id)
    if db_persona:
        update_persona_encoded = jsonable_encoder(persona_request)
        db_persona.nombre = update_persona_encoded['nombre']

        return PersonaRepo.update(db, db_persona)
    else:
        raise HTTPException(status_code=400, detail="El ID de persona dado no fue encontrado")
    
@app.delete('/persona/{persona_id}')
def delete_persona(persona_id: int, db: Session = Depends(get_db)):

    db_persona = PersonaRepo.find_by_id(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="El ID de persona no fue encontrado")

    PersonaRepo.delete(db, persona_id)
    return "Persona borrada"


from typing import Union

from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List

from app.models.persona import Persona
from app.models.database import get_db
from app.repositories import PersonaRepo, VehiculoRepo, OficialRepo, InfraccionRepo
import app.schemas as schemas

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/personas', response_model=List[schemas.Persona])
def get_personas(db: Session = Depends(get_db)):

    persona_repo = PersonaRepo() 
    personas = persona_repo.find_all(db=db)
    if personas:
        return personas
    raise HTTPException(status_code=400, detail="Ninguna persona fue encontrada")


@app.post("/persona/", response_model=schemas.Persona)
def create_persona(persona_request: schemas.PersonaCreate, db: Session = Depends(get_db)):
    
    persona_repo = PersonaRepo()
    db_persona = persona_repo.find_by_name(db=db, nombre= persona_request.nombre)
    if db_persona:
        raise HTTPException(status_code=400, detail=" La persona ya existe")
    else:
        return persona_repo.create(db=db, obj_data=persona_request)
    
    
@app.put('/persona/{persona_id}', response_model=schemas.Persona)
def update_persona(persona_id: int, persona_request: schemas.Persona, db: Session = Depends(get_db)):

    persona_repo = PersonaRepo()
    db_persona = persona_repo.find_by_id(db, persona_id)
    if db_persona:
        update_persona_encoded = jsonable_encoder(persona_request)
        db_persona.nombre = update_persona_encoded['nombre']

        return persona_repo.update(db, db_persona)
    else:
        raise HTTPException(status_code=400, detail="El ID de persona dado no fue encontrado")
    
@app.delete('/persona/{persona_id}')
def delete_persona(persona_id: int, db: Session = Depends(get_db)):

    persona_repo = PersonaRepo()
    db_persona = persona_repo.find_by_id(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="El ID de persona no fue encontrado")

    persona_repo.delete(db, persona_id)
    return "Persona borrada"

@app.post("/vehiculo/", response_model=schemas.Vehiculo)
def create_vehiculo(vehiculo_request: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    
    vehiculo_repo = VehiculoRepo()
    db_vehiculo = vehiculo_repo.find_by_patente(db=db, patente=vehiculo_request.placa_patente)
    if db_vehiculo:
        raise HTTPException(status_code=400, detail=" La placa patente ya existe")
    else:
        return vehiculo_repo.create(db=db, obj_data=vehiculo_request)
    

@app.get('/vehiculos', response_model=List[schemas.Vehiculo])
def get_vehiculos(db: Session = Depends(get_db)):

    vehiculo_repo = VehiculoRepo() 
    vehiculos = vehiculo_repo.find_all(db=db)
    if vehiculos:
        return vehiculos
    raise HTTPException(status_code=400, detail="Ningun Vehiculo fue encontrado")


@app.put('/vehiculo/{vehiculo_id}', response_model=schemas.Vehiculo)
def update_vehiculo(vehiculo_id: int, vehiculo_request: schemas.Vehiculo, db: Session = Depends(get_db)):

    vehiculo_repo = VehiculoRepo() 
    db_vehiculo = vehiculo_repo.find_by_id(db, vehiculo_id)
    if db_vehiculo:
        update_vehiculo_encoded = jsonable_encoder(vehiculo_request)
        db_vehiculo.placa_patente = update_vehiculo_encoded['placa_patente']
        db_vehiculo.marca = update_vehiculo_encoded['marca']
        db_vehiculo.color = update_vehiculo_encoded['color']
        db_vehiculo.propietario_id = update_vehiculo_encoded['propietario_id']

        return vehiculo_repo.update(db, db_vehiculo)
    else:
        raise HTTPException(status_code=400, detail="El ID del vehiculo no fue encontrado")
    
@app.delete('/vehiculo/{vehiculo_id}')
def delete_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):

    vehiculo_repo = VehiculoRepo() 
    db_vehiculo = vehiculo_repo.find_by_id(db, vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="El ID del vehiculo no fue encontrado")

    vehiculo_repo.delete(db, vehiculo_id)
    return "Vehiculo borrado"

@app.post("/oficial/", response_model=schemas.Oficial)
def create_oficial(oficial_request: schemas.OficialCreate, db: Session = Depends(get_db)):
    
    oficial_repo = OficialRepo()
    db_oficial = oficial_repo.find_by_numero(db, oficial_request.numero_identificatorio)
    if db_oficial:
        raise HTTPException(status_code=400, detail="El numero identificatorio del oficial ya existe")
    else:
        return oficial_repo.create(db=db, obj_data=oficial_request)
    
@app.get('/oficiales', response_model=List[schemas.Oficial])
def get_oficiales(db: Session = Depends(get_db)):

    oficial_repo = OficialRepo() 
    oficiales = oficial_repo.find_all(db=db)
    if oficiales:
        return oficiales
    raise HTTPException(status_code=400, detail="Ningun Oficial fue encontrado")

@app.post("/infraccion/", response_model=schemas.Infraccion)
def cargar_infraccion(infraccion_request: schemas.InfraccionCreate, db: Session = Depends(get_db)):
    
    # Verificar si la placa patente existe en la tabla de vehículos
    vehiculo_repo = VehiculoRepo()
    vehiculo_existente = vehiculo_repo.find_by_patente(db=db, patente=infraccion_request.placa_patente)
    if not vehiculo_existente:
        raise HTTPException(status_code=404, detail="Placa patente no encontrada")
    
    try:
        infracccion_repo = InfraccionRepo()
        return infracccion_repo.create(db=db, obj_data=infraccion_request)
    except Exception as e:
        # Manejo de errores inesperados
        raise HTTPException(status_code=500, detail="Error interno del servidor") from e
    

@app.post("/generar_informe/", response_model=schemas.InformeInfraccionResponse)
def generar_informe(informe_request: schemas.InformeInfraccionRequest, db: Session = Depends(get_db)):
    """ Debe recibir como parámetro el correo electrónico de una persona, y devolver un JSON con el
        listado de infracciones de cualquier vehículo a su nombre.""" 

    infracccion_repo = InfraccionRepo()
    infracciones = infracccion_repo.obtener_infracciones_por_correo(db, informe_request.correo_electronico)
    if not infracciones:
        raise HTTPException(status_code=404, detail="No se encontraron infracciones para el correo electrónico proporcionado")
    return {"infracciones": infracciones}


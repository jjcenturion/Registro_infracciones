from typing import Union

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.persona import Persona
from app.models.database import get_db

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.post("/users/")
def create_user(nombre: str, correo_electronico: str, db: Session = Depends(get_db)):
    db_user = Persona(nombre=nombre, correo_electronico=correo_electronico)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
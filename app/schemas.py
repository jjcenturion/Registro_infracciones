from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import List

class PersonaBase(BaseModel):

    nombre: str
    correo_electronico: str


class PersonaCreate(PersonaBase):
    pass


class Persona(PersonaBase):
    id: int

    class Config:
        orm_mode = True

class VehiculoBase(BaseModel):

    placa_patente: str
    marca: str
    color: str
    propietario_id: int


class VehiculoCreate(VehiculoBase):
    pass


class Vehiculo(VehiculoBase):
    id: int

    class Config:
        orm_mode = True

class OficialBase(BaseModel):

    nombre: str
    numero_identificatorio: str
    hash_contraseña: str

class OficialCreate(OficialBase):
    pass

class Oficial(OficialBase):
    id: int

    class Config:
        orm_mode = True

class InfraccionBase(BaseModel):

    placa_patente: str
    timestamp: datetime
    comentario: Optional[str] = None

class InfraccionCreate(InfraccionBase):
    pass

class Infraccion(InfraccionBase):
    id: int

    class Config:
        orm_mode = True

class InformeInfraccionRequest(BaseModel):
    correo_electronico: str

class InformeInfraccionResponse(BaseModel):
    infracciones: List[Infraccion]
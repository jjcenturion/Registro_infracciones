from pydantic import BaseModel

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
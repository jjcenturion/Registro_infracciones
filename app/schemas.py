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
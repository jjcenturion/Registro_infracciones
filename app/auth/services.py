import os
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import FastAPI, HTTPException,status
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from app.models.database import get_db
from app.models.oficial import Oficial

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Instancia de CryptContext para manejar el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Función para verificar si una contraseña coincide con su hash
def verificar_contraseña(contraseña_plana: str, hash_contraseña: str) -> bool:
    return pwd_context.verify(contraseña_plana, hash_contraseña)

# Función para hashear una contraseña
def hashear_contraseña(contraseña: str) -> str:
    return pwd_context.hash(contraseña)

    
async def get_oficial(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Decodificar el token JWT y obtener el sub (subject)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        num_identificatorio = payload.get("sub")
        if not num_identificatorio:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de acceso inválido")

        db_oficial = db.query(Oficial).filter(Oficial.numero_identificatorio == num_identificatorio).first()
        if not db_oficial:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se encontró el oficial")

        # retorna un valor verdadero si la validación del token y la existencia del oficial son exitosas
        return True
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pudo validar el token")
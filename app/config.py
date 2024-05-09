import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtene la URL de conexión a la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")



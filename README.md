# Registro de Infracciones

Este es un proyecto desarrollado con Python y FastApi para crear una API RESTful.

## Configuración del Entorno

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/jjcenturion/Registro_infracciones.git
    ```

2. Crea un entorno virtual para instalar las dependencias del proyecto:

    ```bash
    cd proyecto
    python3 -m venv venv
    source venv/bin/activate    


3. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

4. Crea un archivo `.env` en la raíz del proyecto para definir las variables de entorno necesarias. 

## Migraciones con Alembic

Para administrar las migraciones de la base de datos, utilizamos Alembic.

1. Asegúrate de tener todas las configuraciones de la base de datos en el archivo `alembic.ini`.

2. Para crear una nueva versión de migración, ejecuta el siguiente comando:

     ```bash
    alembic revision -m "Descripción de la migración"
    ```


3. Para aplicar las migraciones pendientes a la base de datos, usa:

    ```bash
    alembic upgrade head
    ```

## Iniciar el Proyecto

Una vez configurado el entorno y aplicadas las migraciones, puedes iniciar el proyecto.

1. Para iniciar la API, ejecuta el siguiente comando:

    ```bash
    uvicorn app.app:app --reload
    ```    

Esto iniciará la API en [http://localhost:8000](http://localhost:8000).

## Crear Contenedor y Docker Compose

Si prefieres ejecutar el proyecto en un contenedor de Docker:

1. Construye la imagen del contenedor:

    ```bash
    docker build -t proyecto-xyz .
    ```  

2. Crea y ejecuta el contenedor con Docker Compose:

    ```bash
    docker-compose up
    ``` 

Esto iniciará el contenedor y la aplicación estará disponible en [http://localhost:8000](http://localhost:8000).

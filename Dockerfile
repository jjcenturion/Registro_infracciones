
FROM python:3.8-slim

# Configura el working directory en el container
WORKDIR /app

COPY . /app
COPY ./requirements.txt /app/requirements.txt
COPY ./tests /app/tests

# Instala los paquetes de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Inicia FastAPI server 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]

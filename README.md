# Spot FastAPI App

## Sin hacer uso de docker
Hay que crear la base de datos con las credenciales que aparecen en el archivo de variables de entorno (dev.env)

```

pip install -r requirements.txt

vunicorn app.main:app --host=0.0.0.0 --reload --env-file=dev.env

```

## Haciendo uso de docker
Se debe correr lo siguiente para construir y correr el contenedor. No es necesario crear la base de datos de postgres, pues esta se crea dentro del mismo contenedor automaticamente:

```

sudo docker-compose up -d --build

```

### Para abrir el aplicativo se debe abrir la url http://127.0.0.1:8000/docs

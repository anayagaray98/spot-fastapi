from fastapi import FastAPI
from routes.storage import storage_routes
from . import models
from .database import engine
#______________________________________________________________
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(storage_routes, prefix="")


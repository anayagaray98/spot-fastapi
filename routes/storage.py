from fastapi import APIRouter, Form, UploadFile, File
from azure_blob.blob import upload_blob
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import SessionLocal
from app import crud
from os import getenv
from azure.storage.blob import BlobServiceClient, generate_account_sas, AccountSasPermissions, ResourceTypes, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app.environment import ENVIRONMENT

if ENVIRONMENT=='PROD':
    load_dotenv('prod.env')
else:
    load_dotenv('.env')
#___________________________________________________________
storage_routes = APIRouter()
#______________________________________________________________
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#______________________________________________________________
"""Using async, await to make function asynchronic - punto 1.f"""
@storage_routes.post("/create/camera", response_model=schemas.Camera)
async def createCamera(name:str=Form(...), db: Session = Depends(get_db)):
    db_camera = crud.get_camera(db=db, camera_name=name)

    """Validating input data - punto 1.h"""
    if db_camera:
        raise HTTPException(status_code=400, detail="Camera already registered")
    return crud.create_camera(db=db, camera_name=name)
#______________________________________________________________
def getBlob(filename:str):
    try:
        """Generate an account-level SAS token for the storage account"""
        sas_token = generate_account_sas(
            account_name=getenv('AZURE_ACCOUNT_NAME'),
            account_key=getenv('AZURE_ACCOUNT_KEY'),
            resource_types=ResourceTypes(service=True),
            permission=AccountSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(days=365)
        )
        #__________________________________________________________
        blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=' + getenv('AZURE_ACCOUNT_NAME') + ';AccountKey=' + getenv('AZURE_ACCOUNT_KEY') + ';EndpointSuffix=core.windows.net')
        blob_url = blob_service_client.get_blob_client(container=getenv('AZURE_CONTAINER_NAME'), blob=filename).url
        #__________________________________________________________
        """Create a blob-level SAS token"""
        sas_url = generate_blob_sas(
            account_name=getenv('AZURE_ACCOUNT_NAME'),
            account_key=getenv('AZURE_ACCOUNT_KEY'),
            container_name=getenv('AZURE_CONTAINER_NAME'),
            blob_name=filename,
            permission=BlobSasPermissions(read=True),
            protocol="https",
            start_time=datetime.utcnow(),
            expiry=datetime.utcnow() + timedelta(days=365),
            ip=None,
            user_delegation_key=None,
            cache_control=None,
            content_disposition=None,
            content_encoding=None,
            content_language=None,
            content_type=None,
            claims=None,
            snapshot=None,
            version=None,
            encoded_account_sas=sas_token,
            url_prefix=f"https://{blob_url}"
        )
        #__________________________________________________________
        return blob_url #+ '?' + sas_url
    
    except TypeError as e:
        print(e)
        return ""
#______________________________________________________________
@storage_routes.post("/image/upload")
async def upload(cameraId:int=Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    data = await file.read()
    filename = file.filename
    """Uploading image/base64 to Azure Storage Account, Blob - punto 1.c"""
    upload_blob(filename, data)
    url = getBlob(filename)
    print(url)
    """Saving Information - punto 1.d"""
    return crud.create_camera_image(db=db, camera_id=cameraId, image=url)
#____________________________________________________________
@storage_routes.get("/image/get-images")
async def getImages(db: Session = Depends(get_db)):
    db_images = crud.get_images(db=db)
    return db_images
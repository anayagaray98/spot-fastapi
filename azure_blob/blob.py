from azure.storage.blob import BlobServiceClient
from os import getenv
from typing import BinaryIO
from responses.response_json import response_json
from app.environment import ENVIRONMENT
from dotenv import load_dotenv

if ENVIRONMENT=='PROD':
    load_dotenv('prod.env')
else:
    load_dotenv('.env')
#______________________________________________________________
blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=' + getenv('AZURE_ACCOUNT_NAME') + ';AccountKey=' + getenv('AZURE_ACCOUNT_KEY') + ';EndpointSuffix=core.windows.net')
container = getenv('AZURE_CONTAINER_NAME')
#______________________________________________________________
def upload_blob(filename:str, data:BinaryIO):
    try:
        blob_client = blob_service_client.get_blob_client(container=container, blob=filename)
        blob_client.upload_blob(data)
        return response_json(message="success")
    
    except Exception as e:
        return response_json(message=e.message, status=500)
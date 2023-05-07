"""Using serilizers with pydantic - punto 1.g"""
from pydantic import BaseModel
#______________________________________________________________
class ImageBase(BaseModel):
    image: str

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int
    camera_id: int
    class Config:
        orm_mode = True

class CameraBase(BaseModel):
    name:str

class CameraCreate(CameraBase):
    pass

class Camera(CameraBase):
    id: int
    images: list[Image] = []
    class Config:
        orm_mode = True
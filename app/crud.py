from sqlalchemy.orm import Session
from . import models, schemas
#______________________________________________________________
def get_camera(db: Session, camera_name: str):
    return db.query(models.Camera).filter(models.Camera.name == camera_name).first()
#______________________________________________________________
def get_cameras(db: Session):
    return db.query(models.Camera).all()
#______________________________________________________________
def get_images(db: Session):
    return db.query(models.Image).all()
#______________________________________________________________
def create_camera(db: Session, camera_name: schemas.CameraCreate):
    db_camera = models.Camera(name=camera_name)
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera
#______________________________________________________________
def create_camera_image(db: Session, image: schemas.ImageCreate, camera_id: int):
    db_image = models.Image(image=image, camera_id=camera_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
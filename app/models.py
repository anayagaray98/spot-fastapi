from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
"""Defining models"""
#___________________________________________________________________
class Camera(Base):
    __tablename__ = "cameras"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    images = relationship("Image", back_populates="camera")
#_______________________________________________________________________
"""Data to DB - punto 1.b"""
class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True, default=datetime.utcnow())
    image = Column(String, index=True )
    camera_id = Column(Integer, ForeignKey("cameras.id"))
    camera = relationship("Camera", back_populates="images")
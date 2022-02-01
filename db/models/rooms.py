from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base

class Room(Base):
    """
    Room model
    """
    __tablename__   = "rooms"
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String(64), nullable=False, index=True)
    description     = Column(String(240), nullable=False)
    price           = Column(Float, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)
    available       = Column(Boolean, nullable=False, default=True)
    location        = relationship("Location", back_populates="rooms", uselist=False)
    images          = relationship("RoomImage", back_populates="room")
    owner_id        = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner           = relationship("User", back_populates="rooms")

class RoomImage(Base):
    """
    Room image model
    """
    __tablename__   = "room_images"
    id              = Column(Integer, primary_key=True, index=True)
    url             = Column(String(256), nullable=False)
    room_id         = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    room            = relationship("Room", back_populates="images")

class Location(Base):
    """
    Location model
    """
    __tablename__   = "locations"
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String(64), nullable=False, index=True)
    address         = Column(String(128), nullable=False)
    city            = Column(String(64), nullable=False)
    state           = Column(String(64), nullable=False)
    zip             = Column(String(64), nullable=False)
    lat             = Column(Float, nullable=False)
    lng             = Column(Float, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)
    room_id         = Column(Integer, ForeignKey("rooms.id"), nullable=False)
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
    __tablename__   = "users"
    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String(64), nullable=False, index=True)
    email           = Column(String(64), nullable=False, index=True, unique=True)
    is_active       = Column(Boolean, nullable=False, default=True)
    is_admin        = Column(Boolean, nullable=False, default=False)
    password        = Column(String(128), nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)
    rooms           = relationship("Room", back_populates="owner")
     
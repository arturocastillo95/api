from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from uuid import uuid4, UUID

class Location(BaseModel):
    id: Optional[UUID] = None
    address: str
    city: str
    state: str
    zip: str
    lat: float
    lng: float
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class Room(BaseModel):
    id: Optional(UUID) = uuid4
    name: str
    description: str
    capacity: int
    price: float
    available: bool
    image_url: str
    amenities: list
    reviews: list
    location: Location
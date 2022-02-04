from sqlalchemy.orm import Session

from schemas.users import UserCreate
from core.hashing import Hasher
from db.models.users import User

from datetime import datetime


def create_new_user(user: UserCreate, db: Session):
    email = user.email
    hashed_password = Hasher.hash_password(user.password)
    name = user.name
    is_active = True
    is_admin = False
    #Add created at current time
    created_at = datetime.now()
    updated_at = datetime.now()
    db_user = User(email=email, password=hashed_password, name=name ,is_active=is_active, is_admin=is_admin, created_at=created_at, updated_at=updated_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

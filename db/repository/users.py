from sqlalchemy.orm import Session

from schemas.users import UserCreate
from models.users import User
from core.hashing import Hasher

from datetime import datetime


def crate_new_user(user: UserCreate, db: Session):
    email = user.email
    hashed_password = Hasher.get_password_hash(user.password)
    is_active = True
    is_admin = False
    #Add created at current time
    created_at = datetime.now()
    updated_at = datetime.now()
    db_user = User(email=email, password=hashed_password, is_active=is_active, is_admin=is_admin, created_at=created_at, updated_at=updated_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

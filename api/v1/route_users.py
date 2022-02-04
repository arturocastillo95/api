from sys import prefix
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.session import get_db
from crud.users import create_new_user

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    return create_new_user(user, db)
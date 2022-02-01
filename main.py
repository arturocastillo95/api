from matplotlib.pyplot import title
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)
    create_tables(engine)
    return app

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = start_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}


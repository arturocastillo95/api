from matplotlib.pyplot import title
from fastapi import FastAPI
from core.config import settings

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI(title=settings.PROJECT_TITLE, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)

@app.get("/")
async def root():
    return {"message": "Hello World"}


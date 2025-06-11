from fastapi import FastAPI
from routes import ask, upload

app = FastAPI()

app.include_router(ask.router)
app.include_router(upload.router)
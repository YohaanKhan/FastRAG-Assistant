from fastapi import FastAPI
from routes import ask, upload, auth

app = FastAPI()

app.include_router(ask.router)
app.include_router(upload.router)
app.include_router(auth.router)
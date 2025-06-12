from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserRegister):
    # Accepts a email, username and password.
    # Add email verification maybe
    # Hash the password (for security).
    # Store the user in a database.
    # Return a confirmation message.
    return {"User registered"}

@router.post("/login")
def login(user: UserLogin):
    # Accept the username and password.
    # confirm the existence of the user from the database.
    # Return a confirmation message.
    return {"User Logged in."}


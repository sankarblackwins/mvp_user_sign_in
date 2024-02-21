"""
from fastapi import APIRouter, Depends
from controllers import UserController
from models import User
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()

# Connect to MongoDB Atlas
MONGO_URI = "mongodb+srv://sankarworks:Sankar%1134@final.hfalk9f.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGO_URI)

# Initialize UserController with MongoDB client
user_controller = UserController(db_client=client)

@router.post("/users/")
def create_user(user: User):
    user_controller.add_user(user)
    return user

@router.get("/users/{username}")
def read_user(username: str):
    return user_controller.get_user_by_username(username)
"""
from fastapi import APIRouter
from controllers import UserController
from models import User
from dbconfig import db_config

router = APIRouter()

# Pass db_config argument when creating UserController instance
user_controller = UserController(db_config)

@router.post("/users/")
async def create_user(user: User):
    await user_controller.add_user(user)
    return user

@router.get("/users/{username}")
async def read_user(username: str):
    return await user_controller.get_user_by_username(username)

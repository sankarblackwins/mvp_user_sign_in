from fastapi import HTTPException
from models import User

class UserController:
    def __init__(self, db_config): 
        self.db = db_config.db
        self.collection = self.db.users

    async def add_user(self, user: User):
        await self.collection.insert_one(user.dict())

    async def get_user_by_username(self, username: str) -> User:
        user = await self.collection.find_one({"username": username})
        if user:
            return User(**user)
        else:
            raise HTTPException(status_code=404, detail="User not found")

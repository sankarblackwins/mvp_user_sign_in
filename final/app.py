from fastapi import FastAPI
from controllers import UserController
from dbconfig import DatabaseConfig
from dbconfig import db_config
from router import router

app = FastAPI()

# MongoDB Atlas configuration
MONGO_URI = "mongodb+srv://sankarworks:Sankar%1134@final.hfalk9f.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "final"

# Initialize MongoDB configuration
db_config = DatabaseConfig(uri=MONGO_URI, db_name=DB_NAME)

# Connect to MongoDB
if db_config.connect():
    print("Connected to MongoDB.")
else:
    print("Failed to connect to MongoDB.")

# Initialize controller with MongoDB config
user_controller = UserController(db_config=db_config)

# Include router with the controller injected
app.include_router(router)

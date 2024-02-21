from pymongo import MongoClient
import urllib.parse
from controllers import UserController

class DatabaseConfig:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.user_controller = None

    def connect(self):
        try:
            # Parse the URI to handle special characters in the username and password
            parsed_uri = urllib.parse.quote_plus(self.uri)
            
            # Create a MongoClient instance
            self.client = MongoClient(parsed_uri)

            # Access the specified database
            self.db = self.client[self.db_name]
            
            # Initialize controller with MongoDB config
            self.user_controller = UserController(db_config=self)
            
            return True
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            return False

    def disconnect(self):
        if self.client:
            self.client.close()

# Create a global instance of DatabaseConfig
db_config = DatabaseConfig(uri="mongodb+srv://sankarworks:Sankar%1134@final.hfalk9f.mongodb.net/?retryWrites=true&w=majority", db_name="final")

# Connect to MongoDB
if not db_config.connect():
    raise RuntimeError("Failed to connect to MongoDB.")

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

class MongoDBClient:
    def __init__(self, uri: str, db_name: str):
        print("Initializing MongoDB client=============================")
        print("\t---URI: ", uri)
        print("\t---DB Name: ", db_name)
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str) -> Collection:
        """
        Retrieve a collection from the database.
        """
        return self.db[collection_name]
    
# Dependency Injection for FastAPI
def get_mongo_client():
    """
    Dependency-injected MongoDB client.
    """
    from backend.multiquery.config.config_loader import get_config
    config = get_config().database
    return MongoDBClient(config.uri, config.db_name)
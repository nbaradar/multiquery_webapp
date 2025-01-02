from pymongo import MongoClient
from fastapi import Depends
from multiquery.app import get_config
from multiquery.core.config import AppConfig

def get_mongo_client(config: AppConfig = Depends(get_config)):
    """
    Dependency-injected MongoDB client.
    """
    db_config = config.database_configs[0]  # Assume first config for now
    return MongoClient(db_config.uri)

def get_mongo_collection(client=Depends(get_mongo_client), config: AppConfig = Depends(get_config)):
    """
    Dependency-injected MongoDB collection.
    """
    db_config = config.database_configs[0]
    db = client[db_config.db_name]
    return db[db_config.collection_name]
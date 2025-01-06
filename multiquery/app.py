from fastapi import FastAPI, Depends
from multiquery.config.config_loader import get_config
from multiquery.api.endpoints import query, history, export
from multiquery.utils.mongodb_client import get_mongo_collection
from multiquery.config.config import AppConfig

# Create the FastAPI application
app = FastAPI(title="Multiquery API", version="0.1.0")

#Include API routers
app.include_router(query.router, prefix="/query", tags=["Query"])
app.include_router(history.router, prefix="/history", tags=["History"])
app.include_router(export.router, prefix="/export", tags=["Export"])

# Define startup event
@app.on_event("startup")
async def startup_event():
    """
    Actions to perform at application startup.
    """
    # Directly call get_config to load the configuration
    config = get_config()
    
    # Log loaded configuration
    print(f"Loaded configuration: {config}")

    # Debug database connection
    db_config = config.database
    print(f"Connecting to database {db_config.db_name} at {db_config.uri}")
    print(f"Using collection: {db_config.collection_name}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


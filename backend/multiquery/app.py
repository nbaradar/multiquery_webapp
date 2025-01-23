from fastapi import FastAPI
from multiquery.config.config_loader import get_config
from multiquery.api.endpoints import query, history, export
from fastapi.middleware.cors import CORSMiddleware
# uvicorn multiquery.app:app --reload
# Create the FastAPI application
app = FastAPI(title="Multiquery API", version="0.1.0")

# Add CORS middleware to your FastAPI app:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
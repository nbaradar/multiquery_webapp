import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to a file
        logging.StreamHandler(),        # Output logs to the console
    ],
)
logger = logging.getLogger(__name__)

# Log Every Request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log incoming request details
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        # Log the request body (if any)
        body = await request.json()
        logger.info(f"Request body: {body}")
    except Exception:
        logger.info("No request body")

    # Call the next middleware or endpoint
    response = await call_next(request)

    # Log response status code
    logger.info(f"Response status: {response.status_code}")
    return response

#Log Errors
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.error(f"HTTP Exception: {exc.detail} - Path: {request.url.path}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation Error: {exc.errors()} - Path: {request.url.path}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
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
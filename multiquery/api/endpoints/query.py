from fastapi import APIRouter, Depends
from pydantic import BaseModel
from multiquery.utils.config_loader import get_config
from multiquery.core.services.llm_service import run_query
from multiquery.utils.mongodb_client import get_mongo_collection
from multiquery.utils.config_loader import instantiate_providers

router = APIRouter()

class QueryRequest(BaseModel):
    prompt: str

@router.post("/")
async def query_api(
    request: QueryRequest,       # Accept request body as a pydantic model 
    config=Depends(get_config),  # Inject config dependency
    collection=Depends(get_mongo_collection)
):
    """
    Handle query requests, run through LLMs and store the results in MongoDB.
    """
    #Extract prompt from request
    prompt = request.prompt

    #Instantiate Providers (reuse existing instance in real-world apps)
    providers = instantiate_providers(config)

    #Run the query using existing logic
    responses = await run_query(prompt, providers)

    #Store results in MongoDB
    result = {
        "prompt": prompt,
        "responses": responses
    }
    collection.insert_one(result)

    return {"prompt": prompt, "responses": responses}
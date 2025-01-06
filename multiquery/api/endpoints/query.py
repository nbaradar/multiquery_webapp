from fastapi import APIRouter, Depends
from pydantic import BaseModel
from multiquery.config.config_loader import get_config
from multiquery.core.services.llm_service import run_query
from multiquery.utils.mongodb_client import get_mongo_collection
from multiquery.config.config_loader import instantiate_providers

router = APIRouter()

class QueryRequest(BaseModel):
    prompt: str

@router.post("/")
async def query_api(
    request: QueryRequest,       # Accept request body as a pydantic model 
    collection=Depends(get_mongo_collection)
):
    """
    Handle query requests, run through LLMs and store the results in MongoDB.
    """
    #Extract prompt from request
    prompt = request.prompt

    #Run the query using existing logic
    responses = await run_query(prompt)

    #Store results in MongoDB
    result = {
        "prompt": prompt,
        "responses": responses
    }
    collection.insert_one(result)

    return {"prompt": prompt, "responses": responses}
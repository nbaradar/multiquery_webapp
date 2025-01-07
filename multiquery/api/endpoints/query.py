from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from multiquery.core.services.llm_service import run_query
from multiquery.utils.mongodb_client import get_mongo_collection
from multiquery.llm_providers.provider_factory import ProviderFactory
from typing import Optional
from multiquery.api.dependencies import get_provider_factory
import asyncio

router = APIRouter()

class QueryRequest(BaseModel):
    #The users query to the LLM. JSON request body.
    prompt: str

@router.post("/")
async def query_api(
    # JSON body for the prompt
    request: QueryRequest,  
    # Optional query params
    model: Optional[str] = Query(None), 
    max_tokens: Optional[int] = Query(None),
    temperature: Optional[float] = Query(None),
    factory: ProviderFactory = Depends(get_provider_factory),  # Injected factory
    # Optional parameter for filtering providers
    context_type: str = None  
):

    """
    Handle query requests using dynamically instantiated providers.
    Clients can override provider settings via query parameters.
    """
    #Create providers dynamically
    providers = factory.create_providers()

    #Extract prompt from request
    prompt = request.prompt

    #Define tasks for concurrent execution
    tasks = []

    # Override LLM configs if provided as query parameters in request. 
    # Then, add the task for the provider's `send_query` method
    for provider in providers:
        # Retrieve the provider's default configuration
        provider_config = provider.config

        # Override default settings with query params
        if model:
            provider_config["model"] = model
        if max_tokens:
            provider_config["max_tokens"] = max_tokens
        if temperature:
            provider_config["temperature"] = temperature

        # Add the task for the provider's `send_query` method
        tasks.append(provider.send_query(request.prompt, **provider_config))

    # Run all tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Collect responses from all the LLM tasks
    responses = {}
    for provider, result in zip(providers, results):
        provider_name = provider.__class__.__name__
        if isinstance(result, Exception):
            responses[provider_name] = f"Error: {str(result)}"
        else:
            responses[provider_name] = result

    result = {
        "prompt": prompt,
        "responses": responses
    }

    #TODO: Store results in MongoDB
    #get_mongo_collection.insert_one(result)

    return {"prompt": prompt, "responses": responses}
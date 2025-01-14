from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from backend.multiquery.core.services.llm_service import run_query
from backend.multiquery.core.services.query_db_service import save_query_result
from backend.multiquery.utils.mongodb_client import get_mongo_client, MongoDBClient
from backend.multiquery.llm_providers.provider_factory import ProviderFactory
from typing import Optional
from backend.multiquery.api.dependencies import get_provider_factory
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
    llm_provider: Optional[str] = Query(None),

    # Injected factory
    factory: ProviderFactory = Depends(get_provider_factory), 
    # Inject MongoDB client 
    mongo_client: MongoDBClient = Depends(get_mongo_client),  
    # Optional parameter for filtering providers
    context_type: str = None  
):

    """
    Handle query requests using dynamically instantiated providers.
    Clients can override provider settings via query parameters.
    """
    #Create providers dynamically
    providers = []
    #providers = factory.create_providers()

    #Extract prompt from request
    prompt = request.prompt

    #Define tasks for concurrent execution
    tasks = []

    if llm_provider:
        provider_names = llm_provider.split(",")
        for provider_name in provider_names:
            providers.append(factory.create_provider(provider_name)) 
        for provider in providers:
            tasks.append(provider.send_query(request.prompt))
    else:
        # Override LLM configs if provided as query parameters in request. 
        # Then, add the task for the provider's `send_query` method
        providers = factory.create_providers()
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
    #TODO THE LOGIC ISSUE IS HERE. YOU ARE PROBABLY LOOPING THROUGH ALL THE 
    # PROVIDERS FOR THE NAMES INSTEAD OF PICKING THE NAME FROM THE CORRESPONDING USED PROVIDER
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

    # Save the result to MongoDB
    collection = mongo_client.get_collection("result")
    inserted_id = await save_query_result(collection, request.prompt, responses)
    print(f"Saved query result to MongoDB with ID: {inserted_id}")

    return {"prompt": prompt, "responses": responses}
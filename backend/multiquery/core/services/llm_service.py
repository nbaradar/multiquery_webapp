from typing import Dict
from multiquery.llm_providers.provider_factory import ProviderFactory
from multiquery.api.dependencies import get_provider_factory
import asyncio

async def run_query(prompt: str, factory: ProviderFactory) -> Dict[str, str]:
    """
    Run the query through all configured LLM providers.

    :param prompt: The user's query.
    :param config: The application configuration (AppConfig instance).
    :return: A dictionary of provider names and their responses.
    """
    # Use Dependency Injection to get config instead of reloading
    providers = factory.create_providers()

    # Run queries concurrently
    tasks = [provider.send_query(prompt) for provider in providers]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Collect responses
    responses = {}
    for provider, result in zip(providers, responses):
        provider_name = provider.__class__.__name__
        if isinstance(result, Exception):
            responses[provider_name] = f"Error: {str(result)}"
        else:
            responses[provider_name] = result

    return responses
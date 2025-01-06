from multiquery.llm_providers.chatgpt import ChatGPTProvider
from multiquery.llm_providers.grok import GrokProvider
from multiquery.config.config_loader import instantiate_providers
from multiquery.config.config_loader import get_config
import asyncio

async def run_query(prompt: str) -> dict[str, str]:
    """
    Run the query through all configured LLM providers.

    :param prompt: The user's query.
    :param config: The application configuration (AppConfig instance).
    :return: A dictionary of provider names and their responses.
    """
    # Use Dependency Injection to get config instead of reloading
    config = get_config()
    providers = instantiate_providers(config)

    # Extracts LLM specific configurations from App Config
    llm_configs = {llm.name: llm for llm in config.llm_configs}

    # Run querys concurrently
    # tasks = [provider.send_query(prompt) for provider in providers]
    # results = await asyncio.gather(*tasks, return_exceptions=True)

    # Run queries concurrently
    tasks = []
    for provider in providers:
        provider_config = llm_configs.get(provider.__class__.__name__.lower(), {})
        tasks.append(provider.send_query(prompt, **provider_config.dict()))


    # Collect responses
    responses = {}
    for provider, result in zip(providers, responses):
        provider_name = provider.__class__.__name__
        if isinstance(result, Exception):
            responses[provider_name] = f"Error: {str(result)}"
        else:
            responses[provider_name] = result

    return responses
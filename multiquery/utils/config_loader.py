# File: multiquery/utils/config_loader.py

import yaml
import importlib
from multiquery.core.config import AppConfig

def load_config(file_path: str) -> AppConfig:
    """
    Loads the configuration file and returns it as a dictionary. The file should be in YAML format.

    :param file_path: Path to the configuration file (YAML format)
    """
    with open(file_path, "r") as file:
        raw_config = yaml.safe_load(file)
    return AppConfig(**raw_config)

#Use FastAPIs dependency injection to pass the configuration to the API routers
def get_config():
    """
    Provide the application configuration as a dependency.
    """
    return load_config("multiquery/config/config.yaml")

def instantiate_providers(config: dict):
    """
    Dynamically instantiates LLM providers based on the configuration.
    """
    providers = []
    for provider_config in config.llm_providers:
        # Dynamically import the provider class
        module_name, class_name = provider_config.class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        provider_class = getattr(module, class_name)

        # Instantiate the provider with API keys if available
        api_key = provider_config.api_key
        provider_instance = provider_class(api_key) if api_key else provider_class()  # Pass API key if required
        providers.append(provider_instance)
    return providers

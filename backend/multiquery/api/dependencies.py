from fastapi import Depends
from multiquery.llm_providers.provider_factory import ProviderFactory
from multiquery.config.config_loader import get_config

def get_provider_factory(config=Depends(get_config)) -> ProviderFactory:
    """
    Provides a pre-configured ProviderFactory instance as a dependency.
    """
    return ProviderFactory(config)
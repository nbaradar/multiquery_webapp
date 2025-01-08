import importlib
from typing import List, Optional
from multiquery.config.config import AppConfig
from multiquery.llm_providers.base import LLMProvider 

class ProviderFactory:
    """
    Factory class for dynamically creating and managing LLM providers.
    """
    def __init__(self, config: AppConfig):
        self.config = config
        self._cache = {}  # Optional: Cache instantiated providers

    def create_providers(self, context_type: Optional[str] = None) -> List[LLMProvider]:
        """
        Create and return a list of LLM providers based on the configuration.
        
        :param context_type: The context type to filter the providers by.This will be expanded on in the future
        :return: A list of instantiated providers
        """
        #First, instantiate a list that will hold instantiated providers
        providers = []

        #Then, use config file settings to loop through and create objects of each provider
        for llm_provider in self.config.llm_provider:
            #Debugging statements
            print(f"Creating provider: {llm_provider.name}")

            #TODO Going to implement filtering based on context_type later. (Data, Writing, Image, Audio, etc)
            if context_type and llm_provider.name != context_type:
                continue

            # Check cache (if caching is enabled)
            if llm_provider.name in self._cache:
                providers.append(self._cache[llm_provider.name])
                continue

            #Extract the class path from the config
            llm_provider_module_path, llm_provider_class_name = llm_provider.class_path.rsplit(".", 1)
            #Then, use importlib to dynamically import the module (which is our llm_provider class)
            module = importlib.import_module(llm_provider_module_path)
            #Finally, grab the ACTUAL CLASS OBJECT (for example, ChatGPTProvider) from the loaded module (multiquery.llm_providers.chatgpt) using the Class Name (ChatGPTProvider)
            provider_classname = getattr(module, llm_provider_class_name)

            #Now, instantiate the llm_provider class with appropriate and necessary configs
            #TODO This is probably where you want to expand the logic for dynamically instantiating providers based on needs (like context_type value)
            #Grab API key for provider
            api_key = llm_provider.api_key

            #Grab llm configurations for the provider
            provider_settings = llm_provider.config
            
            #Create provider instance 
            provider_instance = provider_classname(api_key, **provider_settings.dict())
            providers.append(provider_instance)

            # Cache the provider instance (optional)
            self._cache[llm_provider.name] = provider_instance

        return providers

    #TODO Need to implement caching for the rest of these providers
    def create_provider(self, provider_name: str) -> LLMProvider:
        """
        Create an LLM provider instance based on the provider name.

        :param provider_name: Name of the provider to create.
        :return: An instance of the specified provider.
        """
        if provider_name.lower() == "chatgpt":
            return self.create_chatgpt_provider()
        elif provider_name.lower() == "gemini":
            return self.create_gemini_provider()
        elif provider_name.lower() == "grok":
            return self.create_grok_provider()
        else:
            raise ValueError(f"Unknown provider: {provider_name}")

    def create_chatgpt_provider(self) -> LLMProvider:
        """
        Create and return a ChatGPT provider instance.
        """
        llm_provider = next(
            (p for p in self.config.llm_provider if p.name.lower() == "chatgpt"), None
        )
        if not llm_provider:
            raise ValueError("ChatGPT provider configuration not found.")
        module = importlib.import_module(llm_provider.class_path.rsplit(".", 1)[0])
        provider_class = getattr(module, llm_provider.class_path.rsplit(".", 1)[1])
        return provider_class(llm_provider.api_key, **llm_provider.config.dict())
    
    def create_gemini_provider(self) -> LLMProvider:
        """
        Create and return a Gemini provider instance.
        """
        llm_provider = next(
            (p for p in self.config.llm_provider if p.name.lower() == "gemini"), None
        )
        if not llm_provider:
            raise ValueError("Gemini provider configuration not found.")
        module = importlib.import_module(llm_provider.class_path.rsplit(".", 1)[0])
        provider_class = getattr(module, llm_provider.class_path.rsplit(".", 1)[1])
        return provider_class(llm_provider.api_key, **llm_provider.config.dict())

    def create_grok_provider(self) -> LLMProvider:
        """
        Create and return a Grok provider instance.
        """
        llm_provider = next(
            (p for p in self.config.llm_provider if p.name.lower() == "grok"), None
        )
        if not llm_provider:
            raise ValueError("Grok provider configuration not found.")
        module = importlib.import_module(llm_provider.class_path.rsplit(".", 1)[0])
        provider_class = getattr(module, llm_provider.class_path.rsplit(".", 1)[1])
        return provider_class(llm_provider.api_key, **llm_provider.config.dict())

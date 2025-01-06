import importlib
from typing import List, Optional
from multiquery.config.config import AppConfig

class ProviderFactory:
    def __init__(self, config: AppConfig):
        self.config = config

    def create_providers(self, context_type: Optional[str] = None) -> List:
        """
        Create and return a list of LLM providers based on the configuration.
        
        :param context_type: The context type to filter the providers by.This will be expanded on in the future
        :return: A list of instantiated providers
        """

        #First, instantiate a list that will hold instantiated providers
        providers = []

        #Then, use config file settings to loop through and create objects of each provider
        for llm_provider in self.config.llm_providers:
            #Debugging statements
            print(f"Creating provider: {llm_provider.name}")

            #Extract the class path from the config
            llm_provider_module_path, llm_provider_class_name = llm_provider.class_path.rsplit(".", 1)
            #Then, use importlib to dynamically import the module (which is our llm_provider class)
            module = importlib.import_module(llm_provider_module_path)
            #Finally, grab the ACTUAL CLASS OBJECT (for example, ChatGPTProvider) from the loaded module (multiquery.llm_providers.chatgpt) using the Class Name (ChatGPTProvider)
            provider_classname = getattr(module, llm_provider_class_name)

            #Now, instantiate the llm_provider class with appropriate and necessary configs
            #TODO This is probably where you want to expand the logic for dynamically instantiating providers based on needs (like context_type value)
            api_key = llm_provider.api_key
            
            #Create provider instance 
            provider_instance = provider_classname(api_key)
            providers.append(provider_instance)

        return providers



from .base import LLMProvider
from typing import List, Optional
from openai import OpenAI
from openai import AsyncOpenAI
import aiohttp
class ChatGPTProvider(LLMProvider):

    def __init__(self, api_key: str, **config):
        """
        Initializes the ChatGPTProvider with the necessary configuration.
        
        :param api_key: API key for authenticating with the ChatGPT service.
        :param configs: Additional configurations.
        """
        self.api_key = api_key
        self.provider_name = "ChatGPT"
        self.config = config

    async def send_query(self, query: str, **overrides) -> str:
        """
        Send a query to ChatGPT asynchronously, with optional overrides for model settings.
        
        :param prompt: The user's query.
        :param overrides: Configuration overrides (e.g., model, max_tokens).
        :return: The response text from ChatGPT (String).
        """

        # Merge default config with overrides
        config = {**self.config, **overrides}

        # Ensure the API key is set
        if self.api_key == "YOUR_API_KEY":
            return "Error: " + self.provider_name + " API key is not configured."
        

        #First create a client and set the API key (retrieved from config file)
        client = AsyncOpenAI(
            api_key=self.api_key
        )

        #Now attempt to make a call to REST API
        try:
            chat_completion = await client.chat.completions.create(
                model=config["model"],
                messages=[
                    {
                    "role": "user",
                    "content": query,
                    },
                ],
                temperature=config["temperature"],  # Adjust for creativity
                max_tokens=config["max_tokens"],   # Limit response length
            )
            return chat_completion.choices[0].message.content
        except Exception as e: 
            return f"Error: {e}"
from .base import LLMProvider
import google.generativeai as genai


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str, **config):
        """
        Initializes the Gemini Provider with the necessary configuration.
        
        :param api_key: API key for authenticating with the ChatGPT service.
        :param configs: Additional configurations.
        """
        self.api_key = api_key
        self.provider_name = "Gemini"
        self.config = config
 
    async def send_query(self, query: str, **overrides) -> str:
        """
        Sends a query to Gemini and returns the response.
        """

        # Merge default config with overrides
        config = {**self.config, **overrides}

        # Ensure the API key is set
        if self.api_key == "YOUR_API_KEY":
            return "Error: " + self.provider_name + " API key is not configured."
        
        try:
            #Set API Key and model
            genai.configure(api_key=self.api_key)
            generationConfig = {
                "temperature": config["temperature"],
                #TODO: Figure out how to set max_tokens. 
                # see here: https://ai.google.dev/api/generate-content#generationconfig 
                # and here: https://github.com/google-gemini/cookbook/blob/18bb4f2bd03c66839dc388bb1e9ae7e7819b1cd0/quickstarts/New_in_002.ipynb#L220
                #"maxOutputTokens": 100
            }
            model = genai.GenerativeModel(config["model"], generation_config=generationConfig)
            

            #Query Gemini
            response = await model.generate_content_async(query)
            return response.text
        except Exception as e:
            return f"Error: {e}"
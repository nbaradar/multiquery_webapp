from pydantic import BaseModel
from typing import List, Dict, Optional 

class LLMConfig(BaseModel):
    model: str
    max_tokens: int
    temperature: float

class LLMProviderConfig(BaseModel):
    name: str
    class_path: str
    api_key: Optional[str]
    config: LLMConfig #Reference to a named config in llm_configs

class DatabaseConfig(BaseModel):
    uri: str
    db_name: str
    collection_name: str

class AppConfig(BaseModel):
    llm_provider: List[LLMProviderConfig]  #List of LLM Providers
    database: DatabaseConfig  #Database configs
# File: multiquery/core/config.py

from pydantic import BaseModel
from typing import List, Dict, Optional 

class LLMProviderConfig(BaseModel):
    name: str
    class_path: str
    api_key: Optional[str]

class LLMConfig(BaseModel):
    name: str
    model: str
    max_tokens: int
    temperature: float

class DatabaseConfig(BaseModel):
    name: str
    uri: str
    db_name: str
    collection_name: str

class AppConfig(BaseModel):
    llm_providers: List[LLMProviderConfig]
    llm_configs: List[LLMConfig]
    database_configs: List[DatabaseConfig]

#settings = Settings()
import yaml
import importlib
from multiquery.config.config import AppConfig

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
from fastapi import Depends
from multiquery.app import get_config
from multiquery.core.config import AppConfig
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_history():
    return {"message": "This is the export endpoint"}

def export_to_json(file_path: str, query: str, responses: dict, config: AppConfig = Depends(get_config)):
    """
    Exports data to JSON with injected configuration.
    """
    # Example: Use config if needed for metadata or default paths
    data = {
        "query": query,
        "responses": responses,
        "export_path": config.database_configs[0].collection_name,  # Example usage
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

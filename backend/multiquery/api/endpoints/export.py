from fastapi import Depends

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_history():
    return {"message": "This is the export endpoint"}


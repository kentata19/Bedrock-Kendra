from fastapi import APIRouter
from services import QueryProcessorService as QueryProcessor

router = APIRouter()


@router.get("/query")
async def query(query: str) -> str:
    response = QueryProcessor(query).process()
    return response

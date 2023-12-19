from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

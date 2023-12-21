from fastapi import FastAPI
from routers import query

app = FastAPI()
app.include_router(query.router)

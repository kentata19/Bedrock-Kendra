from pydantic import BaseModel

# Request


# Response


class KendraResponse(BaseModel):
    content: str
    document_uri: str

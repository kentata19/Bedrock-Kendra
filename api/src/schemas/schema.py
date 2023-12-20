import json

from pydantic import BaseModel


# Request
class BedrockRequest(BaseModel):
    prompt: str
    max_tokens_to_sample: int = 500

    def json(self) -> str:
        return json.dumps(
            {
                "prompt": self.prompt,
                "max_tokens_to_sample": self.max_tokens_to_sample,
            }
        )


# Response


class KendraResponse(BaseModel):
    content: str
    document_uri: str

import json
from dataclasses import dataclass

import boto3
from common import settings


class BedrockService:
    def __init__(self) -> None:
        self.client = boto3.client(
            "bedrock-runtime",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name="us-east-1",
        )

    @dataclass(slots=True)
    class RequestBody:
        prompt: str
        max_tokens_to_sample: int = 500

        def json(self) -> str:
            return json.dumps(
                {
                    "prompt": self.prompt,
                    "max_tokens_to_sample": self.max_tokens_to_sample,
                }
            )

    def call_endpoint(self, body: RequestBody) -> str:
        response = self.client.invoke_model(
            body=body.json(),
            modelId="anthropic.claude-v2",
            contentType="application/json",
            accept="application/json",
        )
        return response["body"].read().decode("utf-8")

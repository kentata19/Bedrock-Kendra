import boto3
from common import settings
from schemas import BedrockRequest


class BedrockService:
    def __init__(self, prompt: str) -> None:
        self.prompt = prompt
        self.client = boto3.client(
            "bedrock-runtime",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name="us-east-1",
        )

    def call_endpoint(self) -> str:
        body = BedrockRequest(prompt=self.prompt)
        response = self.client.invoke_model(
            body=body.json(),
            modelId="anthropic.claude-v2",
            contentType="application/json",
            accept="application/json",
        )
        return response["body"].read().decode("utf-8")

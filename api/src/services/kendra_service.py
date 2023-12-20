import boto3
from common import settings
from schemas import KendraResponse


class KendraService:
    def __init__(self) -> None:
        self.client = boto3.client(
            "kendra",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name="us-east-1",
        )

    def search(self, query: str) -> list[KendraResponse]:
        response = self.client.retrieve(
            QueryText=query,
            IndexId=settings.KENDRA_INDEX_ID,
            AttributeFilter={
                "EqualsTo": {
                    "Key": "_language_code",
                    "Value": {"StringValue": "ja"},
                },
            },
        )
        results = response["ResultItems"][:3] if response["ResultItems"] else []

        extracted_results = [
            KendraResponse(
                content=item.get("Content"), document_uri=item.get("DocumentURI")
            )
            for item in results
            if item.get("Content")
        ]

        return extracted_results

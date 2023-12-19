import boto3
from common import settings


class KendraService:
    def __init__(self) -> None:
        self.client = boto3.client(
            "kendra",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name="us-east-1",
        )

    # TODO: returnをschemaで管理する
    def search(self, query: str) -> list[dict[str, str]]:
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
            {
                "Content": item.get("Content"),
                "DocumentURI": item.get("DocumentURI"),
            }
            for item in results
        ]
        return extracted_results

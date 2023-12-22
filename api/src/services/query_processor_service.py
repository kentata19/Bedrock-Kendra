from services import BedrockService, KendraService, PromptCreatorService


class QueryProcessorService:
    def __init__(self, query: str) -> None:
        self.query = query
        self.kendra_service = KendraService()
        self.bedrock_service = BedrockService()

    # Step1: Kendraにクエリを投げて、関連する文書を取得する
    # Step2: 取得した文書をもとにpromptを生成する
    # Step3: Bedrockにpromptを投げて、回答を取得する
    def process(self) -> str:
        kendra_response = self.kendra_service.search(self.query)
        contents = [response.content for response in kendra_response]
        formatted_content = self.__format_content(contents)
        prompt = PromptCreatorService(
            content=formatted_content, query=self.query
        ).create_prompt()
        bedrock_response = self.bedrock_service.call_endpoint(
            prompt=prompt, query=self.query
        )
        return bedrock_response

    @staticmethod
    def __format_content(content: list[str]) -> str:
        formatted_content = [
            f"<document index={index}>{content}</document>"
            for index, content in enumerate(content, start=1)
        ]
        concatted_content = f"""
        <documents>
        {formatted_content}
        </documents>
        """

        return concatted_content

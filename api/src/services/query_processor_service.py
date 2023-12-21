from services import BedrockService, KendraService, PromptCreatorService


class QueryProcessorService:
    def __init__(self, query: str) -> None:
        self.query = query

    # Step1: Kendraにクエリを投げて、関連する文書を取得する
    # Step2: 取得した文書をもとにpromptを生成する
    # Step3: Bedrockにpromptを投げて、回答を取得する
    def process(self) -> str:
        kendra_response = KendraService().search(self.query)
        contents = [response.content for response in kendra_response]
        formatted_content = self.__format_content(contents)
        prompt = PromptCreatorService(
            query=self.query, content=formatted_content
        ).create_prompt()
        bedrock_response = BedrockService(prompt=prompt).call_endpoint()
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

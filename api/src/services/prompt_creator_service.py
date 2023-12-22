from langchain.prompts import PromptTemplate


class PromptCreatorService:
    def __init__(self, content: str, query: str) -> None:
        self.content = content
        self.query = query

    def create_prompt(self) -> PromptTemplate:
        template = f"""以下の文書を参考にしつつ、質問に専門的に答えてください。

            <document>
            {self.__remove_braces(self.content)}
            </document>

            あなたは経験豊富なエンジニアであり、深い技術的な知識を持っています。
            質問に答える際は、その技術的な専門知識を前面に出し、文書の関連情報を適切に引用して補強してください。

            回答は以下のフォーマットに従ってください。

            <example>
            関連する引用:
            [1] "X社は2021年に1200万ドルの収益を計上した"
            [2] "収益のほぼ90%はウィジェットの販売によるもので、残りの10%はガジェットの販売によるものである。"

            回答:
            X社は1,200万ドルの収入を得た[1]。 そのほぼ90%はウィジェットの販売によるものである[2]。
            </example>

            このフォーマットに従って、あなたの専門知識と文書の情報をバランス良く組み合わせて質問に答えてください。

            以下が質問です: {self.query}

            ChatHistory: {{chat_history}}
            \nHuman: {{Query}}


            \nAssistant:"""
        return PromptTemplate(
            input_variables=["chat_history", "Query"], template=template
        )

    @staticmethod
    def __remove_braces(text: str) -> str:
        return text.replace("{", "").replace("}", "")

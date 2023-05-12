from langchain.chains import LLMChain as LangchainLLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

class LLMChain(LangchainLLMChain):
    def __init__(self, llm: ChatOpenAI = ChatOpenAI()):
        human_message_prompt = HumanMessagePromptTemplate(
            prompt = PromptTemplate(
                template="{message}",
                input_variables=["message"],
            )
        )

        prompt = ChatPromptTemplate.from_messages([human_message_prompt])
        super().__init__(llm=llm, prompt=prompt)

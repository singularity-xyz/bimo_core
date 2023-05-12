from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain import OpenAI

from .base_chain import BaseChain

class QAChain(BaseChain):
    def __init__(self, llm: ChatOpenAI = OpenAI(temperature=0)):
        self.llm = llm

        human_message_prompt = HumanMessagePromptTemplate(
            prompt = PromptTemplate(
                input_variables=["question"],
                template="please answer the following question: {question}"
            )
        )

        self.prompt = ChatPromptTemplate.from_messages([human_message_prompt])
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def run(self, question: str):
        return self.chain.run({"question": question})
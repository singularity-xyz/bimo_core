from langchain.chains import LLMChain as LangchainLLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

class LLMChain(LangchainLLMChain):
    def __init__(
        self,
        llm: ChatOpenAI = ChatOpenAI(),
        chat_prompt: ChatPromptTemplate = None,
    ):
        if chat_prompt is None:
            human_message_prompt_template = PromptTemplate(
                template="{human_message}",
                input_variables=["human_message"],
            )
            human_message_prompt = HumanMessagePromptTemplate(prompt=human_message_prompt_template)

            system_message_prompt_template = PromptTemplate(
                template="{system_message}",
                input_variables=["system_message"],
            )
            system_message_prompt = SystemMessagePromptTemplate(prompt=system_message_prompt_template)

            ai_message_prompt_template = PromptTemplate(
                template="{ai_message}",
                input_variables=["ai_message"],
            )
            ai_message_prompt = AIMessagePromptTemplate(prompt=ai_message_prompt_template)

            chat_prompt = ChatPromptTemplate.from_messages([
                human_message_prompt,
                system_message_prompt,
                ai_message_prompt,
            ])

        super().__init__(llm=llm, prompt=chat_prompt)

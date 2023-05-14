"""
Brief summary of the class's purpose.

Detailed explanation of the class's behavior, its role within the larger application, and how it interacts with other classes or data.

Parameters
----------
param1 : type
    Description of param1, including any constraints or required formats.
param2 : type
    Description of param2, including any constraints or required formats.
...

Attributes
----------
attr1 : type
    Description of attr1, including any default values.
attr2 : type
    Description of attr2, including any default values.
...

Methods
-------
method1
    Brief description of method1.
method2
    Brief description of method2.
...

Example
-------
>>> ClassName(param1, param2)
Expected result

Notes
-----
Any additional notes on the class's usage within the broader application.
"""

from langchain.chains import LLMChain as LangchainLLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from prompts.human_message import default

class LLMChain(LangchainLLMChain):
    def __init__(
        self,
        llm: ChatOpenAI = ChatOpenAI(),
        chat_prompt: ChatPromptTemplate = None,
    ):
        if chat_prompt is None:
            human_message_prompt = HumanMessagePromptTemplate(prompt=default)

            chat_prompt = ChatPromptTemplate.from_messages([
                human_message_prompt
            ])

        super().__init__(llm=llm, prompt=chat_prompt)

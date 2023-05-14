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

from langchain.chains import RetrievalQA, combine_documents
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import OpenAI


class QAChain(RetrievalQA):
    def __init__(self, retriever, llm: ChatOpenAI = OpenAI(temperature=0)):
        template = "You are a helpful assistant named momo that provides helpful information to people based on the provided document."
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template="{message}",
                input_variables=["message"],
            )
        )

        prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

        combine_document_chain = load_qa_with_sources_chain(llm, chain_type="stuff")
        super().__init__(combine_documents_chain=combine_document_chain, retriever=retriever)

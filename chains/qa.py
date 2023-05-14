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

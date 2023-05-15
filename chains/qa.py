"""
    This class extends LangChain's ConversationalRetrievalChain for question/answering over a document.

    Con formats the prompt template with the input key values (and memory key values, if available),
    passes the formatted string to LLM, and returns the LLM output.

    Args:
        llm (ChatOpenAI, optional):
            A ChatOpenAI instance for language model interaction.
        chat_prompt (ChatPromptTemplate, optional):
            A ChatPromptTemplate instance for generating prompts.

    Attributes:
        llm (OpenAI):
            The OpenAI instance to use for generating text.
        retriever:
            The retriever object used to access the document.

    Methods:
        run(input: dict) -> string:
            Takes in a question and chat_history and uses those to generate a condensed question to
            answer over the document. Returns an answer with sources listed. 
"""

from langchain.chains import ConversationalRetrievalChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain import OpenAI
from .llm import LLMChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from utils import logging


class QAChain(ConversationalRetrievalChain):
    def __init__(
        self, 
        retriever, 
        llm: OpenAI = OpenAI(verbose=True, temperature=0)
    ):
        question_generator = LLMChain(llm=llm, chat_prompt=CONDENSE_QUESTION_PROMPT)
        combine_docs_chain = load_qa_with_sources_chain(llm, chain_type="map_reduce")

        super().__init__(combine_docs_chain=combine_docs_chain, question_generator=question_generator, retriever=retriever)
        logging.info(f"Initialized QAChain.")

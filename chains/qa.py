from .llm import LLMChain
from utils import logging
from typing import Any, Dict, Optional
from langchain.schema import BaseRetriever
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.prompts.base import BasePromptTemplate
from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.chains.qa_with_sources.base import QAWithSourcesChain
from langchain.chains import QAWithSourcesChain as LangchainQAWithSourcesChain
from langchain.chains.base import Chain
from langchain.chains.base import Chain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
import inspect


# I think for naming consistency, this should be called ConversationRetrievalChain not QAChain,
# unless we want to start deviating from the LangChain class names that we have been using.
class QAChain(Chain):
    # def __init__(
    #     self, # I used what you had and reformated the init to match the from_llm() function inside ConversationalRetrievalChain
    #     llm: BaseLanguageModel = ChatOpenAI(verbose=True), # like alternatively we could just use ChatOpenAI
    #     #prompt: BasePromptTemplate = CONDENSE_QUESTION_PROMPT,  May need to keep this as default at this level bc different chain_types have different default prompts I think thats why they have a function to initialize
    #     chain_type: str = "stuff",
    #     verbose: bool = False,
    #     #sources: bool = True,
    #     combine_docs_chain_kwargs: Optional[Dict] = None,
    #     **kwargs: Any,
    # ):
    #     combine_docs_chain_kwargs = combine_docs_chain_kwargs or {}
    #     # if(sources):
    #     #     combine_documents_chain = load_qa_with_sources_chain(
    #     #         llm,
    #     #         chain_type=chain_type,
    #     #         verbose=verbose,
    #     #         **combine_docs_chain_kwargs,
    #     #     )
    #     # else:
    #     #     combine_documents_chain = load_qa_chain(
    #     #         llm,
    #     #         chain_type=chain_type,
    #     #         verbose=verbose,
    #     #         **combine_docs_chain_kwargs,
    #     #     )

    #     combine_documents_chain = load_qa_with_sources_chain(
    #             llm,
    #             chain_type=chain_type,
    #             verbose=verbose,
    #             **combine_docs_chain_kwargs,
    #         )
    #     self = combine_documents_chain
    #     logging.info(f"Initialized QAChain with {combine_documents_chain}.")

    def __new__(
        self, 
        llm: BaseLanguageModel = ChatOpenAI(verbose=True), 
        chain_type: str = "stuff", 
        sources: bool = True, 
        verbose: bool = True
    ):
        """
        Creates a new QAChain instance.

        :param sources: If True, loads the QA chain with sources; if False, loads the QA chain without sources.
        :return: An instance of the QAChain.
        """
        if sources:
            return load_qa_with_sources_chain(llm, chain_type=chain_type, verbose=verbose)
        else:
            return load_qa_chain(llm, chain_type=chain_type, verbose=verbose)


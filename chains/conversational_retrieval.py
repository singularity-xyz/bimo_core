from .llm import LLMChain
from .qa import QAChain
from utils import logging
from typing import Any, Dict, Optional
from langchain.schema import BaseRetriever
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.prompts.base import BasePromptTemplate
from langchain.chains import ConversationalRetrievalChain as LangchainConversationalRetrievalChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from langchain.chains.base import Chain


# I think for naming consistency, this should be called ConversationRetrievalChain not QAChain,
# unless we want to start deviating from the LangChain class names that we have been using.
class ConversationalRetrievalChain(LangchainConversationalRetrievalChain):
    """
    This class extends LangChain's ConversationalRetrievalChain for question/answering over a document.

    Con formats the prompt template with the input key values (and memory key values, if available),
    passes the formatted string to LLM, and returns the LLM output.

    Args:
        retriever (BaseRetriever):
            A BaseRetriever instance for retrieving documents.
        combine_docs_chain (BaseChain):
            A BaseChain instance for combining documents.
        llm (BaseLanguageModel, optional):
            A BaseLanguageModel instance for language model interaction.
        condense_question_prompt (BasePromptTemplate, optional):
            A BasePromptTemplate instance for generating prompts.
        chain_type (str, optional):
            The type of chain to use for combining documents.
        verbose (bool, optional):
            Whether to print debug information.
        combine_docs_chain_kwargs (dict, optional):
            Keyword arguments to pass to the combine_docs_chain constructor.
        kwargs (dict, optional):
            Keyword arguments to pass to the ConversationalRetrievalChain constructor.

    Attributes:
        retriever (BaseRetriever):
            The BaseRetriever instance to use for retrieving documents.
        combine_docs_chain (BaseChain):
            The BaseChain instance to use for combining documents.
        question_generator (BaseChain):
            The BaseChain instance to use for generating questions.
    """
    
    def __init__(
        self, # I used what you had and reformated the init to match the from_llm() function inside ConversationalRetrievalChain
        retriever: BaseRetriever, # not really sure if we should be using Base classes or not as the type...
        llm: BaseLanguageModel = ChatOpenAI(verbose=True), # like alternatively we could just use ChatOpenAI
        condense_question_prompt: BasePromptTemplate = CONDENSE_QUESTION_PROMPT,
        chain_type: str = "stuff",
        verbose: bool = False,
        combine_docs_chain_kwargs: Optional[Dict] = None,
        **kwargs: Any,
    ):
        combine_docs_chain_kwargs = combine_docs_chain_kwargs or {}
        doc_chain = QAChain(
            llm,
            chain_type=chain_type,
            verbose=verbose,
            **combine_docs_chain_kwargs,
        )

        condense_question_chain = LLMChain(
            llm=llm, 
            prompt=condense_question_prompt, 
            verbose=verbose
        )

        super().__init__(
            retriever=retriever,
            combine_docs_chain=doc_chain,
            question_generator=condense_question_chain,
            **kwargs,
        )
        logging.info(f"Initialized ConversationalRetrievalChain with {self.retriever} and {self.combine_docs_chain} and {self.question_generator}.")





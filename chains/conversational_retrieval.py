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


class ConversationalRetrievalChain(LangchainConversationalRetrievalChain):
    """
    An extension of the `ConversationalRetrievalChain` class from langchain. This class is used to perform question/answering 
    over documents passed in as a retriever.

    Args:
        retriever (BaseRetriever): 
            An instance of a retriever class used to retrieve relevant documents.
        llm (BaseLanguageModel, optional): 
            An instance of a language model. Default is `ChatOpenAI(verbose=True)`.
        condense_question_prompt (BasePromptTemplate, optional): 
            An instance of a prompt template. Default is `CONDENSE_QUESTION_PROMPT`.
        chain_type (str, optional): 
            Type of the chain. Default is "stuff".
        verbose (bool, optional): 
            If True, verbose mode is activated. Default is False.
        with_sources (bool, optional):  
            If True, sources will be included in the responses. Default is True.
        combine_docs_chain_kwargs (Optional[Dict], optional): 
            Additional keyword arguments to be passed to the `QAChain` instantiation. Default is None.
        **kwargs (Any, optional): 
            Additional keyword arguments to be passed to the `load_qa_with_sources_chain` or `load_qa_chain` functions.

    Attributes:
        retriever (BaseRetriever): 
            The retriever instance used in the chain.
        combine_docs_chain (QAChain): 
            The QAChain instance used in the chain.
        question_generator (LLMChain): 
            The LLMChain instance used to generate the questions.

    Methods:
        run(input: dict) -> dict:
            Similar to __call__, formats the prompt using the input and passes it to the LLM.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        llm: BaseLanguageModel = ChatOpenAI(verbose=True),
        condense_question_prompt: BasePromptTemplate = CONDENSE_QUESTION_PROMPT,
        chain_type: str = "stuff",
        verbose: bool = False,
        with_sources: bool = True,
        combine_docs_chain_kwargs: Optional[Dict] = None,
        **kwargs: Any,
    ):
        combine_docs_chain_kwargs = combine_docs_chain_kwargs or {}

        doc_chain = QAChain(
            llm=llm,
            chain_type=chain_type,
            verbose=verbose,
            with_sources=with_sources,
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





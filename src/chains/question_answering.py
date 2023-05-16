from src.utils import logging
from typing import Any, Optional
from langchain.chains.base import Chain
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackManager
from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain


class QAChain:
    """
    A factory class that returns an instance of a BaseCombineDocumentsChain. Depending on the `with_sources` argument,
    this factory class will return either a BaseCombineDocumentsChain that includes sources or doesn't.

    This class does not actually implement the methods of a chain, but rather delegates the creation
    of a chain to either `load_qa_with_sources_chain` or `load_qa_chain` based on the parameters passed.

    Args:
        llm (BaseLanguageModel, optional): 
            An instance of a language model. Default is `ChatOpenAI(verbose=True)`.
        chain_type (str, optional): 
            Type of the chain. Default is "stuff".
        verbose (Optional[bool], optional): 
            If True, verbose mode is activated. Default is False.
        with_sources (bool, optional): 
            If True, sources will be included in the QA chain. Default is True.
        callback_manager (Optional[BaseCallbackManager], optional): 
            An instance of a callback manager. Default is None.
        **kwargs (Any, optional): 
            Additional keyword arguments to be passed to the `load_qa_with_sources_chain` or `load_qa_chain` functions.

    Returns:
        An instance of a BaseCombineDocumentsChain.
    """

    def __new__(
        self,
        llm: BaseLanguageModel = ChatOpenAI(verbose=True),
        chain_type: str = "stuff",
        verbose: Optional[bool] = False,
        with_sources: bool = True,
        callback_manager: Optional[BaseCallbackManager] = None,
        **kwargs: Any,
    ):
        if with_sources:
            logging.info(f"Initalizing QAChain with sources and {chain_type} chain.")
            return load_qa_with_sources_chain(  
                llm=llm,
                chain_type=chain_type,
                verbose=verbose,
                **kwargs,
            )
        else:
            logging.info(f"Initalizing QAChain without sources and {chain_type} chain.")
            return load_qa_chain(
                llm=llm,
                chain_type=chain_type,
                verbose=verbose,
                callback_manager=callback_manager,
                **kwargs,
            )

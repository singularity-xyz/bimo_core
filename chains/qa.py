from typing import Any, Optional
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackManager
from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain


class QAChain:
    def __init__(
        self,
        chain_type: str,
        llm: BaseLanguageModel = ChatOpenAI(verbose=True),
        verbose: Optional[bool] = None,
        with_sources: bool = False,
        callback_manager: Optional[BaseCallbackManager] = None,
        **kwargs: Any,
    ):
        self.llm = llm
        self.chain_type = chain_type
        self.verbose = verbose
        self.with_sources = with_sources
        self.callback_manager = callback_manager
        self.kwargs = kwargs
        self.chain = self._load_chain()

    def _load_chain(self):
        if self.with_sources:
            return load_qa_with_sources_chain(
                llm=self.llm,
                chain_type=self.chain_type,
                verbose=self.verbose,
                **self.kwargs,
            )
        else:
            return load_qa_chain(
                llm=self.llm,
                chain_type=self.chain_type,
                verbose=self.verbose,
                callback_manager=self.callback_manager,
                **self.kwargs,
            )

    def run(self, **kwargs):
        return self.chain.run(**kwargs)

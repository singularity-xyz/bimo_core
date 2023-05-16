from langchain.chains import LLMChain as LangchainLLMChain
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.prompts.base import BasePromptTemplate
# from langchain.prompts.chat import ChatPromptTemplate
# need custom ChatPromptTemplate to resolve _prompt_type error
from src.prompts import default_human_message_prompt, ChatPromptTemplate
from src.utils import logging


class LLMChain(LangchainLLMChain):
    """
    This class extends LangChain's LLMChain for querying an LLM object using a prompt template and input key values.

    LLMChain formats the prompt template with the input key values (and memory key values, if available),
    passes the formatted string to LLM, and returns the LLM output.

    Args:
        llm (ChatOpenAI, optional):
            A ChatOpenAI instance for language model interaction.
        chat_prompt (ChatPromptTemplate, optional):
            A ChatPromptTemplate instance for generating prompts.
        verbose (Bool, optional):
            If True, verbose mode is activated. Default is False.

    Attributes:
        llm (ChatOpenAI):
            The ChatOpenAI instance to use for generating text.
        prompt (ChatPromptTemplate):
            The ChatPromptTemplate instance to format with input key values.
    """

    def __init__(
        self,
        llm: BaseLanguageModel = ChatOpenAI(verbose=True),
        prompt: BasePromptTemplate = ChatPromptTemplate.from_messages([default_human_message_prompt]),
        verbose: bool = False
    ):
        super().__init__(llm=llm, prompt=prompt, verbose=verbose)
        logging.info(f"Initialized LLMChain with {self.llm.model_name} and {self.prompt.input_variables}.")

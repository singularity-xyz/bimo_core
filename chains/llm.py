from langchain.chains import LLMChain as LangchainLLMChain
from langchain.chat_models import ChatOpenAI
from langchain.base_language import BaseLanguageModel
from langchain.prompts.base import BasePromptTemplate
# from langchain.prompts.chat import ChatPromptTemplate
# need custom ChatPromptTemplate to resolve _prompt_type error
from prompts import default_human_message_prompt, ChatPromptTemplate
from utils import logging


class LLMChain(LangchainLLMChain):
    r"""
    This class extends LangChain's LLMChain for querying an LLM object using a prompt template and input key values.

    LLMChain formats the prompt template with the input key values (and memory key values, if available),
    passes the formatted string to LLM, and returns the LLM output.

    Args:
        llm (ChatOpenAI, optional):
            A ChatOpenAI instance for language model interaction.
        chat_prompt (ChatPromptTemplate, optional):
            A ChatPromptTemplate instance for generating prompts.

    Attributes:
        llm (ChatOpenAI):
            The ChatOpenAI instance to use for generating text.
        prompt (ChatPromptTemplate):
            The ChatPromptTemplate instance to format with input key values.

    Methods:
        __call__(input: dict) -> dict:
            Formats the prompt using the input and passes it to the LLM.

        run(input: dict) -> dict:
            Similar to __call__, formats the prompt using the input and passes it to the LLM.

        apply(input_list: list[dict]) -> list[dict]:
            Formats the prompt using each dict in input_list and passes them to the LLM.

        generate(input_list: list[dict]) -> LLMResult:
            Similar to apply, but returns an LLMResult instead of a list of strings.

        predict(\*\*kwargs) -> str:
            Formats the prompt using the kwargs and passes it to the LLM.

        predict_and_parse(\*\*kwargs) -> Any:
            Similar to predict, but also applies the output parser on the LLM output.

        apply_and_parse(input_list: list[dict]) -> list[Any]:
            Similar to apply, but also applies the output parser on each LLM output.

        from_string(llm: OpenAI, template: str) -> LLMChain:
            Constructs an LLMChain from a string template.
    """

    def __init__(
        self,
        llm: ChatOpenAI = ChatOpenAI(verbose=True),
        prompt: BasePromptTemplate = ChatPromptTemplate.from_messages([default_human_message_prompt]),
        verbose: bool = True
    ):
        super().__init__(llm=llm, prompt=prompt, verbose=verbose)
        logging.info(f"Initialized LLMChain with {self.llm.model_name} and {self.prompt.input_variables}.")

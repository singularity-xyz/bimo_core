from typing import Any, List

from pydantic import BaseModel

from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.chains.openai_functions.utils import (
    _convert_schema,
    _resolve_schema_references,
    get_llm_kwargs,
)
from langchain.output_parsers.openai_functions import (
    JsonKeyOutputFunctionsParser,
    PydanticAttrOutputFunctionsParser,
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema.language_model import BaseLanguageModel


def _get_extraction_function(entity_schema: dict) -> dict:
    return {
        "name": "information_extraction",
        "description": "Extracts the relevant information from the passage.",
        "parameters": {
            "type": "object",
            "properties": {
                "info": {"type": "array", "items": _convert_schema(entity_schema)}
            },
            "required": ["info"],
        },
    }


# _EXTRACTION_TEMPLATE = """Extract and save the relevant entities mentioned\
#  in the following passage together with their properties.

# Passage:
# {input}
# """

_EXTRACTION_TEMPLATE = """Extract and save assignments and exams mentioned\
 in the following university class syllabus together with their properties. An assignment\
 is anything the student has to submit for a grade, such as a project, essay, or homework.\
 An exam is a quiz, midterm, or final exam. For each assignment and exam, save the following\
 properties: name, description, due date, and weightage.

Syllabus:
{input}
"""

def create_extraction_chain(schema: dict, llm: BaseLanguageModel) -> Chain:
    """Creates a chain that extracts information from a passage.

    Args:
        schema: The schema of the entities to extract.
        llm: The language model to use.

    Returns:
        Chain that can be used to extract information from a passage.
    """
    function = _get_extraction_function(schema)
    prompt = ChatPromptTemplate.from_template(_EXTRACTION_TEMPLATE)
    output_parser = JsonKeyOutputFunctionsParser(key_name="info")
    llm_kwargs = get_llm_kwargs(function)
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        llm_kwargs=llm_kwargs,
        output_parser=output_parser,
    )
    return chain


def create_extraction_chain_pydantic(
    pydantic_schema: Any, llm: BaseLanguageModel, prompt_template: str = _EXTRACTION_TEMPLATE
) -> Chain:
    """Creates a chain that extracts information from a passage using pydantic schema.

    Args:
        pydantic_schema: The pydantic schema of the entities to extract.
        llm: The language model to use.

    Returns:
        Chain that can be used to extract information from a passage.
    """

    class PydanticSchema(BaseModel):
        info: List[pydantic_schema]  # type: ignore

    openai_schema = pydantic_schema.schema()
    openai_schema = _resolve_schema_references(
        openai_schema, openai_schema.get("definitions", {})
    )

    function = _get_extraction_function(openai_schema)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    output_parser = PydanticAttrOutputFunctionsParser(
        pydantic_schema=PydanticSchema, attr_name="info"
    )
    llm_kwargs = get_llm_kwargs(function)
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        llm_kwargs=llm_kwargs,
        output_parser=output_parser,
    )
    return chain
    
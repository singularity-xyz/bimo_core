

from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)

from langchain.prompts import PromptTemplate

default = PromptTemplate(
            template="{human_message}",
            input_variables=["human_message"],
        )
from langchain.chains import create_extraction_chain_pydantic
from langchain.chat_models import ChatOpenAI

from typing import Optional
from pydantic import BaseModel, Field

class Properties(BaseModel):
    person_name: str
    person_height: int
    person_hair_color: str
    dog_breed: Optional[str]
    dog_name: Optional[str]

class SyllabusExtractionChain:
    def __init__(self, schema: BaseModel = Properties, llm: ChatOpenAI = ChatOpenAI()):
        self.chain = create_extraction_chain_pydantic(llm=llm, pydantic_schema=schema)

    def __getattr__(self, name):
        # If the attribute isn't found in SyllabusExtractionChain, look for it in self.chain
        return getattr(self.chain, name)

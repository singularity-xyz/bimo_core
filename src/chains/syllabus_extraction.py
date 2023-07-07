from langchain.chains import create_extraction_chain_pydantic
from langchain.chat_models import ChatOpenAI

from typing import Optional, List
from pydantic import BaseModel, Field

class School(BaseModel):
    id: str
    name: str

class Course(BaseModel):
    id: str
    course_code: str
    name: str
    department: str
    professor_name: Optional[str]
    professor_email: Optional[str]
    description: Optional[str]
    school: School

class Assignment(BaseModel):
    id: str
    name: str
    due_date: str
    description: Optional[str]
    priority: Optional[int]
    completed: Optional[bool]

class Document(BaseModel):
    id: str
    name: str
    type: str
    url: str

class Exam(BaseModel):
    id: str
    name: str
    start_time: str
    end_time: Optional[str]
    description: Optional[str]
    priority: Optional[int]

class Task(BaseModel):
    id: str
    name: str
    date: str
    description: Optional[str]
    priority: Optional[int]
    completed: Optional[bool]

class UserCourse(BaseModel):
    course: Course
    assignments: List[Assignment] = []
    documents: List[Document] = []
    exams: List[Exam] = []
    tasks: List[Task] = []


class SEChain:
    def __init__(self, schema: BaseModel = UserCourse, llm: ChatOpenAI = ChatOpenAI(model="gpt-3.5-turbo-16k")):
        self.chain = create_extraction_chain_pydantic(llm=llm, pydantic_schema=schema)

    def __getattr__(self, name):
        # If the attribute isn't found in SyllabusExtractionChain, look for it in self.chain
        return getattr(self.chain, name)

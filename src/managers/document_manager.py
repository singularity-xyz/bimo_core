"""
1. Upload document file to the database
2. Get document file from the database
3. Split document file into chunks
4. Generate embeddings and add to the vectorstore
6. Generate a retriever from the vectorstore    
"""

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.schema import BaseRetriever


class DocumentManager:
    def __init__(self):
        self.db = None # some mongo db connection instance
        self.vector_store = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())

    def upload_document(self, user_id: str, class_id: str, document_id: str) -> None:
        self.generate_embeddings(user_id, class_id, document_id)

    def get_document(self, user_id: str, class_id: str, document_id: str) -> None:
        pass
        
    def generate_embeddings(self, user_id: str, class_id: str, document_id: str) -> None:
        file_path = f"./{user_id}/{class_id}/{document_id}"
        loader = PyPDFLoader(file_path)
        documents = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        self.vector_store.add_documents(texts)

    def get_db(self) -> DeepLake:
        return self.vector_store

    def get_retriever(self) -> BaseRetriever:
        return self.vector_store.as_retriever()

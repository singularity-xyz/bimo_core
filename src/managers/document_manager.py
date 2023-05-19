"""
1. Upload document file to the database
2. Get document file from the database
3. Split document file into chunks
4. Generate embeddings and add to the vectorstore
6. Generate a retriever from the vectorstore    
"""

import uuid

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import BaseRetriever
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake
from momoai_core.src.utils import GCSClient
from langchain.vectorstores import DeepLake

class DocumentMetadata:
    id: uuid
    user_id: uuid
    name: str
    class_name: str = None

class DocumentManager:
    def __init__(self, gcs: GCSClient, vector_store: DeepLake):
        self.gcs = gcs 
        self.vector_store = vector_store

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

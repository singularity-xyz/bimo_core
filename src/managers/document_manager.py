"""
1. Upload document file to the database
2. Get document file from the database
3. Split document file into chunks
4. Generate embeddings and add to the vectorstore
6. Generate a retriever from the vectorstore    
"""

import uuid
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

from langchain.schema import BaseRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake
from momoai_core.src.utils import GCSClient


class DocumentMetadata:
    id: uuid
    user_id: uuid
    name: str = None
    class_name: str = None


class DocumentManager:
    def __init__(self, gcs_client: GCSClient=None, vector_store: DeepLake=None):
        self.gcs_client = gcs_client or GCSClient(bucket_name="momo-ai")
        self.vector_store = vector_store or DeepLake(dataset_path="deeplake_dataset", embedding_function=OpenAIEmbeddings())

    def _generate_blob_name(self, document_metadata: DocumentMetadata) -> str:
        return f"{document_metadata.user_id}/{document_metadata.id}"

    def _upload_embeddings(self, document_metadata: DocumentMetadata, file_content) -> None:
        reader = PdfReader(file_content)
        documents = reader.pages
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        self.vector_store.add_documents(texts)

    def upload_document(self, document_metadata: DocumentMetadata, file_content) -> None:
        destination_blob_name = self._generate_blob_name(document_metadata)
        self.gcs_client.upload_blob(file_content, destination_blob_name)
        self._upload_embeddings(document_metadata, file_content)

    def get_document(self, document_metadata: DocumentMetadata) -> None:
        blob_name = self._generate_blob_name(document_metadata)
        return self.gcs_client.download_blob(blob_name)

    def get_vector_store(self) -> DeepLake:
        return self.vector_store

    def get_retriever(self) -> BaseRetriever:
        return self.vector_store.as_retriever()

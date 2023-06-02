import uuid
import tempfile
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from typing import List

from langchain.schema import BaseRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake
from momoai_core.src.utils import GCSClient
from dataclasses import dataclass
import uuid

@dataclass
class DocumentMetadata:
    id: uuid.UUID
    user_id: uuid.UUID
    name: str = None


class DocumentManager:
    def __init__(self, gcs_client: GCSClient=None, vector_store: DeepLake=None):
        self.gcs_client = gcs_client or GCSClient(bucket_name="momo-ai")
        self.vector_store = vector_store or DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())

    # somewhere in here we need to add the metadata to mongo db
    def upload_document(self, document_metadata: DocumentMetadata, file_content: BytesIO) -> None:
        destination_blob_name = self._generate_blob_name(document_metadata)
        self.gcs_client.upload_blob(file_content, destination_blob_name)
        # After uploading the blob, reset the position of the file content
        file_content.seek(0)
        self._upload_embeddings(document_metadata, file_content)

    def get_document(self, document_metadata: DocumentMetadata) -> None:
        blob_name = self._generate_blob_name(document_metadata)
        return self.gcs_client.download_blob(blob_name)
    
    def get_document_retriever(self, user_id: uuid.uuid4, document_metadatas: List[DocumentMetadata]) -> BaseRetriever:
        retriever = self._get_retriever()
    
        if len(document_metadatas) == 0:
            def filter(x):
                metadata = x['metadata'].data()['value']
                if str(user_id) == metadata['user_id']:
                    return True
        else:
            def filter(x):
                metadata = x['metadata'].data()['value']

                for document_metadata in document_metadatas:
                    if (str(document_metadata.id) == metadata['document_id']) and (str(user_id) == metadata['user_id']):
                        return True
                
        retriever.search_kwargs["filter"] =  filter
            
        return retriever


    def get_vector_store(self) -> DeepLake:
        return self.vector_store

    def _get_retriever(self) -> BaseRetriever:
        return self.vector_store.as_retriever()

    def _generate_blob_name(self, document_metadata: DocumentMetadata) -> str:
        return f"{document_metadata.user_id}/{document_metadata.id}/{document_metadata.name}"

    def _upload_embeddings(self, document_metadata: DocumentMetadata, file_content: BytesIO) -> None:
        # Create a temporary file and save the content of the BytesIO object to it
        with tempfile.NamedTemporaryFile(delete=True) as temp:
            temp.write(file_content.read())
            temp.flush()  # Ensure all data is written to the file

            loader = PyPDFLoader(temp.name)
            documents = loader.load_and_split()

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)

            for text in texts:
                text.metadata["document_id"] = str(document_metadata.id)
                text.metadata["user_id"] = str(document_metadata.user_id)
                text.metadata["name"] = str(document_metadata.name)

            self.vector_store.add_documents(texts)

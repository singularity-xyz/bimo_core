import uuid
import tempfile
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

    def get_vector_store(self) -> DeepLake:
        return self.vector_store

    def get_retriever(self) -> BaseRetriever:
        return self.vector_store.as_retriever()

    def _generate_blob_name(self, document_metadata: DocumentMetadata) -> str:
        return f"{document_metadata.user_id}/{document_metadata.id}"

    def _upload_embeddings(self, document_metadata: DocumentMetadata, file_content: BytesIO) -> None:
        # Create a temporary file and save the content of the BytesIO object to it
        with tempfile.NamedTemporaryFile(delete=True) as temp:
            temp.write(file_content.read())
            temp.flush()  # Ensure all data is written to the file

            loader = PyPDFLoader(temp.name)
            documents = loader.load_and_split()

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)

            self.vector_store.add_documents(texts)

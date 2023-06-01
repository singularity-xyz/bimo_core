import pytest
import uuid
from io import BytesIO
from unittest.mock import MagicMock
from momoai_core.src.utils import GCSClient
from langchain.vectorstores import DeepLake
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

from momoai_core import DocumentManager, DocumentMetadata  # adjust import as needed


@pytest.fixture
def document_manager():
    gcs_client = GCSClient(bucket_name="momo-ai")
    vector_store = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())
    return DocumentManager(gcs_client=gcs_client, vector_store=vector_store)


@pytest.fixture
def document_metadata():
    return DocumentMetadata(
        id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="test_document.pdf",
        class_name="TestDocument"
    )


def test_upload_document(document_manager, document_metadata):
    file_content = BytesIO(b"Some test content")

    # Mocking GCSClient and DeepLake's methods
    document_manager.gcs_client.upload_blob = MagicMock()
    document_manager._upload_embeddings = MagicMock()
    file_content.seek = MagicMock()

    document_manager.upload_document(document_metadata, file_content)

    # Verifying that the methods were called
    document_manager.gcs_client.upload_blob.assert_called_once()
    document_manager._upload_embeddings.assert_called_once()
    file_content.seek.assert_called_once_with(0)


def test_get_document(document_manager, document_metadata):
    # Mocking GCSClient's download_blob method
    document_manager.gcs_client.download_blob = MagicMock(return_value=BytesIO(b"Some test content"))

    result = document_manager.get_document(document_metadata)

    # Verifying that the methods were called
    document_manager.gcs_client.download_blob.assert_called_once()
    assert isinstance(result, BytesIO)


def test_get_document_retriever(document_manager, document_metadata):
    # Mocking vector store's as_retriever method
    document_manager._get_retriever = MagicMock()
    
    result = document_manager.get_document_retriever([document_metadata])

    # Verifying that the methods were called
    document_manager._get_retriever.assert_called_once()


def test_get_vector_store(document_manager):
    result = document_manager.get_vector_store()

    assert isinstance(result, DeepLake)


def test_generate_blob_name(document_manager, document_metadata):
    result = document_manager._generate_blob_name(document_metadata)

    assert result == f"{document_metadata.user_id}/{document_metadata.id}/{document_metadata.name}"


def test_upload_embeddings(document_manager, document_metadata):
    file_content = BytesIO(b"Some test content")

    # Mocking DeepLake's add_documents method, PyPDFLoader's load_and_split method, and CharacterTextSplitter's split_documents method
    document_manager.vector_store.add_documents = MagicMock()
    PyPDFLoader.load_and_split = MagicMock(return_value=["document"])
    CharacterTextSplitter.split_documents = MagicMock(return_value=["text"])
    
    document_manager._upload_embeddings(document_metadata, file_content)
    
    # Verifying that the methods were called
    document_manager.vector_store.add_documents.assert_called_once()
    PyPDFLoader.load_and_split.assert_called_once()
    CharacterTextSplitter.split_documents.assert_called_once()

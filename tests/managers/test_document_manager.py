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
    document_metadata = DocumentMetadata(
        id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="Brendan_Morrison_Resume.pdf",
        class_name="Test Class"
    )


    document_manager.upload_document(document_metadata=document_metadata, file_content=open("./Brendan_Morrison_Resume.pdf", "rb"))

    retriever = document_manager.get_document_retriever([document_metadata])
   
    docs = retriever.get_relevant_documents("brendan")

    print(len(docs))

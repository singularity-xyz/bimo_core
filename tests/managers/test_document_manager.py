import pytest
import uuid
from io import BytesIO
from unittest.mock import MagicMock
from bimo_core.src.utils import GCSClient
from langchain.vectorstores import DeepLake
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

from bimo_core import DocumentManager, DocumentMetadata  # adjust import as needed


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
    )


def test_upload_document(document_manager: DocumentManager, document_metadata: DocumentMetadata):
    user_id = uuid.uuid4()

    document_metadata = DocumentMetadata(
        id=uuid.uuid4(),
        user_id=user_id,
        name="Brendan_Morrison_Resume.pdf",
    )


    document_manager.upload_document(document_metadata=document_metadata, file_content=open("./Brendan_Morrison_Resume.pdf", "rb"))

    retriever = document_manager.get_document_retriever(user_id=user_id, document_metadatas=[document_metadata])
   
    docs = retriever.get_relevant_documents("how large is the earth")

    print(len(docs))

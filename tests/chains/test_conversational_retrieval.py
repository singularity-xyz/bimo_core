from bimo_core import CRChain
from bimo_core import logging
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings


def test_conversational_retrieval():
    loader = TextLoader("tests/chains/test_document.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)

    chain = CRChain(retriever=docsearch.as_retriever(), verbose=True)
    message = "What is the name of the main character in the story? Please respond with only the name."
    response = chain.run({"question": message, "chat_history": []})

    assert isinstance(response, str)
    assert len(response) > 0
    assert "Elara" in response

    print() # for cleaner output
    logging.info("Message: %s", message)
    logging.info("Response: %s", response)
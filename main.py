from managers import ChainManager
from chains import ConversationalRetrievalChain

from chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from utils import logging

loader = TextLoader("tests/chains/test_document.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

chain_manager = ChainManager()

chain_manager.create_custom_chain("1", ConversationalRetrievalChain, retriever=docsearch.as_retriever(), with_sources=False)

conv_chain = chain_manager.get_chain("1")

print(conv_chain.run({"question": "What is the main characters name?", "chat_history": []}))
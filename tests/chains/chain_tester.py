import os
import logging
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import GoogleDriveLoader, PyPDFLoader
from langchain.memory import ConversationBufferMemory

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from chains import LLMChain
from chains.qa import QAChain
from managers import ChainManager

from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
loader = TextLoader("./doc.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

def main():
    chain_manager = ChainManager()

    chain_manager.add_chain(chain_id="1", chain=LLMChain)

    # chain_manager.mount_chain(chain_id="1")

    print(chain_manager.execute_chain(chain_id="1", inputs=['what is 2+2?']))

    print(chain_manager.get_loaded_chains())

if __name__ == "__main__":
    main()
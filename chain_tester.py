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

from chains.qa_chain import QAChain
from managers.chain_manager import ChainManager

chain_manager = ChainManager()

def main():
    chain_manager.add_chain(chain_id="1", chain=QAChain)

    chain_manager.mount_chain(chain_id="1")

    print(chain_manager.execute_chain(chain_id="1", inputs=["hello"]))

    print(chain_manager.get_loaded_chains())

if __name__ == "__main__":
    main()
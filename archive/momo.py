import os
import pickle
import logging
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import GoogleDriveLoader, PyPDFLoader, TextLoader
from langchain.memory import ConversationBufferMemory
import pickle

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] [%(name)s] %(message)s",
)

# Set up PyPDF Loader
#loader = PyPDFLoader("classes/CLAS-151/syllabus.pdf")
loader = TextLoader("./doc.txt")

# Load documents
logging.info("Loading documents...")
documents = loader.load_and_split()

# Split documents into chunks
logging.info("Splitting documents...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Generate embeddings and create vectorstore
logging.info("Generating embeddings...")
embeddings = OpenAIEmbeddings()
# db = DeepLake(dataset_path="deeplake", embedding_function=embeddings)
# db.add_documents(texts)
db = DeepLake(dataset_path="deeplake", embedding_function=embeddings, read_only=True)

def filter(x):
    return True

# Create retrieval chain
logging.info("Creating retrieval chain...")
model = ChatOpenAI()
retriever = db.as_retriever()
retriever.search_kwargs['filter'] = filter
qa = ConversationalRetrievalChain.from_llm(llm, retriever, verbose=True)

with open('test.pkl',  "wb") as file:
    pickle.dump(qa, file)

# Start chat loop
chat_history = []
while True:
    query = input("Enter your question (or 'exit'): ")
    if query.lower() == "exit":
        break
    
    result = qa({"question": query, "chat_history": chat_history}) 
    chat_history.append((query, result["answer"]))
    print("Answer:", result["answer"])
    

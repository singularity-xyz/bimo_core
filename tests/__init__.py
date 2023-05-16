import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OPENAI_API_KEY environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["MONGO_HOST"] = os.getenv("MONGO_HOST")
os.environ["MONGO_PORT"] = os.getenv("MONGO_PORT")
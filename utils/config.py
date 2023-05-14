import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OPENAI_API_KEY environment variable
def set_openai_api_key():
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OPENAI_API_KEY environment variable
def set_openai_api_key():
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        # logging.FileHandler("momo-ai.log")
    ]
)

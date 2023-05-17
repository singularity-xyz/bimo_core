import os
import pytest
from dotenv import load_dotenv
import sys

load_dotenv()

# Set OPENAI_API_KEY environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["MONGO_HOST"] = os.getenv("MONGO_HOST")
os.environ["MONGO_PORT"] = os.getenv("MONGO_PORT")

module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the module directory to the sys.path list
sys.path.append(module_dir)
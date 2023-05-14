"""
The chains module has implementations of various langchain chains to use.

This module is used to import chains and interact with them. Intended to be directlty 
utilized by the ChainManager class in the managers module. 

Classes
-------
LLMChain
    Used for basic interaction with LLM model.
QAChain
    Used for question/answering over documents.
...

Functions
---------
None

Variables
---------
None

Notes
-----
Any additional notes on the module's usage within the broader application.
"""

# Convenience imports
from llm import LLMChain
from qa import QAChain
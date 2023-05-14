"""
The managers module has implementations of various managers to use.

This module is used to import managers and abstract complexity of lower-level modules 
such as chains and tools. Intended to be directly utilized by the server. 

Classes
-------
ChainManager
    Used to manage, initialize, and interact with, chains defined in the chains module.
DocumentManager
    Used to index, store, and retreive both file-type documents and thier respective vector store objects.
ToolManager
    Used to manage, initialize, and interact with, tools defined in the tools module.
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
from .chain_manager import ChainManager
from .document_manager import DocumentManager
from .tool_manager import ToolManager
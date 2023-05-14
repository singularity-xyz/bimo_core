"""
Brief summary of the class's purpose.

Detailed explanation of the class's behavior, its role within the larger application, and how it interacts with other classes or data.

Parameters
----------
param1 : type
    Description of param1, including any constraints or required formats.
param2 : type
    Description of param2, including any constraints or required formats.
...

Attributes
----------
attr1 : type
    Description of attr1, including any default values.
attr2 : type
    Description of attr2, including any default values.
...

Methods
-------
method1
    Brief description of method1.
method2
    Brief description of method2.
...

Example
-------
>>> ClassName(param1, param2)
Expected result

Notes
-----
Any additional notes on the class's usage within the broader application.
"""

import pickle

class ChainManager:
    def __init__(self):
        # load global chains
        self.chains = {}

    def add_chain(self, chain_id: str, chain: type, chain_parameters: list=[]) -> None:
        # Initialize chain
        chain = chain(*chain_parameters)

        self.chains[chain_id] = chain

    def mount_chain(self, chain_id: str):
        # Load chain object to memory
        with open(f'{chain_id}.pkl', 'rb') as file:
            chain = pickle.load(file)

        self.chains[chain_id] = chain

    def unmount_chain(self, chain_id: str):
        # Remove chain object from memory
        del self.chains[chain_id]

    def execute_chain(self, chain_id: str, inputs: list=[]):
        if chain_id not in self.chains:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")
        return self.chains[chain_id].run(*inputs)

    def remove_chain(self, chain_id: str) -> None:
        pass

    def get_loaded_chains(self):
        return self.chains.keys()

from typing import Dict, List, Optional, Type
from chains import Chain, LLMChain


class ChainManager:
    def __init__(self):
        self.default_chains: Dict[str, Chain] = {
            "llm": LLMChain()
        }
        self.custom_chains: Dict[str, Chain] = {}

    def get_chain(self, chain_id: str) -> Optional[Chain]:
       """Returns the chain with the given chain_id, if it exists."""
       return self.default_chains.get(chain_id) or self.custom_chains.get(chain_id)

    def get_all_chains(self) -> Dict[str, Chain]:
        """Returns a dictionary of all chains, both default and custom."""
        return {**self.default_chains, **self.custom_chains}

    def get_all_chain_ids(self) -> List[str]:
       """Returns a list of all chain IDs, both default and custom."""
       return list(self.default_chains.keys()) + list(self.custom_chains.keys())

    def update_chain(self, chain_id: str, chain: Chain) -> None:
        """Updates the chain with the given chain_id, if it exists."""
        if chain_id in self.default_chains:
            self.default_chains[chain_id] = chain
        elif chain_id in self.custom_chains:
            self.custom_chains[chain_id] = chain
        else:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")

    def create_custom_chain(self, chain_id: str, chain_class: Type[Chain], *args, **kwargs) -> None:
        """Creates a custom chain with the given chain_id and chain_class."""
        if chain_id in self.default_chains or chain_id in self.custom_chains:
            raise ValueError(f"A chain with ID '{chain_id}' already exists.")
        chain = chain_class(*args, **kwargs)
        self.custom_chains[chain_id] = chain

    def delete_custom_chain(self, chain_id: str) -> None:
        """Deletes the custom chain with the given chain_id, if it exists."""
        if chain_id in self.custom_chains:
            del self.custom_chains[chain_id]
        else:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")

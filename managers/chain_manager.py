from typing import Dict, List, Optional, Type
from chains import Chain, LLMChain


class ChainManager:
    def __init__(self):
        self.default_chains: Dict[str, Chain] = {
            "llm": LLMChain(),
            # "router": RouterChain(),
            # "sequential": SequentialChain(),
            # "summary": SummaryChain(),
            # "transformer": TransformerChain(),
        }
        self.custom_chains: Dict[str, Chain] = {}

    def get_chain(self, chain_id: str) -> Optional[Chain]:
       """Returns the chain with the given chain_id, or None."""
       return self.default_chains.get(chain_id) or self.custom_chains.get(chain_id)

    def get_all_chains(self, chain_type: str = None) -> Dict[str, Chain]:
         """Returns a dictionary of chains: all. default, or custom."""
         if chain_type is None:
              return {**self.default_chains, **self.custom_chains}
         elif chain_type == "default":
              return self.default_chains
         elif chain_type == "custom":
              return self.custom_chains
         else:
              raise ValueError(f"Invalid chain type '{chain_type}'. Must be 'default' or 'custom' or None.")

    def get_all_chain_ids(self,  chain_type: str = None) -> List[str]:
        """Returns a list of chain IDs: all, default, or custom."""
        return list(self.get_all_chains(chain_type).keys())

    def update_chain(self, chain_id: str, chain: Chain) -> None:
        """Updates the chain with the given chain_id, if it exists."""
        if chain_id in self.default_chains:
            self.default_chains[chain_id] = chain
        elif chain_id in self.custom_chains:
            self.custom_chains[chain_id] = chain
        else:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")

    def create_custom_chain(self, chain_id: str, chain_class: Type[Chain], *args, **kwargs) -> Chain:
        """Creates a custom chain with the given chain_id and chain_class."""
        if chain_id in self.default_chains or chain_id in self.custom_chains:
            raise ValueError(f"A chain with ID '{chain_id}' already exists.")
        chain = chain_class(*args, **kwargs)
        self.custom_chains[chain_id] = chain
        return chain

    def delete_custom_chain(self, chain_id: str) -> None:
        """Deletes the custom chain with the given chain_id, if it exists."""
        if chain_id in self.custom_chains:
            del self.custom_chains[chain_id]
        else:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")

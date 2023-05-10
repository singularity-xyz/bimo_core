class ChainManager:
    def __init__(self):
        self.chains = {}

    def add_chain(self, chain_id: str, chain: Chain) -> None:
        if chain_id in self.chains:
            raise ValueError(f"Chain with ID '{chain_id}' already exists.")
        self.chains[chain_id] = chain

    def remove_chain(self, chain_id: str) -> None:
        if chain_id not in self.chains:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")
        del self.chains[chain_id]

    def execute_chain(self, chain_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        if chain_id not in self.chains:
            raise ValueError(f"Chain with ID '{chain_id}' not found.")
        return self.chains[chain_id].run(inputs)


class UserChainManager:
    def __init__(self):
        self.user_chains = {}

    def add_chain(self, user_id: str, chain_id: str, chain: Chain) -> None:
        if user_id not in self.user_chains:
            self.user_chains[user_id] = {}
        
        if chain_id in self.user_chains[user_id]:
            raise ValueError(f"Chain with ID '{chain_id}' already exists for user '{user_id}'.")
        
        self.user_chains[user_id][chain_id] = chain

    def remove_chain(self, user_id: str, chain_id: str) -> None:
        if user_id not in self.user_chains or chain_id not in self.user_chains[user_id]:
            raise ValueError(f"Chain with ID '{chain_id}' not found for user '{user_id}'.")
        
        del self.user_chains[user_id][chain_id]

    def execute_chain(self, user_id: str, chain_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        if user_id not in self.user_chains or chain_id not in self.user_chains[user_id]:
            raise ValueError(f"Chain with ID '{chain_id}' not found for user '{user_id}'.")
        
        return self.user_chains[user_id][chain_id].run(inputs)

    def load_user_chains(self, user_id: str) -> None:
        # Load user-specific chains from disk or database

    def save_user_chains(self, user_id: str) -> None:
        # Save user-specific chains to disk or database

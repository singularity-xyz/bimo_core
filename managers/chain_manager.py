import pickle

class ChainManager:
    def __init__(self):
        # load global chains
        self.chains = {}

    def add_chain(self, chain_id: str, chain: type, chain_parameters: list=[]) -> None:
        # Initialize chain
        chain = chain(*chain_parameters)

        # Save chain to file
        chain.save(f'{chain_id}.pkl')

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


# class UserChainManager:
#     def __init__(self):
#         self.user_chains = {}

#     def add_chain(self, user_id: str, chain_id: str, chain: Chain) -> None:
#         if user_id not in self.user_chains:
#             self.user_chains[user_id] = {}
        
#         if chain_id in self.user_chains[user_id]:
#             raise ValueError(f"Chain with ID '{chain_id}' already exists for user '{user_id}'.")
        
#         self.user_chains[user_id][chain_id] = chain

#     def remove_chain(self, user_id: str, chain_id: str) -> None:
#         if user_id not in self.user_chains or chain_id not in self.user_chains[user_id]:
#             raise ValueError(f"Chain with ID '{chain_id}' not found for user '{user_id}'.")
        
#         del self.user_chains[user_id][chain_id]

#     def execute_chain(self, user_id: str, chain_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
#         if user_id not in self.user_chains or chain_id not in self.user_chains[user_id]:
#             raise ValueError(f"Chain with ID '{chain_id}' not found for user '{user_id}'.")
        
#         return self.user_chains[user_id][chain_id].run(inputs)

#     def load_user_chains(self, user_id: str) -> None:
#         # Load user-specific chains from disk or database

#     def save_user_chains(self, user_id: str) -> None:
#         # Save user-specific chains to disk or database

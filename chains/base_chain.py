from abc import ABC, abstractmethod
import pickle

class BaseChain(ABC):
    # TODO: cofigure a global prompt "identity" that will be appended to other chain prompts to give GPT the identity of momo
    
    def __init__(self):
        print("abstract_init")
    
    @abstractmethod
    def run(self):
        pass 

    def save(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    # def load(self):
    #     with open(file_name, 'rb') as file:
    #         obj = pickle.load(file)

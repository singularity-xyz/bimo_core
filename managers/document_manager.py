import pickle

class DocumentManager:
    def __init__(self):
        self.documents = {}

    def add_document(self, document_id: str, document) -> None:
        pass

    def mount_document(self, document_id):
        pass

    def unmount_document(self, document_id):
        pass

    def remove_document(self, document_id):
        pass

    def get_loaded_documents(self):
        return self.documents.keys()
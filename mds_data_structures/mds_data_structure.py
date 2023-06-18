from abc import ABC, abstractmethod

class MDSDataStructure(ABC):
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def delete(self, index):
        pass

    @abstractmethod
    def visualize(self):
        pass

class MDSLinearDataStructure(MDSDataStructure):
    @abstractmethod
    def insert(self, index, value):
        pass

class MDSNonLinearDataStructure(MDSDataStructure):
    @abstractmethod
    def traverse(self):
        pass

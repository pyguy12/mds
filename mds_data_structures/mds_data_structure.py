from abc import ABC, abstractmethod

class MDSDataStructure(ABC):
    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __delitem__(self, index):
        pass

    @abstractmethod
    def visualize(self):
        pass

class MDSLinearDataStructure(MDSDataStructure):
    @abstractmethod
    def __setitem__(self, index, value):
        pass

    @abstractmethod
    def insert(self, index, value):
        pass

    @abstractmethod
    def append(self, value):
        pass

class MDSNonLinearDataStructure(MDSDataStructure):
    @abstractmethod
    def traverse(self):
        pass

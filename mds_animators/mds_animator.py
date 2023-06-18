from abc import ABC, abstractmethod

class MDSAnimator(ABC):
    @abstractmethod
    def animate_insertion(self, value, index=None):
        pass

    @abstractmethod
    def animate_deletion(self, index):
        pass

    @abstractmethod
    def animate_access(self, index):
        pass

    @abstractmethod
    def animate_reversal(self):
        pass

    # ...other operations...

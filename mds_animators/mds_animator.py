from abc import ABC, abstractmethod

class MDSAnimator(ABC):
    def __init__(self, scene):
        self.scene = scene

    @abstractmethod
    def animate_init(self, values):
        pass

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

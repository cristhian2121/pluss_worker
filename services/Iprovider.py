from abc import ABC, abstractmethod

class Abs_Provider_Entity(ABC):
    """Contructor of providers

    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getUrl(self):
        pass

    @abstractmethod
    def setUrl(self):
        pass

    @abstractmethod
    def getImageUrl(self):
        pass

    @abstractmethod
    def setImageUrl(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self):
        pass

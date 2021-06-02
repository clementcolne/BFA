from abc import ABC, abstractmethod


class Filtre(ABC):

    """
    @param self: objet de la classe
    @param action: Action sur laquelle on applique le filtre
    """
    @abstractmethod
    def process(self, action):
        pass

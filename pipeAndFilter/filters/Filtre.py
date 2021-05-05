from abc import ABC, abstractmethod


class Filtre(ABC):
    @abstractmethod
    def process(self, action):
        pass

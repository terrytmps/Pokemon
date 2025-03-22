from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_types(self):
        """
        Return the types of the pokemon
        """
        pass

    @abstractmethod
    def get_resistances(self):
        """ "
        Return the resistances of the pokemon
        """
        pass

    @abstractmethod
    def get_weaknesses(self):
        """
        Return the weaknesses of the pokemon
        """
        pass

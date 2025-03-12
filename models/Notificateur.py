from abc import ABC, abstractmethod


class Notificateur(ABC):
    """
    Interface pour tout notificateur.
    """

    @abstractmethod
    def notifier(self, alerte, priorite: str):
        pass

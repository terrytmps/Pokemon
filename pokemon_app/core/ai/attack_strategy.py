from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from pokemon_app.core.move import Move

if TYPE_CHECKING:
    from pokemon_app.core.battle import Battle


class AttackStrategy(ABC):
    """Interface for attack strategies"""

    @abstractmethod
    def choose_move(self, battle: "Battle") -> Move:
        pass

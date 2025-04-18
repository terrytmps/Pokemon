from pokemon_app.core.move import Move
from pokemon_app.core.ai.attack_strategy import AttackStrategy
import random
import typing

if typing.TYPE_CHECKING:
    from pokemon_app.core.battle import Battle


class RandomAttackStrategy(AttackStrategy):
    """Strategy that chooses a random move from the opponent's available moves."""

    def choose_move(self, battle: "Battle") -> Move:
        opponent = battle.opponent_pokemon
        available_moves = opponent.get_moves()

        valid_moves = [m for m in available_moves if m is not None]

        if not valid_moves:
            raise ValueError(f"{opponent.name} n'a aucune attaque valide!")

        chosen_move = random.choice(valid_moves)
        return chosen_move

from pokemon_app.core.ai.attack_strategy import AttackStrategy
import typing

if typing.TYPE_CHECKING:
    from pokemon_app.core.battle import Battle
from pokemon_app.core.move import Move


class HighestDamageStrategy(AttackStrategy):
    """Strategy that chooses the move that deals the most damage to the opponent."""

    def choose_move(self, battle: "Battle") -> Move:
        opponent = battle.opponent_pokemon
        player = battle.player_pokemon
        available_moves = opponent.get_moves()

        valid_moves = [m for m in available_moves if m is not None]

        if not valid_moves:
            raise ValueError(f"{opponent.name} n'a aucune attaque valide!")

        best_move = valid_moves[0]
        max_damage = -1

        try:
            max_damage = battle.calculate_damage(opponent, player, best_move)
        except Exception as e:
            print(f"Erreur calcul dégâts initiaux pour {best_move.name}: {e}")
            max_damage = -1

        for move in valid_moves[1:]:
            try:
                potential_damage = battle.calculate_damage(opponent, player, move)
                print(potential_damage)
                if potential_damage > max_damage:
                    max_damage = potential_damage
                    best_move = move
            except Exception as e:
                print(
                    f"Avertissement: Erreur calcul dégâts pour {move.name}: {e}. Ignorée."
                )
                continue
        return best_move

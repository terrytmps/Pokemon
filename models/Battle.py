from typing import List, Optional
import random

from models.Pokemon import Pokemon
from models.Move import Move
from models.enum.MoveCategory import MoveCategory
from models.status.BurnStatusStrategy import BurnStatusStrategy
from models.status.FreezeStatusStrategy import FreezeStatusStrategy
from models.status.NormalStatusStrategy import NormalStatusStrategy
from models.status.ParalysisStatusStrategy import ParalysisStatusStrategy
from models.status.PoisonStatusStrategy import PoisonStatusStrategy
from models.status.SleepStatusStrategy import SleepStatusStrategy
from models.status.StatusEnum import StatusEnum


class Battle:
    def __init__(self, player_pokemon: Pokemon, opponent_pokemon: Pokemon):
        """
        Initialize a battle between two Pokemon
        """
        self.player_pokemon: Pokemon = player_pokemon
        self.opponent_pokemon: Pokemon = opponent_pokemon
        self.turn_count: int = 0
        self.battle_log: List[str] = []

    def calculate_damage(self, attacker: Pokemon, defender: Pokemon, move: Move) -> int:
        """
        Calculate damage based on Pokemon battle mechanics
        """

        # Base damage calculation
        base_damage = move.power
        # if the type of the moves is one of the type of the attacker pokemon get bonus
        if move.move_type in [attacker.first_type, attacker.second_type]:
            base_damage *= 1.5

        # apply stat changes for status
        stat_attacker = attacker.status_strategy.stat_change(attacker)
        stat_defender = defender.status_strategy.stat_change(defender)

        # Attack and defense stat consideration
        if move.move_category == MoveCategory.PHYSICAL:
            attack_stat = stat_attacker.current_attack
            defense_stat = stat_defender.current_defense
        else:  # Special moves
            attack_stat = stat_attacker.current_attack_special
            defense_stat = stat_defender.current_defense_special

        # Damage calculation formula (simplified)
        damage = (
            base_damage * (attack_stat / defense_stat)
        )

        # Type effectiveness
        type_multiplier = 1.0

        # Check for immunities
        if move.move_type in defender.get_immunity():
            type_multiplier = 0.0
            self.battle_log.append(f"{defender.name} is immune to {move.move_type}!")
        else:
            # Check for weaknesses
            if move.move_type in defender.get_weaknesses():
                type_multiplier *= 2.0
                self.battle_log.append(f"It's super effective!")

            # Check for resistances
            if move.move_type in defender.get_resistances():
                type_multiplier *= 0.5
                self.battle_log.append(f"It's not very effective.")

        # Critical hit chance
        critical_chance = attacker.stat.current_speed / 512
        if random.random() < critical_chance:
            damage *= 1.5
            self.battle_log.append(f"Critical hit!")

        damage *= type_multiplier

        return max(1, int(damage))

    def check_accuracy(self, move: Move) -> bool:
        """
        Determine if a move hits based on its accuracy
        """
        return random.random() * 100 <= move.accuracy

    def apply_move_effects(self, attacker: Pokemon, defender: Pokemon, move: Move):
        """
        Appliquer les effets spéciaux de mouvement au-delà des dégâts
        """
        # Vérifier si le mouvement a un effet de statut
        if move.move_effect != StatusEnum.NORMAL:
            status_strategies = {
                StatusEnum.POISON: PoisonStatusStrategy(),
                StatusEnum.SLEEP: SleepStatusStrategy(),
                StatusEnum.BURN: BurnStatusStrategy(),
                StatusEnum.FREEZE: FreezeStatusStrategy(),
                StatusEnum.PARALYSIS: ParalysisStatusStrategy(),
                StatusEnum.NORMAL: NormalStatusStrategy()
            }
            
            defender.status_strategy = status_strategies.get(move.move_effect, NormalStatusStrategy())

            self.battle_log.append(f"{defender.name} is now {move.move_effect.name}!")

    def perform_attack(self, attacker: Pokemon, defender: Pokemon, move: Move) -> dict:
        """
        Execute a single attack
        """
        # Check if the attack hits
        if not self.check_accuracy(move):
            self.battle_log.append(f"{attacker.name}'s {move.name} missed!")
            return {"hit": False, "damage": 0}

        # Calculate and apply damage
        damage = self.calculate_damage(attacker, defender, move)

        if not attacker.status_strategy.attack():
            self.battle_log.append(f"{attacker.name} cant attack because of his status!")
            return {"hit": False, "damage": 0}

        # Reduce defender's HP
        defender.take_damage(damage)

        # Log the attack
        self.battle_log.append(
            f"{attacker.name} used {move.name} and dealt {damage} damage!"
        )

        # Apply any additional move effects
        self.apply_move_effects(attacker, defender, move)

        return {"hit": True, "damage": damage}

    def is_battle_over(self) -> bool:
        """
        Check if the battle has ended
        """
        # Probably not used but used by observer
        return (
            self.player_pokemon.get_current_hp() <= 0
            or self.opponent_pokemon.get_current_hp() <= 0
        )

    def get_battle_winner(self) -> Optional[Pokemon]:
        """
        Determine the winner of the battle
        """
        if self.player_pokemon.get_current_hp() <= 0:
            self.battle_log.append(f"{self.opponent_pokemon.name} wins!")
            return self.opponent_pokemon
        elif self.opponent_pokemon.get_current_hp() <= 0:
            self.battle_log.append(f"{self.player_pokemon.name} wins!")
            return self.player_pokemon
        return None


    def handle_end_of_turn(self, pokemon: Pokemon):
        """
        Gérer les effets de fin de tour pour un Pokémon
        """
        pokemon.status_strategy.end_turn(pokemon)
        if pokemon.get_current_hp() <= 0:
            self.battle_log.append(f"{pokemon.name} is KO")


    def battle_turn(self, player_move: Move, opponent_move: Move):
        """
        Execute a single battle turn
        """
        self.turn_count += 1

        # Determine turn order based on speed
        if (
            self.player_pokemon.status_strategy.stat_change(self.player_pokemon).current_speed
            >= self.opponent_pokemon.status_strategy.stat_change(self.opponent_pokemon).current_speed
        ):
            first_attacker, first_move = self.player_pokemon, player_move
            second_attacker, second_move = self.opponent_pokemon, opponent_move
        else:
            first_attacker, first_move = self.opponent_pokemon, opponent_move
            second_attacker, second_move = self.player_pokemon, player_move


        first_result = self.perform_attack(first_attacker, second_attacker, first_move)
        self.battle_log.append(str(first_result))

        # Check if battle is over after first attack
        if self.is_battle_over():
            return self.get_battle_winner()

        # Second Pokemon's attack
        second_result = self.perform_attack(
                second_attacker, first_attacker, second_move
            )
        self.battle_log.append(str(second_result))

        # Gérer les effets de fin de tour pour chaque Pokémon
        self.handle_end_of_turn(self.player_pokemon)
        self.handle_end_of_turn(self.opponent_pokemon)

        # Return winner if battle is over
        return self.get_battle_winner()

    def get_battle_log(self) -> List[str]:
        """
        Retrieve the battle log
        """
        logs = self.battle_log
        self.battle_log = []
        return logs

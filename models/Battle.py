from typing import List, Optional
import random

from models.Player import Player
from models.Pokemon import Pokemon
from models.Move import Move
from models.RoundGenerator import RoundGenerator
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
        self._player_pokemon: Pokemon = player_pokemon
        self.opponent_pokemon: Pokemon = opponent_pokemon
        self.turn_count: int = 0
        self.battle_log: List[str] = []

    @property
    def player_pokemon(self) -> Pokemon:
        return self._player_pokemon

    @player_pokemon.setter
    def player_pokemon(self, pokemon: Pokemon):
        self.battle_log.append(
            f"{self._player_pokemon.name} a été remplacé par  {pokemon.name}!"
        )
        self._player_pokemon = pokemon

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
        damage = base_damage * (attack_stat / defense_stat) * 0.6

        # Type effectiveness
        type_multiplier = 1.0

        # Check for immunities
        if move.move_type in defender.get_immunity():
            type_multiplier = 0.0
        else:
            # Check for weaknesses
            if move.move_type in defender.get_weaknesses():
                type_multiplier *= 2.0

            # Check for resistances
            if move.move_type in defender.get_resistances():
                type_multiplier *= 0.5

        # Critical hit chance
        critical_chance = attacker.stat.current_speed / 512
        if random.random() < critical_chance:
            damage *= 1.5

        damage *= type_multiplier
        # if move is status do 0
        if move.move_effect != StatusEnum.NORMAL:
            return 0

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
                StatusEnum.NORMAL: NormalStatusStrategy(),
            }

            defender.status_strategy = status_strategies.get(
                move.move_effect, NormalStatusStrategy()
            )

            self.battle_log.append(
                f"{defender.name} est maintenant {move.move_effect.name}!"
            )

    def perform_attack(self, attacker: Pokemon, defender: Pokemon, move: Move) -> dict:
        """
        Execute a single attack
        """
        # Check if the attack hits
        if not self.check_accuracy(move):
            self.battle_log.append(f"{move.name} a raté!")
            return {"hit": False, "damage": 0}

        # Calculate and apply damage
        damage = self.calculate_damage(attacker, defender, move)

        if not attacker.status_strategy.attack():
            self.battle_log.append(f"{attacker.name} ne peut pas attaquer!")
            return {"hit": False, "damage": 0}

        # Reduce defender's HP
        defender.take_damage(damage)

        # Log the attack only if attack is not a status move
        if move.move_effect == StatusEnum.NORMAL:
            self.battle_log.append(f"{attacker.name} utilise {move.name}")

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

    def get_battle_winner(self, player) -> Optional[Pokemon] | bool:
        """
        Determine the winner of the battle
        """
        if self.player_pokemon.get_current_hp() <= 0:
            self.handle_end_combat(False, player)
            return self.opponent_pokemon
        elif self.opponent_pokemon.get_current_hp() <= 0:
            if RoundGenerator.get_instance().is_last_pokemon():
                self.handle_end_combat(True, player)
                return True
            return self.player_pokemon
        return None

    def handle_end_combat(self, winner: bool, player: Player):
        """
        True if player wins, False if opponent wins
        """
        if not winner:
            player.money += RoundGenerator.get_instance().get_price() // 2
            self.battle_log.append(f"{player.get_current_pokemon().name} est K.O.!")

        if winner:
            player.money += RoundGenerator.get_instance().get_price()
            self.battle_log.append(
                f"Vous avez gagné, vos gains:{RoundGenerator.get_instance().get_price()} $"
            )
            RoundGenerator.get_instance().reset()

    def gave_up(self, player: Player):
        player.money += RoundGenerator.get_instance().get_price() // 2
        self.battle_log.append(
            f"Vous avez perdu, voici vos gains :{RoundGenerator.get_instance().get_price() // 2} $"
        )
        RoundGenerator.get_instance().reset()

    def handle_end_of_turn(self, pokemon: Pokemon):
        """
        Gérer les effets de fin de tour pour un Pokémon
        """
        pokemon.status_strategy.end_turn(pokemon)

    def battle_turn(self, player_move: Move | None, opponent_move: Move):
        """
        Execute a single battle turn
        return pokemon that attacked first
        """
        self.turn_count += 1
        if player_move is None:
            """only opponent attack"""
            first_attacker, first_move = self.opponent_pokemon, opponent_move
            second_attacker, second_move = self.player_pokemon, player_move
        elif (  # determined by speed
            self.player_pokemon.status_strategy.stat_change(
                self.player_pokemon
            ).current_speed
            >= self.opponent_pokemon.status_strategy.stat_change(
                self.opponent_pokemon
            ).current_speed
        ):
            first_attacker, first_move = self.player_pokemon, player_move
            second_attacker, second_move = self.opponent_pokemon, opponent_move
        else:
            first_attacker, first_move = self.opponent_pokemon, opponent_move
            second_attacker, second_move = self.player_pokemon, player_move

        first_result = self.perform_attack(first_attacker, second_attacker, first_move)

        # Check if battle is over after first attack
        if self.is_battle_over():
            return [True, first_attacker == self.player_pokemon]

        if player_move is not None:
            # Second Pokemon's attack
            second_result = self.perform_attack(
                second_attacker, first_attacker, second_move
            )

        # Gérer les effets de fin de tour pour chaque Pokémon
        self.handle_end_of_turn(self.player_pokemon)
        self.handle_end_of_turn(self.opponent_pokemon)
        if self.opponent_pokemon.get_current_hp() <= 0:
            self.player_pokemon.gain_experience(self.opponent_pokemon.get_experience())
        # Return winner if battle is over
        return [False, first_attacker == self.player_pokemon]

    def get_battle_log(self) -> str:
        """
        Retrieve the oldest battle log and remove it
        """
        if self.battle_log:
            return self.battle_log.pop(0)
        return ""

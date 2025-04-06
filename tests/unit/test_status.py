import unittest

from pokemon_app.core.factories.pokemon_factory import PokemonFactory
from pokemon_app.core.status_effects.burn_status_strategy import BurnStatusStrategy
from pokemon_app.core.status_effects.freeze_status_strategy import FreezeStatusStrategy
from pokemon_app.core.status_effects.paralysis_status_strategy import (
    ParalysisStatusStrategy,
)
from pokemon_app.core.status_effects.poison_status_strategy import PoisonStatusStrategy
from pokemon_app.core.status_effects.sleep_status_strategy import SleepStatusStrategy
from pokemon_app.core.status_effects.status_enum import StatusEnum


class TestPokemonStatus(unittest.TestCase):

    def setUp(self):
        self.pikachu = PokemonFactory.create_pikachu()

    def test_status_normal(self):
        assert self.pikachu.status_strategy.get_status() == StatusEnum.NORMAL
        assert self.pikachu.status_strategy.attack() == True
        assert self.pikachu.status_strategy.stat_change(self.pikachu).equals(
            self.pikachu.stat
        )

    def test_status_sleep(self):
        self.pikachu.status_strategy = SleepStatusStrategy()
        assert self.pikachu.status_strategy.get_status() == StatusEnum.SLEEP
        assert self.pikachu.status_strategy.attack() == False
        assert self.pikachu.status_strategy.stat_change(self.pikachu).equals(
            self.pikachu.stat
        )

        for i in range(1000):
            self.pikachu.status_strategy.end_turn(self.pikachu)
            if self.pikachu.status_strategy.get_status() == StatusEnum.NORMAL:
                break
        assert self.pikachu.status_strategy.get_status() == StatusEnum.NORMAL

    def test_status_poison(self):
        self.pikachu.status_strategy = PoisonStatusStrategy()
        assert self.pikachu.status_strategy.get_status() == StatusEnum.POISON
        assert self.pikachu.status_strategy.attack() == True
        assert self.pikachu.status_strategy.stat_change(self.pikachu).equals(
            self.pikachu.stat
        )
        hp_beginning = self.pikachu.stat.current_hp
        assert self.pikachu.status_strategy.end_turn(self.pikachu) is None
        assert self.pikachu.stat.current_hp < hp_beginning
        hp_diff_first_poison = hp_beginning - self.pikachu.stat.current_hp
        hp_first_poison = self.pikachu.stat.current_hp
        assert self.pikachu.status_strategy.end_turn(self.pikachu) is None
        assert self.pikachu.stat.current_hp < hp_first_poison
        hp_diff_second_poison = hp_first_poison - self.pikachu.stat.current_hp
        assert hp_diff_second_poison > hp_diff_first_poison

    def test_status_paralysis(self):
        self.pikachu.status_strategy = ParalysisStatusStrategy()
        assert self.pikachu.status_strategy.get_status() == StatusEnum.PARALYSIS
        assert (
            self.pikachu.status_strategy.stat_change(self.pikachu).current_speed
            == self.pikachu.stat.current_speed // 2
        )
        # 25% chance of not being able to attack
        count = 0
        for i in range(1000):
            if not self.pikachu.status_strategy.attack():
                count += 1
        assert count > 0

    def test_status_freeze(self):
        self.pikachu.status_strategy = FreezeStatusStrategy()
        assert self.pikachu.status_strategy.get_status() == StatusEnum.FREEZE
        assert self.pikachu.status_strategy.attack() == False
        assert self.pikachu.status_strategy.stat_change(self.pikachu).equals(
            self.pikachu.stat
        )
        # 20 chance of defrost
        for i in range(1000):
            self.pikachu.status_strategy.end_turn(self.pikachu)
            if self.pikachu.status_strategy.get_status() == StatusEnum.NORMAL:
                break
        assert self.pikachu.status_strategy.get_status() == StatusEnum.NORMAL

    def test_status_burn(self):
        self.pikachu.status_strategy = BurnStatusStrategy()
        assert self.pikachu.status_strategy.get_status() == StatusEnum.BURN
        assert (
            self.pikachu.status_strategy.stat_change(self.pikachu).current_attack
            == self.pikachu.stat.current_attack // 3
        )
        assert self.pikachu.status_strategy.attack() == True
        hp_beginning = self.pikachu.stat.current_hp
        assert self.pikachu.status_strategy.end_turn(self.pikachu) is None
        assert self.pikachu.stat.current_hp < hp_beginning
        hp_diff_first_burn = hp_beginning - self.pikachu.stat.current_hp
        hp_first_burn = self.pikachu.stat.current_hp
        assert self.pikachu.status_strategy.end_turn(self.pikachu) is None
        assert self.pikachu.stat.current_hp < hp_first_burn
        hp_diff_second_burn = hp_first_burn - self.pikachu.stat.current_hp
        assert hp_diff_second_burn == hp_diff_first_burn
        assert hp_diff_first_burn == hp_diff_second_burn


if __name__ == "__main__":
    unittest.main()

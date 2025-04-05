from math import floor

from pokemon_app.core.level.level_observer import LevelObserver

""""
Stats class handle evolution of stats of a pokemon with level up 
"""


class Stat(LevelObserver):

    def __init__(
        self,
        base_hp: int,
        base_attack: int,
        base_attack_special: int,
        base_defense: int,
        base_defense_special: int,
        base_speed: int,
        max_hp: int,
        max_attack: int,
        max_attack_special: int,
        max_defense: int,
        max_defense_special: int,
        max_speed: int,
    ):
        self.__base_hp = base_hp
        self.__base_attack = base_attack
        self.__base_attack_special = base_attack_special
        self.__base_defense = base_defense
        self.__base_defense_special = base_defense_special
        self.__base_speed = base_speed
        self.__max_hp = max_hp
        self.__max_attack = max_attack
        self.__max_attack_special = max_attack_special
        self.__max_defense = max_defense
        self.__max_defense_special = max_defense_special
        self.__max_speed = max_speed
        self.__current_hp = self.__base_hp
        self.current_max_hp = self.__base_hp
        self.__set_stat(1)

    def __set_stat(self, level_current: int):
        """
        Calculate the stats of a pokemon with current level
        basic linear interopolation formula with floor
        """
        linear_interpolation = lambda level, base, max_value: floor(
            base + (max_value - base) * level / 100
        )
        # if pokemon hurt then he gain back hp that the new level_max difference is from the old
        # so if max_hp before 100 after 110 pokemon gain 10
        if self.__current_hp <= self.current_max_hp:
            new_current_max_hp = linear_interpolation(
                level_current, self.__base_hp, self.__max_hp
            )
            self.__current_hp += new_current_max_hp - self.current_max_hp

        self.current_max_hp = linear_interpolation(
            level_current, self.__base_hp, self.__max_hp
        )

        self.current_attack = linear_interpolation(
            level_current, self.__base_attack, self.__max_attack
        )
        self.current_attack_special = linear_interpolation(
            level_current, self.__base_attack_special, self.__max_attack_special
        )
        self.current_defense = linear_interpolation(
            level_current, self.__base_defense, self.__max_defense
        )
        self.current_defense_special = linear_interpolation(
            level_current, self.__base_defense_special, self.__max_defense_special
        )
        self.current_speed = linear_interpolation(
            level_current, self.__base_speed, self.__max_speed
        )

    def on_level_up(self, pokemon, old_level: int, new_level: int):
        """
        Method called by observable when level Up
        """
        self.__set_stat(new_level)

    def on_dead(self, pokemon):
        """
        Method called by observable when pokemon die
        """
        self._current_hp = 0

    @property
    def current_hp(self):
        """
        Return the current max hp of pokemon
        """
        return self.__current_hp

    @current_hp.setter
    def current_hp(self, value):
        self.__current_hp = value
        if self.current_hp < 0:
            self.__current_hp = 0
        if self.current_hp > self.current_max_hp:
            self.__current_hp = self.current_max_hp

    def equals(self, stat):
        """
        Compare two stats
        """
        return (
            self.current_max_hp == stat.current_max_hp
            and self.current_attack == stat.current_attack
            and self.current_attack_special == stat.current_attack_special
            and self.current_defense == stat.current_defense
            and self.current_defense_special == stat.current_defense_special
            and self.current_speed == stat.current_speed
        )

    @property
    def base_hp(self):
        return self.__base_hp

    @property
    def base_attack(self):
        return self.__base_attack

    @property
    def base_attack_special(self):
        return self.__base_attack_special

    @property
    def base_defense(self):
        return self.__base_defense

    @property
    def base_defense_special(self):
        return self.__base_defense_special

    @property
    def base_speed(self):
        return self.__base_speed

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def max_attack(self):
        return self.__max_attack

    @property
    def max_attack_special(self):
        return self.__max_attack_special

    @property
    def max_defense(self):
        return self.__max_defense

    @property
    def max_defense_special(self):
        return self.__max_defense_special

    @property
    def max_speed(self):
        return self.__max_speed

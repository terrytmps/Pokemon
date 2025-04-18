from pokemon_app.core.move import Move
from pokemon_app.core.level.level import Level
from pokemon_app.core.level.stats import Stat
from pokemon_app.core.level.xp_difficulty import XPDifficulty
from pokemon_app.core.pokemon_type.utils.pokemon_type_enum import PokemonType
from pokemon_app.core.status_effects.normal_status_strategy import NormalStatusStrategy
from pokemon_app.core.status_effects.status_enum import StatusEnum
from pokemon_app.core.status_effects.status_strategy import StatusStrategy


class Pokemon:
    """
    Class that represent a pokemon with all its attributes and behavior
    with stats and level logic separated status_effects also
    and a builder to make the initialisation easy
    """

    def __init__(
        self,
        name: str = "",
        sprite_url: str = "",
        price: int = 0,
        level: Level = None,
        stat: Stat = None,
    ):
        """
        Not recommend use the builder
        """
        super().__init__()
        self.id: int = 0
        self.name: str = name
        self.__level: Level = level
        self.__stat: Stat = stat
        self._sprite_url: str = sprite_url
        self._moves: list[Move | None] = [None] * 4
        self.price: int = price
        self._status_strategy: StatusStrategy = NormalStatusStrategy()

    def max_hp(self):
        return self.__stat.current_max_hp

    def get_current_hp(self):
        return self.__stat.current_hp

    def get_current_max_hp(self):
        return self.__stat.current_max_hp

    def get_level_object(self):
        return self.__level

    def get_status(self) -> StatusEnum:
        return self._status_strategy.get_status()

    @property
    def sprite_url(self):
        return self._sprite_url

    @property
    def stat(self):
        return self.__stat

    @property
    def level(self):
        return self.__level.level

    @level.setter
    def level(self, value):
        self.__level.level_up_to(value)

    @property
    def first_type(self):
        return None

    @property
    def second_type(self):
        return None

    @property
    def status_strategy(self):
        return self._status_strategy

    @status_strategy.setter
    def status_strategy(self, strategy: StatusStrategy):
        assert strategy is not None
        self._status_strategy = strategy

    def take_damage(self, amount: int):
        """
        Take damage from the pokemon
        """
        self.__stat.current_hp = max(0, self.__stat.current_hp - amount)

    def get_experience(self):
        """
        Return the experience of the pokemon
        """
        return self.__level.level + 1

    def gain_experience(self, xp: int):
        """
        Gain X amount of experience at the end of the fight
        """
        self.__level.gain_experience(xp)

    def level_up_to(self, level: int):
        """
        Level up the pokemon to the given level
        """
        self.__level.level_up_to(level)

    def add_move(self, move) -> bool:
        """
        Try to add a move return boolean meaning success of operation
        """
        for i in range(4):
            if self._moves[i] is None:
                self._moves[i] = move
                return True
        return False

    def replace_move(self, move, index) -> bool:
        """
        Try to replace a move return boolean meaning success of operation
        """

        if index < 0 or index > 3:
            return False
        self._moves[index] = move
        return True

    def get_moves(self) -> list:
        """
        Return the moves of the pokemon
        """
        return self._moves

    ## Decorator pattern methods

    def get_types(self):
        """
        Return the types of the pokemon
        """
        return []

    def get_resistances(self):
        """ "
        Return the resistances of the pokemon
        """
        return []

    def get_weaknesses(self):
        """
        Return the weaknesses of the pokemon
        """
        return []

    def get_immunity(self):
        """
        Return the immunities of the pokemon
        """
        return []

    def to_dict(self):
        """Convertit le Pokémon en dictionnaire sérialisable en JSON. seulement informations utiles"""
        first_move = self._moves[0]
        second_move = self._moves[1]
        third_move = self._moves[2]
        fourth_move = self._moves[3]
        if first_move is not None:
            first_move = first_move.to_dict()
        if second_move is not None:
            second_move = second_move.to_dict()
        if third_move is not None:
            third_move = third_move.to_dict()
        if fourth_move is not None:
            fourth_move = fourth_move.to_dict()

        return {
            "name": self.name,
            "sprite_url": self._sprite_url,
            "level": self.level,
            "hp_max": self.__stat.current_max_hp,
            "hp_current": self.__stat.current_hp,
            "status": str(self.get_status().value[1] if self.get_status() else None),
            "first_type": self.first_type.value if self.first_type else None,
            "second_type": self.second_type.value if self.second_type else None,
            "first_move": first_move,
            "second_move": second_move,
            "third_move": third_move,
            "fourth_move": fourth_move,
        }

    class Builder:
        """
        Builder for pokemon
        """

        def __init__(self):
            self.stat = None
            self.level = None
            self.price = None
            self.sprite_url = None
            self.name = None
            self.types = []
            self.moves = [None] * 4

        def set_name(self, name: str):
            self.name = name
            return self

        def set_img(self, sprite_url: str):
            self.sprite_url = sprite_url
            return self

        def set_price(self, price: int):
            self.price = price
            return self

        def set_level(self, level: int, xp_difficulty: XPDifficulty):
            self.level = Level(level, xp_difficulty)
            return self

        def set_stat(self, stat: Stat):
            self.stat = stat
            return self

        def set_type(self, pokemon_type: PokemonType):
            """Allow only 2 types"""
            if len(self.types) < 2:
                self.types.append(pokemon_type)
            return self

        def set_moves(self, move):
            """Allow only 4 moves"""
            for i in range(4):
                if self.moves[i] is None:
                    self.moves[i] = move
                    return self
            return self

        def build(self):
            """
            Build the pokemon with the given attributes
            """
            from pokemon_app.core.pokemon_type.utils.pokemon_type_dict import (
                dict_from_enum_to_decorator,
            )

            assert self.level is not None
            assert self.price is not None
            assert self.sprite_url is not None
            assert self.name is not None
            assert self.stat is not None
            self.level.subscribe_level_observer(self.stat)
            pokemon = Pokemon(
                self.name, self.sprite_url, self.price, self.level, self.stat
            )
            # sort the order of the types if there is 2
            if len(self.types) == 2:
                self.types = sorted(self.types, key=lambda x: x.value)

            for pokemon_type in self.types:
                if pokemon_type is not None:
                    pokemon = dict_from_enum_to_decorator.get(pokemon_type)(pokemon)

            for move in self.moves:
                if move is not None:
                    pokemon.add_move(move)

            return pokemon

    def __str__(self):
        moves = [move.name if move else "None" for move in self._moves]
        return (
            f"Pokemon(id={self.id}, name={self.name}, level={self.level}, hp={self.get_current_hp()}/{self.get_current_max_hp()}, "
            f"price={self.price}, status_effects={self.get_status().value[1] if self.get_status() else 'None'}, "
            f"first_type={self.first_type if self.first_type else 'None'}, "
            f"second_type={self.second_type if self.second_type else 'None'}, "
            f"moves={moves}, sprite_url={self.sprite_url})"
        )

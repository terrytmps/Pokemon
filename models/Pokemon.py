from models.level.Level import Level
from models.level.Stats import Stat
from models.level.XpDifficulty import XPDifficulty
from models.pokemonType.utils.PokemonTypeEnum import PokemonType
from models.status.NormalStatusStrategy import NormalStatusStrategy
from models.status.StatusEnum import StatusEnum
from models.status.StatusStrategy import StatusStrategy


class Pokemon:
    """
    Class that represent a pokemon with all its attributes and behavior
    with stats and level logic separated status also
    and a builder to make the initialisation easy
    """

    def __init__(
        self, name: str, sprite_url: str, price: int, level: Level, stat: Stat
    ):
        """
        Not recommend use the builder
        """
        super().__init__()
        self.name = name
        self.__level = level
        self.__stat = stat
        self._sprite_url = sprite_url
        self._moves = [None] * 4
        self.price = price
        self._status_strategy = NormalStatusStrategy()

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
        if self.__stat.current_hp == 0:
            self.__level.notify_dead()


    def gain_experience(self, xp: int):
        """
        Gain X amount of experience at the end of the fight
        """
        self.__level.gain_experience(xp)

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
            from models.pokemonType.utils.PokemonTypeDict import (
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

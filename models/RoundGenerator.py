from models.Pokemon import Pokemon
from models.factory.PokemonFactory import PokemonFactory
import threading


class RoundGenerator:
    """Generates all 100 rounds with a specific Pokémon and level.
    Implements the Singleton pattern in a thread-safe way.
    """

    _instance = None
    _lock = threading.Lock()  # protect from multi-threading

    def __new__(cls):
        with cls._lock:  # Lock access
            if cls._instance is None:
                cls._instance = super(RoundGenerator, cls).__new__(cls)
                cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Unique initialization method."""
        if hasattr(self, "__rounds"):
            return

        self.__rounds = [
            (PokemonFactory.create_salameche(), 1),
            (PokemonFactory.create_pikachu(), 1),
            (PokemonFactory.create_rattatac(), 5),
            (PokemonFactory.create_ponyta(), 7),
            (PokemonFactory.create_machop(), 9),
            (PokemonFactory.create_tangela(), 10),
            (PokemonFactory.create_onix(), 12),
            (PokemonFactory.create_machoke(), 14),
            (PokemonFactory.create_leviator(), 16),
            (PokemonFactory.create_lucario(), 18),
            (PokemonFactory.create_gardevoir(), 20),
            (PokemonFactory.create_exeggutor(), 22),
            (PokemonFactory.create_metalosse(), 24),
            (PokemonFactory.create_trioxhydre(), 26),
            (PokemonFactory.create_blizzaroi(), 28),
            (PokemonFactory.create_ectoplasma(), 30),
            (PokemonFactory.create_arbok(), 32),
            (PokemonFactory.create_golem(), 34),
            (PokemonFactory.create_farfetchd(), 36),
            (PokemonFactory.create_musteflott(), 38),
            (PokemonFactory.create_tyranocif(), 40),
            (PokemonFactory.create_pikachu(), 42),
            (PokemonFactory.create_rattatac(), 44),
            (PokemonFactory.create_machoke(), 46),
            (PokemonFactory.create_noctali(), 48),
            (PokemonFactory.create_lucario(), 50),
            (PokemonFactory.create_blizzaroi(), 52),
            (PokemonFactory.create_machop(), 54),
            (PokemonFactory.create_ponyta(), 56),
            (PokemonFactory.create_gardevoir(), 58),
            (PokemonFactory.create_trioxhydre(), 60),
            (PokemonFactory.create_trioxhydre(), 62),
            (PokemonFactory.create_metalosse(), 64),
            (PokemonFactory.create_ectoplasma(), 66),
            (PokemonFactory.create_exeggutor(), 68),
            (PokemonFactory.create_golem(), 70),
            (PokemonFactory.create_noctali(), 72),
            (PokemonFactory.create_pikachu(), 74),
            (PokemonFactory.create_dracaufeu(), 76),
            (PokemonFactory.create_arbok(), 78),
            (PokemonFactory.create_musteflott(), 80),
            (PokemonFactory.create_gardevoir(), 82),
            (PokemonFactory.create_trioxhydre(), 84),
            (PokemonFactory.create_mewtwo(), 86),
            (PokemonFactory.create_exeggutor(), 88),
            (PokemonFactory.create_ectoplasma(), 90),
            (PokemonFactory.create_leviator(), 92),
            (PokemonFactory.create_lucario(), 94),
            (PokemonFactory.create_tartard(), 96),
            (PokemonFactory.create_blizzaroi(), 98),
            (PokemonFactory.create_leviator(), 100),
            (PokemonFactory.create_metalosse(), 102),
            (PokemonFactory.create_voltali(), 104),
            (PokemonFactory.create_tyranocif(), 106),
            (PokemonFactory.create_lucario(), 108),
            (PokemonFactory.create_exeggutor(), 110),
            (PokemonFactory.create_musteflott(), 112),
            (PokemonFactory.create_ectoplasma(), 114),
            (PokemonFactory.create_trioxhydre(), 116),
            (PokemonFactory.create_metalosse(), 118),
            (PokemonFactory.create_ronflex(), 120),
            (PokemonFactory.create_voltali(), 122),
            (PokemonFactory.create_tyranocif(), 124),
            (PokemonFactory.create_lucario(), 126),
            (PokemonFactory.create_mewtwo(), 130),
        ]

        self.__index = 0

    def generate_round(self) -> Pokemon | None:
        """Generate the next round."""
        if self.__index < len(self.__rounds):
            pokemon, level = self.__rounds[self.__index]
            self.__index += 1
            pokemon.level_up_to(level)
            return pokemon
        return None

    def is_last_pokemon(self) -> bool:
        """Return if the current pokemon is last one"""
        return self.__index == len(self.__rounds)

    def reset(self):
        """Reset the round generator."""
        self.__index = 0

    def get_price(self) -> int:
        """Get the price for all cleared round"""
        if self.__index <= 1:
            return 0
        return self.__index * 2

    @classmethod
    def get_instance(cls):
        """Retrieve the singleton instance."""
        return cls.__new__(cls)

    def get_index(self):
        """Return the current index."""
        return self.__index

from models.Pokemon import Pokemon
from models.factory.MoveFactory import MoveFactory
from models.level.Stats import Stat
from models.level.XpDifficulty import XPDifficulty
from models.pokemonType.utils.PokemonTypeEnum import PokemonType


class PokemonFactory:
    """
    Factory to create the most common pokemon useful also for test
    """

    @staticmethod
    def create_pikachu():
        stat = Stat(35, 55, 50, 40, 50, 90, 330, 250, 220, 120, 180, 250)
        return (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(10)
            .set_type(PokemonType.ELECTRIC)
            .set_moves(MoveFactory.get_move("Éclair"))
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Queue de Fer"))
            .set_moves(MoveFactory.get_move("Paralysie"))
            .build()
        )

    @staticmethod
    def create_dracaufeu():
        stat = Stat(78, 84, 109, 78, 85, 100, 328, 280, 325, 250, 290, 315)
        return (
            Pokemon.Builder()
            .set_name("Dracaufeu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
            )
            .set_level(36, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.FIRE)
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Mèche Enflammée"))
            .set_moves(MoveFactory.get_move("Griffe Dragon"))
            .build()
        )

    @staticmethod
    def create_leviator():
        stat = Stat(95, 75, 60, 79, 100, 81, 350, 270, 260, 210, 250, 270)
        return (
            Pokemon.Builder()
            .set_name("Leviator")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png"
            )
            .set_level(20, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(18)
            .set_type(PokemonType.WATER)
            .set_type(PokemonType.FLYING)
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .build()
        )

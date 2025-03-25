import unittest

from models.level.Stats import Stat
from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.BugTypeDecorator import BugTypeDecorator
from models.pokemonType.DarkTypeDecorator import DarkTypeDecorator
from models.pokemonType.DragonTypeDecorator import DragonTypeDecorator
from models.pokemonType.ElectricTypeDecorator import ElectricTypeDecorator
from models.pokemonType.FightingTypeDecorator import FightingTypeDecorator
from models.pokemonType.FlyingTypeDecorator import FlyingTypeDecorator
from models.pokemonType.GhostTypeDecorator import GhostTypeDecorator
from models.pokemonType.GrassTypeDecorator import GrassTypeDecorator
from models.pokemonType.GroundTypeDecorator import GroundTypeDecorator
from models.pokemonType.IceTypeDecorator import IceTypeDecorator
from models.pokemonType.PoisonTypeDecorator import PoisonTypeDecorator
from models.pokemonType.PsychicTypeDecorator import PsychicTypeDecorator
from models.pokemonType.RockTypeDecorator import RockTypeDecorator
from models.pokemonType.SteelTypeDecorator import SteelTypeDecorator
from models.pokemonType.WaterTypeDecorator import WaterTypeDecorator
from models.Pokemon import Pokemon
from models.level.XpDifficulty import XPDifficulty
from models.pokemonType.FireTypeDecorator import FireTypeDecorator
from models.pokemonType.NormalTypeDecorator import NormalTypeDecorator
from models.pokemonType.utils.PokemonTypeEnum import PokemonType


class TestTypeDecorator(unittest.TestCase):

    def setUp(self):
        stat = Stat(35, 55, 50, 40, 50, 90, 330, 250, 220, 120, 180, 250)

        self.electric = (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(10)
            .set_type(PokemonType.ELECTRIC)
            .build()
        )

        self.no_type = (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(10)
            .build()
        )

        self.fire = (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(10)
            .set_type(PokemonType.FIRE)
            .build()
        )

        self.normal_fire = (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(10)
            .set_type(PokemonType.FIRE)
            .set_type(PokemonType.NORMAL)
            .build()
        )

    def test_type_decorator_empty(self):
        assert self.no_type.get_types() == []
        assert self.no_type.first_type is None
        assert self.no_type.second_type is None
        assert self.no_type.get_resistances() == []
        assert self.no_type.get_weaknesses() == []
        assert self.no_type.get_immunity() == []

    def test_fire_type_decorator(self):

        assert PokemonType.FIRE in self.fire.get_types()
        assert len(self.fire.get_types()) == 1

        # Vérification des résistances
        resistances = self.fire.get_resistances()
        expected_resistances = [
            PokemonType.FIRE,
            PokemonType.GRASS,
            PokemonType.ICE,
            PokemonType.BUG,
            PokemonType.STEEL,
        ]
        for resistance in expected_resistances:
            assert resistance in resistances
        assert len(resistances) == 5

        # Vérification des faiblesses
        weaknesses = self.fire.get_weaknesses()
        expected_weaknesses = [PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 3

    def test_type_solo_each(self):
        def check_type_decorator(type_decorator: TypeDecorator):
            assert type_decorator.get_types() == [type_decorator.first_type]
            assert type_decorator.get_resistances() != [type_decorator.get_weaknesses()]
            assert type_decorator.get_immunity() != [type_decorator.get_weaknesses()]

        # Test all types
        check_type_decorator(BugTypeDecorator(self.no_type))
        check_type_decorator((DarkTypeDecorator(self.no_type)))
        check_type_decorator((DragonTypeDecorator(self.no_type)))
        check_type_decorator((ElectricTypeDecorator(self.no_type)))
        check_type_decorator((FightingTypeDecorator(self.no_type)))
        check_type_decorator((FireTypeDecorator(self.no_type)))
        check_type_decorator((FlyingTypeDecorator(self.no_type)))
        check_type_decorator((GhostTypeDecorator(self.no_type)))
        check_type_decorator((GrassTypeDecorator(self.no_type)))
        check_type_decorator((GroundTypeDecorator(self.no_type)))
        check_type_decorator((IceTypeDecorator(self.no_type)))
        check_type_decorator((NormalTypeDecorator(self.no_type)))
        check_type_decorator((PoisonTypeDecorator(self.no_type)))
        check_type_decorator((PsychicTypeDecorator(self.no_type)))
        check_type_decorator((RockTypeDecorator(self.no_type)))
        check_type_decorator((SteelTypeDecorator(self.no_type)))
        check_type_decorator((WaterTypeDecorator(self.no_type)))

    def test_double_type_decorator(self):

        normal_fire_types = self.normal_fire.get_types()
        assert PokemonType.NORMAL in normal_fire_types
        assert PokemonType.FIRE in normal_fire_types
        assert len(normal_fire_types) == 2
        assert self.normal_fire.first_type == PokemonType.NORMAL
        assert self.normal_fire.second_type == PokemonType.FIRE

        # Vérification des résistances (combinaison des deux types)
        resistances = self.normal_fire.get_resistances()
        expected_resistances = [
            PokemonType.FIRE,
            PokemonType.GRASS,
            PokemonType.ICE,
            PokemonType.BUG,
            PokemonType.STEEL,
        ]
        for resistance in expected_resistances:
            assert resistance in resistances
        assert len(resistances) == 5

        # Vérification des faiblesses (combinaison des deux types)
        weaknesses = self.normal_fire.get_weaknesses()
        expected_weaknesses = [
            PokemonType.FIGHT,
            PokemonType.WATER,
            PokemonType.GROUND,
            PokemonType.ROCK,
        ]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 4

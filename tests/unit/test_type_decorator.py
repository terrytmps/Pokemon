import unittest

from pokemon_app.core.level.stats import Stat
from pokemon_app.core.pokemon_type.type_decorator import TypeDecorator
from pokemon_app.core.pokemon_type.bug_type_decorator import BugTypeDecorator
from pokemon_app.core.pokemon_type.dark_type_decorator import DarkTypeDecorator
from pokemon_app.core.pokemon_type.dragon_type_decorator import DragonTypeDecorator
from pokemon_app.core.pokemon_type.electric_type_decorator import ElectricTypeDecorator
from pokemon_app.core.pokemon_type.fighting_type_decorator import FightingTypeDecorator
from pokemon_app.core.pokemon_type.flying_type_decorator import FlyingTypeDecorator
from pokemon_app.core.pokemon_type.ghost_type_decorator import GhostTypeDecorator
from pokemon_app.core.pokemon_type.grass_type_decorator import GrassTypeDecorator
from pokemon_app.core.pokemon_type.ground_type_decorator import GroundTypeDecorator
from pokemon_app.core.pokemon_type.ice_type_decorator import IceTypeDecorator
from pokemon_app.core.pokemon_type.poison_type_decorator import PoisonTypeDecorator
from pokemon_app.core.pokemon_type.psychic_type_decorator import PsychicTypeDecorator
from pokemon_app.core.pokemon_type.rock_type_decorator import RockTypeDecorator
from pokemon_app.core.pokemon_type.steel_type_decorator import SteelTypeDecorator
from pokemon_app.core.pokemon_type.water_type_decorator import WaterTypeDecorator
from pokemon_app.core.pokemon import Pokemon
from pokemon_app.core.level.xp_difficulty import XPDifficulty
from pokemon_app.core.pokemon_type.fire_type_decorator import FireTypeDecorator
from pokemon_app.core.pokemon_type.normal_type_decorator import NormalTypeDecorator
from pokemon_app.core.pokemon_type.utils.pokemon_type_enum import PokemonType


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

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
from models.pokemon import Pokemon
from models.xp_difficulty import XPDifficulty
from models.pokemonType.FireTypeDecorator import FireTypeDecorator
from models.pokemonType.NormalTypeDecorator import NormalTypeDecorator
from models.pokemonType.pokemon_type import PokemonType



class TestTypeDecorator:

    def test_type_decorator_empty(self):
        pikachu = TypeDecorator(Pokemon("Pikachu", 12, 57, "", XPDifficulty.EASY, 10))

        assert pikachu.get_types() == []
        assert pikachu.first_type is None
        assert pikachu.second_type is None
        assert pikachu.get_resistances() == []
        assert pikachu.get_weaknesses() == []
        assert pikachu.get_immunity() == []


    def test_fire_type_decorator(self):
        pikachu = Pokemon("Pikachu", 12, 57, "", XPDifficulty.EASY, 10)

        assert pikachu.get_types() == []
        assert pikachu.get_resistances() == []
        assert pikachu.get_weaknesses() == []

        fire_pikachu = FireTypeDecorator(pikachu)

        assert PokemonType.FIRE in fire_pikachu.get_types()
        assert len(fire_pikachu.get_types()) == 1

        # Vérification des résistances
        resistances = fire_pikachu.get_resistances()
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
        weaknesses = fire_pikachu.get_weaknesses()
        expected_weaknesses = [PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 3

    def test_type_solo_each(self):
        def check_type_decorator(type_decorator: TypeDecorator):
            assert type_decorator.get_types() == [type_decorator.first_type]
            assert type_decorator.get_resistances() != [type_decorator.get_weaknesses()]
            assert type_decorator.get_immunity() != [type_decorator.get_weaknesses()]


        pikachu = Pokemon("Pikachu", 12, 57, "", XPDifficulty.EASY, 10)
        # Test all types
        check_type_decorator(BugTypeDecorator(pikachu))
        check_type_decorator((DarkTypeDecorator(pikachu)))
        check_type_decorator((DragonTypeDecorator(pikachu)))
        check_type_decorator((ElectricTypeDecorator(pikachu)))
        check_type_decorator((FightingTypeDecorator(pikachu)))
        check_type_decorator((FireTypeDecorator(pikachu)))
        check_type_decorator((FlyingTypeDecorator(pikachu)))
        check_type_decorator((GhostTypeDecorator(pikachu)))
        check_type_decorator((GrassTypeDecorator(pikachu)))
        check_type_decorator((GroundTypeDecorator(pikachu)))
        check_type_decorator((IceTypeDecorator(pikachu)))
        check_type_decorator((NormalTypeDecorator(pikachu)))
        check_type_decorator((PoisonTypeDecorator(pikachu)))
        check_type_decorator((PsychicTypeDecorator(pikachu)))
        check_type_decorator((RockTypeDecorator(pikachu)))
        check_type_decorator((SteelTypeDecorator(pikachu)))
        check_type_decorator((WaterTypeDecorator(pikachu)))



    def test_double_type_decorator(self):
        flareon = Pokemon("Flareon", 20, 65, "", XPDifficulty.NORMAL, 25)

        # Application de deux décorateurs: NormalTypeDecorator et FireTypeDecorator
        normal_then_fire = FireTypeDecorator(NormalTypeDecorator(flareon))

        normal_fire_types = normal_then_fire.get_types()
        assert PokemonType.NORMAL in normal_fire_types
        assert PokemonType.FIRE in normal_fire_types
        assert len(normal_fire_types) == 2
        assert normal_then_fire.first_type == PokemonType.NORMAL
        assert normal_then_fire.second_type == PokemonType.FIRE

        # Vérification des résistances (combinaison des deux types)
        resistances = normal_then_fire.get_resistances()
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
        weaknesses = normal_then_fire.get_weaknesses()
        expected_weaknesses = [
            PokemonType.FIGHT,
            PokemonType.WATER,
            PokemonType.GROUND,
            PokemonType.ROCK,
        ]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 4

from models.pokemon import Pokemon
from models.enum.xp_difficulty import XPDifficulty
from models.Decorator.TypeDecorators.FireTypeDecorator import FireTypeDecorator
from models.Decorator.TypeDecorators.NormalTypeDecorator import NormalTypeDecorator
from models.enum.pokemon_type import PokemonType



class TestTypeDecorator:

    def test_type_decorator(self):
        pikachu = Pokemon("Pikachu", 12, 57, "", XPDifficulty.EASY, 10)

        assert pikachu.get_types() == []
        assert pikachu.get_resistances() == []
        assert pikachu.get_weaknesses() == []

        fire_pikachu = FireTypeDecorator(pikachu)

        assert PokemonType.FIRE in fire_pikachu.get_types()
        assert len(fire_pikachu.get_types()) == 1

        # Vérification des résistances
        resistances = fire_pikachu.get_resistances()
        expected_resistances = [PokemonType.FIRE, PokemonType.GRASS, PokemonType.ICE,
                                PokemonType.BUG, PokemonType.STEEL]
        for resistance in expected_resistances:
            assert resistance in resistances
        assert len(resistances) == 5

        # Vérification des faiblesses
        weaknesses = fire_pikachu.get_weaknesses()
        expected_weaknesses = [PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 3

    def test_double_type_decorator(self):
        flareon = Pokemon("Flareon", 20, 65, "", XPDifficulty.NORMAL, 25)

        # Application de deux décorateurs: NormalTypeDecorator et FireTypeDecorator
        normal_then_fire = FireTypeDecorator(NormalTypeDecorator(flareon))

        normal_fire_types = normal_then_fire.get_types()
        assert PokemonType.NORMAL in normal_fire_types
        assert PokemonType.FIRE in normal_fire_types
        assert len(normal_fire_types) == 2

        # Vérification des résistances (combinaison des deux types)
        resistances = normal_then_fire.get_resistances()
        expected_resistances = [PokemonType.FIRE, PokemonType.GRASS, PokemonType.ICE,
                                PokemonType.BUG, PokemonType.STEEL]
        for resistance in expected_resistances:
            assert resistance in resistances
        assert len(resistances) == 5

        # Vérification des faiblesses (combinaison des deux types)
        weaknesses = normal_then_fire.get_weaknesses()
        expected_weaknesses = [PokemonType.FIGHT, PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK]
        for weakness in expected_weaknesses:
            assert weakness in weaknesses
        assert len(weaknesses) == 4

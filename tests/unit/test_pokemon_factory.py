import unittest

from pokemon_app.core.factories.pokemon_factory import PokemonFactory


class TestPokemonFactory(unittest.TestCase):

    def test_all_method_return_pokemon(self):
        for method in PokemonFactory.get_all_staticmethod():
            pokemon = method()
            self.assertIsNotNone(pokemon)

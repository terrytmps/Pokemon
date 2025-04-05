import unittest

from pokemon_app.core.pokemon import Pokemon
from pokemon_app.core.level.level import Level
from pokemon_app.core.level.stats import Stat
from pokemon_app.core.level.xp_difficulty import XPDifficulty
from pokemon_app.core.pokemon_type.utils.pokemon_type_enum import PokemonType


class TestPokemonBuilder(unittest.TestCase):
    def setUp(self):
        # Préparer des valeurs de test
        self.stat = Stat(35, 55, 50, 40, 50, 90, 330, 250, 220, 120, 180, 250)
        self.level = Level(5, XPDifficulty.NORMAL)
        self.price = 100
        self.sprite_url = "https://example.com/sprite.png"
        self.name = "Pikachu"
        self.pokemon_builder = Pokemon.Builder()

    def test_pokemon_builder_name(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.name, self.name)

    def test_pokemon_builder_sprite_url(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.sprite_url, self.sprite_url)

    def test_pokemon_builder_price(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.price, self.price)

    def test_pokemon_builder_level(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.get_level_object().level, 5)

    def test_pokemon_builder_stat(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.stat, self.stat)

    def test_pokemon_builder_add_types(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .set_type(PokemonType.ELECTRIC)
            .set_type(PokemonType.FIRE)
            .build()
        )

        self.assertEqual(len(pokemon.get_types()), 2)
        self.assertIn(PokemonType.ELECTRIC, pokemon.get_types())
        self.assertIn(PokemonType.FIRE, pokemon.get_types())

    def test_pokemon_builder_add_moves(self):
        move = "Thunderbolt"
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .set_moves(move)
            .build()
        )

        self.assertIn(move, pokemon._moves)

    def test_pokemon_builder_max_hp(self):
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        self.assertEqual(pokemon.max_hp(), self.stat.current_max_hp)

    def test_pokemon_builder_invalid_move_addition(self):
        # Test if adding more than 4 moves fails
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .build()
        )

        # Add 5 moves
        for i in range(5):
            pokemon.add_move(f"Move {i + 1}")

        # Ensure only 4 moves are added
        self.assertEqual(pokemon._moves.count(None), 0)  # No None means 4 moves added

    def test_pokemon_builder_invalid_type_addition(self):
        # Test if adding more than 2 types fails
        pokemon = (
            self.pokemon_builder.set_name(self.name)
            .set_img(self.sprite_url)
            .set_price(self.price)
            .set_level(5, XPDifficulty.NORMAL)
            .set_stat(self.stat)
            .set_type(PokemonType.ELECTRIC)
            .set_type(PokemonType.FIRE)
            .set_type(PokemonType.WATER)
            .build()
        )

        # Ensure only 2 types are added
        self.assertEqual(len(pokemon.get_types()), 2)


if __name__ == "__main__":
    unittest.main()

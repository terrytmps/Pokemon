import unittest
from unittest.mock import MagicMock
from models.Pokemon import Pokemon
from models.factory.PokemonFactory import PokemonFactory
from models.level.XpDifficulty import XPDifficulty
from models.level.Stats import LevelObserver


class TestPokemonLevelUpObserver(unittest.TestCase):

    def setUp(self):
        self.pikachu = PokemonFactory.create_pikachu()
        # Mocking the LevelObserver
        self.mock_observer = MagicMock(spec=LevelObserver)

        # Adding the mock observer to the Pokemon instance
        self.pikachu.get_level_object().subscribe_level_observer(self.mock_observer)

    def test_level_up_notification(self):
        # Simulate a level up
        self.pikachu.gain_experience(1)

        # Check if the observer's on_level_up method was called
        self.mock_observer.on_level_up.assert_called()

        # Check the arguments passed to the on_level_up method
        args, _ = self.mock_observer.on_level_up.call_args
        self.assertEqual(args[0], self.pikachu.get_level_object())

        self.assertEqual(args[1], 1)
        self.assertEqual(args[2], 2)

    def test_multiple_level_ups(self):
        # Simulate multiple level ups
        self.pikachu.gain_experience(50)

        # Check if the observer's on_level_up method was called
        self.assertGreater(self.pikachu.level, 7)

        # assert call more than once
        self.assertGreater(self.mock_observer.on_level_up.call_count, 1)

    def test_remove_observer(self):
        self.pikachu.get_level_object().unsubscribe_level_observer(self.mock_observer)

        self.pikachu.gain_experience(10)

        # Check if the observer's on_level_up method was not called
        self.mock_observer.on_level_up.assert_not_called()

    def test_level_100_limit(self):
        self.pikachu.gain_experience(10000)
        self.assertEqual(self.pikachu.level, 100)
        self.pikachu.level_up_to(130)
        self.assertEqual(self.pikachu.level, 130)


if __name__ == "__main__":
    unittest.main()

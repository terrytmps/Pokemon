import unittest
from unittest.mock import MagicMock
from models.pokemon import Pokemon
from models.level.xp_difficulty import XPDifficulty
from models.level.Stats import LevelObserver


class TestPokemonLevelUpObserver(unittest.TestCase):

    def setUp(self):
        self.pikachu = Pokemon("Pikachu", 5, 35, "pikachu.png", XPDifficulty.NORMAL, 15)

        # Mocking the LevelObserver
        self.mock_observer = MagicMock(spec=LevelObserver)

        # Adding the mock observer to the Pokemon instance
        self.pikachu.subscribe_level_observer(self.mock_observer)

    def test_level_up_notification(self):
        # Simulate a level up
        self.pikachu.levelUp(10)

        # Check if the observer's on_level_up method was called
        self.mock_observer.on_level_up.assert_called()

        # Check the arguments passed to the on_level_up method
        args, _ = self.mock_observer.on_level_up.call_args
        self.assertEqual(args[0], self.pikachu)

        self.assertEqual(args[1], 5)
        self.assertGreater(args[2], 5)

    def test_multiple_level_ups(self):
        # Simulate multiple level ups
        self.pikachu.levelUp(50)

        # Check if the observer's on_level_up method was called
        self.assertGreater(self.pikachu.level, 7)

        # assert call more than once
        self.assertGreater(self.mock_observer.on_level_up.call_count, 1)

    def test_remove_observer(self):
        self.pikachu.unsubscribe_level_observer(self.mock_observer)

        self.pikachu.levelUp(10)

        # Check if the observer's on_level_up method was not called
        self.mock_observer.on_level_up.assert_not_called()


if __name__ == "__main__":
    unittest.main()

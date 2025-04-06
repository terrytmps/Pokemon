import logging

from pokemon_app.core.factories.player_factory import PlayerFactory
from pokemon_app.data.repositories.player_repository import PlayerRepository


class InitializationService:
    """
    Handles application initialization tasks.
    """

    def __init__(self):
        pass

    def seed_initial_data(self, init_type: str):
        """
        Ensures the initial required data exists in the database.

        Parameters:
        init_type (str): The type of initialization, either "tests" or "production".
        """

        player_repo = PlayerRepository()

        if init_type == "tests":
            # Tests: create a player with id 2
            existing_player = player_repo.find_by_id(2)
            if existing_player is not None:
                try:
                    # Deleting the existing player
                    player_repo.delete(existing_player.id)
                except Exception as e:
                    logging.error(f"Error deleting existing player during tests: {e}")
                    raise

            # Special player for tests
            player = PlayerFactory().create_player_tests()
            player_repo.save(player)

        else:
            # Production: create or use a player with id 1
            existing_player = player_repo.find_by_id(1)

            if existing_player is None:
                try:
                    # Production player creation
                    player = PlayerFactory().create_player_prod()
                    player_repo.save(player)
                except Exception as e:
                    logging.error(f"Error seeding initial data for production: {e}")
                    raise

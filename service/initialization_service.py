import logging

from pokemon_app.core.factories.player_factory import PlayerFactory
from pokemon_app.data.repositories.player_repository import PlayerRepository


class InitializationService:
    """
    Handles application initialization tasks.
    """

    def __init__(self):
        pass

    @staticmethod
    def seed_initial_data():
        """
        Ensures the initial required data exists in the database.
        """
        existing_player = PlayerRepository.find_by_id(1)

        if existing_player is None:
            try:
                player = PlayerFactory().create_player_1()
                PlayerRepository().save(player)
            except Exception as e:
                logging.error(f"Error seeding initial data: {e}")
                raise

from models.Database import DatabaseSingleton
from models.Player import Player
from models.Models.PlayerModel import PlayerModel
from models.Models.PokemonRepository import PokemonRepository

db = DatabaseSingleton.get_instance().get_db()


class PlayerRepository:
    @staticmethod
    def save(player: Player) -> int:
        """
        Save a Player to the database
        """
        player_id = getattr(player, "id", None)
        player_model = None

        if player_id:
            player_model = PlayerModel.query.get(player_id)

        if player_model is None:
            player_model = PlayerModel(
                name=player.name,
                money=player.money,
                record_round=player.record_round,
                current_pokemon_id=None,
            )
            db.session.add(player_model)
            db.session.flush()
        else:
            player_model.name = player.name
            player_model.money = player.money
            player_model.record_round = player.record_round

        # Save pokemons
        if hasattr(player, "_pokemons"):
            for i, pokemon in enumerate(player.pokemons):
                if pokemon is not None:

                    # TODO : Overwrite the pokemon if it already exists
                    pokemon_id = PokemonRepository.save(pokemon, player_model.id)

                    if i == player.current_pokemon:
                        player_model.current_pokemon_id = pokemon_id

        db.session.commit()

        # if the player was new, set the id
        if not hasattr(player, "id"):
            player.id = player_model.id

        return player_model.id

    @staticmethod
    def find_by_id(player_id: int) -> Player | None:
        """
        Load a Player from the database
        """
        player_model = PlayerModel.query.get(player_id)
        if not player_model:
            return None

        player = Player()
        player.id = player_model.id
        player.name = player_model.name
        player.money = player_model.money
        player.record_round = player_model.record_round

        for i, pokemon_model in enumerate(player_model.pokemons):
            if i < 6:
                player.pokemons[i] = PokemonRepository.find_by_id(pokemon_model.id)

                if pokemon_model.id == player_model.current_pokemon_id:
                    player.current_pokemon = i

        return player

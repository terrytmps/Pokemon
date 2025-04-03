from models.Database import DatabaseSingleton
from models.Pokemon import Pokemon
from models.Models.PokemonModel import PokemonModel
from models.level.Level import Level
from models.level.XpDifficulty import XPDifficulty

db = DatabaseSingleton.get_instance().get_db()


class PokemonRepository:

    @staticmethod
    def delete_all_pokemons_player(player_id: int):
        """
        Delete all pokemons from a player
        """
        pokemons = PokemonModel.query.filter_by(player_id=player_id).all()
        for pokemon in pokemons:
            db.session.delete(pokemon)
        db.session.commit()

    @staticmethod
    def save(pokemon: Pokemon, player_id: int = None) -> int:
        """
        Save a Pokémon in the database
        """

        pokemon_id = getattr(pokemon, "id", None)
        pokemon_model = None

        if pokemon_id:
            pokemon_model = PokemonModel.query.get(pokemon_id)

        if pokemon_model is None:
            pokemon_model = PokemonModel(
                name=pokemon.name,
                player_id=player_id,
                level=pokemon.level,
            )
            db.session.add(pokemon_model)
        else:
            pokemon_model.name = pokemon.name
            pokemon_model.player_id = player_id
            pokemon_model.level = pokemon.level

        db.session.commit()

        if not hasattr(pokemon, "id"):
            pokemon.id = pokemon_model.id

        return pokemon_model.id

    @staticmethod
    def find_by_id(pokemon_id: int) -> Pokemon | None:
        """
        Load a pokemon from the database
        """
        pokemon_model = PokemonModel.query.get(pokemon_id)
        if not pokemon_model:
            return None

        pokemon = Pokemon(
            name=pokemon_model.name,
            level=Level(level=pokemon_model.level, xp_difficulty=XPDifficulty.EASY),
        )

        pokemon.id = pokemon_model.id

        return pokemon

from pokemon_app.data.Database import DatabaseSingleton
from pokemon_app.data.adapters.PokemonAdapter import PokemonAdapter
from pokemon_app.core.Pokemon import Pokemon
from pokemon_app.data.models.PokemonModel import PokemonModel

db = DatabaseSingleton.get_instance().get_db()


class PokemonRepository:

    @staticmethod
    def delete_all_pokemons_player(player_id: int):
        """
        Delete all pokemons for a given player from the database.
        """
        PokemonModel.query.filter_by(player_id=player_id).delete(
            synchronize_session=False
        )

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting pokemons for player {player_id}: {e}")
            raise

    @staticmethod
    def save(pokemon: Pokemon, player_id: int = None) -> int:
        """
        Save a Pokémon in the database. If the Pokémon already exists, it will be updated.
        """
        pokemon_model = PokemonAdapter.to_model(pokemon, player_id)
        original_pokemon_id = getattr(pokemon, "id", None)

        if pokemon_model.id is None:
            db.session.add(pokemon_model)
            try:
                db.session.flush()
            except Exception as e:
                db.session.rollback()
                print(f"Error flushing new pokemon {pokemon.name}: {e}")
                raise
        else:
            pass

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error committing pokemon {pokemon.name}: {e}")
            raise

        if original_pokemon_id is None and pokemon_model.id is not None:
            pokemon.id = pokemon_model.id

        return pokemon_model.id

    @staticmethod
    def find_by_id(pokemon_id: int) -> Pokemon | None:
        """
        Look up a Pokémon by its ID in the database.
        """
        pokemon_model = db.session.get(PokemonModel, pokemon_id)

        if pokemon_model:
            return PokemonAdapter.from_model(pokemon_model)
        else:
            return None

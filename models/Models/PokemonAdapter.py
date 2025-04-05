from models.Models.PokemonModel import PokemonModel
from models.Pokemon import Pokemon
from models.level.Level import Level
from models.level.XpDifficulty import XPDifficulty
from models.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PokemonAdapter:
    @staticmethod
    def to_model(pokemon: Pokemon, player_id: int = None) -> PokemonModel:
        """
        Convert an object of domain Pokemon to a PokemonModel (for the database).
        """
        pokemon_model = None
        pokemon_id = getattr(pokemon, "id", None)

        if pokemon_id:
            pokemon_model = db.session.get(PokemonModel, pokemon_id)

        if pokemon_model is None:
            pokemon_model = PokemonModel()

        pokemon_model.name = pokemon.name
        pokemon_model.player_id = player_id

        if isinstance(pokemon.level, Level):
            pokemon_model.level = pokemon.level.level
        elif isinstance(pokemon.level, int):
            pokemon_model.level = pokemon.level
        else:
            raise TypeError(
                f"Attribut 'level' du Pokemon doit être un objet Level ou un int, mais reçu {type(pokemon.level)}"
            )

        return pokemon_model

    @staticmethod
    def from_model(pokemon_model: PokemonModel) -> Pokemon | None:
        """
        Convert a PokemonModel (from the database) to a domain Pokemon object.
        """
        if not pokemon_model:
            return None

        level_obj = Level(level=pokemon_model.level, xp_difficulty=XPDifficulty.EASY)

        pokemon = Pokemon(
            name=pokemon_model.name,
            level=level_obj,
        )

        pokemon.id = pokemon_model.id

        return pokemon

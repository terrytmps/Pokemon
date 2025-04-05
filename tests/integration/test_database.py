import pytest
from models.Database import DatabaseSingleton
from models.Models.PlayerModel import PlayerModel
from models.Models.PokemonModel import PokemonModel
from models.Models.PokemonRepository import PokemonRepository
from models.Models.PlayerRepository import PlayerRepository
from models.Player import Player
from models.Pokemon import Pokemon
from models.level.Level import Level
from models.level.XpDifficulty import XPDifficulty

db = DatabaseSingleton.get_instance().get_db()


@pytest.fixture(scope="module")
def setup_db(app):
    """Setup the database before running tests."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


def test_create_player(setup_db):
    """Test the creation and saving of a Player."""
    player = Player()
    player.name = "Ash"
    player.money = 1000
    player.record_round = 5

    player_id = PlayerRepository.save(player)

    loaded_player = PlayerRepository.find_by_id(player_id)

    assert loaded_player is not None
    assert loaded_player.name == "Ash"
    assert loaded_player.money == 1000
    assert loaded_player.record_round == 5


def test_create_pokemon(setup_db):
    """Test the creation and saving of a Pokémon."""
    pokemon = Pokemon(name="Pikachu", level=Level(5, XPDifficulty.EASY))

    pokemon_id = PokemonRepository.save(pokemon)

    loaded_pokemon = PokemonRepository.find_by_id(pokemon_id)

    assert loaded_pokemon is not None
    assert loaded_pokemon.name == "Pikachu"
    assert loaded_pokemon.level == 5


def test_assign_pokemon_to_player(setup_db):
    """Test assigning a Pokémon to a Player."""
    player = Player()
    player.name = "Red"
    player.money = 500
    player.record_round = 3

    player_id = PlayerRepository.save(player)

    pokemon = Pokemon(name="Pikachu", level=Level(8, XPDifficulty.EASY))
    pokemon_id = PokemonRepository.save(pokemon, player_id)

    loaded_player = PlayerRepository.find_by_id(player_id)

    assert loaded_player is not None
    assert len(loaded_player.pokemons) == 6
    assert loaded_player.pokemons[0].name == "Pikachu"


def test_delete_player(setup_db):
    """Test deleting a Player and its associated Pokémon."""
    player = Player()
    player.name = "Misty"
    player.money = 700
    player.record_round = 4

    player_id = PlayerRepository.save(player)

    pokemon = Pokemon(name="Pikachu", level=Level(10, XPDifficulty.EASY))
    PokemonRepository.save(pokemon, player_id)

    PlayerRepository.find_by_id(player_id)
    db.session.delete(db.session.get(PlayerModel, player_id))
    db.session.commit()

    deleted_player = PlayerRepository.find_by_id(player_id)

    assert deleted_player is None

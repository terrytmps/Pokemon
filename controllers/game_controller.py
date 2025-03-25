from flask import render_template, Blueprint

from models.Player import Player
from models.factory.PokemonFactory import PokemonFactory
from models.level.Stats import Stat
from models.status.StatusEnum import StatusEnum
from models.Battle import Battle
from models.factory.MoveFactory import MoveFactory

game_controller = Blueprint("game_controller", __name__)


@game_controller.route("/game")
def game():
    """
    Game endpoints handle the combat part
    """

    player = Player()
    pokemon_self = PokemonFactory.created_pikachu()
    pokemon_self.set_status(StatusEnum.SLEEP)
    pokemon_self.current_hp = 24

    stat = Stat(1, 1, 1, 1, 1, 1, 100, 100, 100, 100, 100, 100)
    pokemon_2 = PokemonFactory.created_leviator()

    player.add_pokemon(pokemon_self)
    player.add_pokemon(pokemon_2)
    player.set_current_pokemon(1)

    pokemon_op = PokemonFactory.created_dracaufeu()

    pokemon_op.set_status(StatusEnum.POISON)
    pokemon_op.current_hp = 5

    # Create battle
    battle = Battle(pokemon_self, pokemon_2)
    """ 
    # Perform a turn
    battle.battle_turn(
        player_move=MoveFactory.get_move("Éclair"),
        opponent_move=MoveFactory.get_move("Lance-Flamme"),
    )

    # Get battle log
    battle_log = battle.get_battle_log()
    for log in battle_log:
        print(log) """

    return render_template("pages/game.html", player=player, pokemon_op=pokemon_op)


@game_controller.route("/")
def menu():
    """
    Main menu  (where player buy pokemons, etc
    """
    player = Player()

    pokemon_1 = PokemonFactory.created_pikachu()
    pokemon_2 = PokemonFactory.created_leviator()
    pokemon_3 = PokemonFactory.created_dracaufeu()

    pokemons = [
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_3,
        pokemon_3,
        pokemon_2,
        pokemon_1,
        pokemon_3,
        pokemon_2,
        pokemon_3,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_3,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_3,
        pokemon_2,
        pokemon_2,
        pokemon_1,
        pokemon_3,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_3,
    ]
    player.add_pokemon(pokemon_1)
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)

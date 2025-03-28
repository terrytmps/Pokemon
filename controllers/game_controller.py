from flask import render_template, Blueprint

from models.Player import Player
from models.factory.PokemonFactory import PokemonFactory
from models.level.Stats import Stat
from models.status.PoisonStatusStrategy import PoisonStatusStrategy
from models.status.SleepStatusStrategy import SleepStatusStrategy
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
    pokemon_self = PokemonFactory.create_pikachu()
    pokemon_self.current_hp = 24

    pokemon_2 = PokemonFactory.create_leviator()

    player.add_pokemon(pokemon_self)
    player.add_pokemon(pokemon_2)
    player.set_current_pokemon(1)

    pokemon_2.current_hp = 24
    pokemon_2.status_strategy = SleepStatusStrategy()

    pokemon_op = PokemonFactory.create_dracaufeu()

    pokemon_op.status_strategy = PoisonStatusStrategy()

    """ # Create battle
    battle = Battle(pokemon_self, pokemon_2)

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
    pokemons = PokemonFactory.get_shop_pokemons()
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)

from flask import render_template, Blueprint

from models.Battle import Battle
from models.Player import Player
from models.RoundGenerator import RoundGenerator
from models.factory.PokemonFactory import PokemonFactory

game_controller = Blueprint("game_controller", __name__)

battle: Battle

@game_controller.route("/game")
def game():
    """
    Game endpoints handle the combat part
    """

    player = Player()
    pokemon_self = PokemonFactory.create_pikachu()
    player.add_pokemon(pokemon_self)

    pokemon_op = RoundGenerator.get_instance().generate_round()
    # create a battle instance that saved for other call
    global battle
    battle = Battle(player.get_current_pokemon(), pokemon_op)


    return render_template("pages/game.html", player=player, pokemon_op=pokemon_op)


"""
Perform a attack choose by the player return the update pokemon_opponent
"""
@game_controller.route("/attack/<attack_id>")
def attack(attack_id):
    global battle

    possible_winner = battle.battle_turn()
from flask import render_template, Blueprint, redirect, url_for, jsonify

from service.GameService import (
    game_perform_attack,
    game_perform_change,
    player,
    create_battle,
    forfet,
    battle_log_get,
    is_winner_back,
)

game_controller = Blueprint("game_controller", __name__)


@game_controller.route("/game", methods=["GET", "POST"])
def game():
    """
    Game endpoints handle the combat part
    """
    battle_created = create_battle()
    return render_template(
        "pages/game.html", player=player, pokemon_op=battle_created.opponent_pokemon
    )


"""
Perform a attack choose by the player return the update pokemon_opponent
"""


@game_controller.route("/attack/<attack_id>", methods=["POST"])
def attack_pokemon(attack_id):
    return game_perform_attack(int(attack_id))


"""
Perform a change of pokemon choose by the player
"""


@game_controller.route("/change/<pokemon_id>", methods=["POST"])
def change_pokemon(pokemon_id):
    return game_perform_change(int(pokemon_id))


"""
Forfeit the game
"""


@game_controller.route("/forfeit", methods=["POST"])
def forfeit():
    forfet()
    return jsonify({"redirect": url_for("shop_controller.menu")})


@game_controller.route("/is/winner", methods=["PUT"])
def is_winner():
    pokemon = is_winner_back()
    # if pokemon is type pokemon return jsonify .to_dict() else return pokemon
    if hasattr(pokemon, "to_dict"):
        return jsonify(pokemon.to_dict())
    return jsonify(pokemon)


@game_controller.route("/battle_log")
def get_last_battle_log():
    return jsonify(battle_log_get())

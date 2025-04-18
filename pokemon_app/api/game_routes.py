from flask import render_template, Blueprint, url_for, jsonify, request

from pokemon_app.data.repositories.player_repository import PlayerRepository
from service.game_service import (
    game_perform_attack,
    game_perform_change,
    init_battle,
    create_battle,
    forfet,
    battle_log_get,
    is_winner_back,
    get_current_battle,
)

from pokemon_app.core.ai.random_attack_strategy import RandomAttackStrategy
from pokemon_app.core.ai.highest_damage_strategy import HighestDamageStrategy

game_controller = Blueprint("game_controller", __name__)


@game_controller.route("/game", methods=["GET", "POST"])
def game():
    """
    Game endpoints handle the combat part
    """
    player = PlayerRepository().find_by_id(1)
    init_battle()
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


@game_controller.route("/change_strategy", methods=["POST"])
def change_strategy():
    data = request.get_json()
    strategy = data.get("strategy", "highest_damage")

    battle = get_current_battle()
    if battle:
        if strategy == "random":
            battle.opponent_strategy = RandomAttackStrategy()
            return jsonify(
                {"message": "Stratégie changée en aléatoire.", "strategy": "random"}
            )
        elif strategy == "highest_damage":
            battle.opponent_strategy = HighestDamageStrategy()
            return jsonify(
                {
                    "message": "Stratégie changée en dégâts maximums.",
                    "strategy": "highest_damage",
                }
            )
        else:
            return jsonify({"error": "Stratégie invalide."}), 400
    else:
        return jsonify({"error": "Aucune bataille en cours."}), 400

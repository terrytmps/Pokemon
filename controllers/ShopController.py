from flask import request, jsonify
from flask import render_template, Blueprint

from models.Models.PlayerRepository import PlayerRepository
from models.factory.PokemonFactory import PokemonFactory

shop_controller = Blueprint("shop_controller", __name__)


@shop_controller.route("/")
def menu():
    """
    Main menu  (where player buy Pokémon, etc.)
    """
    player = PlayerRepository().find_by_id(1)
    pokemons = PokemonFactory.get_shop_pokemons()
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)


@shop_controller.route("/buy_pokemon", methods=["POST"])
def buy_pokemon():
    data = request.get_json()

    shop_index = data.get("pokemon_shop_index")
    team_slot_index = data.get("team_slot_index")

    # Validate shop_index
    if shop_index is None:
        return jsonify({"success": False, "message": "Aucun Pokémon sélectionné."}), 400

    try:
        shop_index_int = int(shop_index)
    except (ValueError, TypeError):
        return (
            jsonify({"success": False, "message": "Indice de Pokémon invalide."}),
            400,
        )

    shop_pokemons = PokemonFactory.get_shop_pokemons()

    if shop_index_int < 0 or shop_index_int >= len(shop_pokemons):
        return (
            jsonify({"success": False, "message": "Indice de Pokémon invalide."}),
            400,
        )

    selected_pokemon = shop_pokemons[shop_index_int]

    player = PlayerRepository().find_by_id(1)

    if player.money < selected_pokemon.price:
        return jsonify({"success": False, "message": "Fonds insuffisants."}), 400

    player.money -= selected_pokemon.price
    player.pokemons[team_slot_index] = selected_pokemon
    PlayerRepository().save(player)

    return jsonify(
        {
            "success": True,
            "new_money": player.money,
            "pokemon": {
                "name": selected_pokemon.name,
                "sprite_url": selected_pokemon._sprite_url,
                "level": selected_pokemon.level,
            },
        }
    )

from flask import request, jsonify
from flask import render_template, Blueprint
from models.factory.PokemonFactory import PokemonFactory
from models.player_adapter import PlayerDBAdapter

shop_controller = Blueprint("shop_controller", __name__)


@shop_controller.route("/")
def menu():
    """
    Main menu  (where player buy Pokémon, etc.)
    """
    player = PlayerDBAdapter().get_unique_player()
    pokemons = PokemonFactory.get_shop_pokemons()
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)


@shop_controller.route("/buy_pokemon", methods=["POST"])
def buy_pokemon():
    """
    Buy a Pokémon from the shop
    """
    data = request.get_json()

    shop_index = data.get("pokemon_shop_index")
    team_slot_index = data.get("team_slot_index")

    player_adapter = PlayerDBAdapter()
    player = player_adapter.get_unique_player()
    shop_pokemons = PokemonFactory.get_shop_pokemons()

    selected_pokemon = shop_pokemons[int(shop_index)]

    # Check if player has enough money
    if player.money < selected_pokemon.price:
        return jsonify(
            {"success": False, "message": "Pas assez d'argent pour acheter ce Pokémon!"}
        )

    player.money -= selected_pokemon.price
    player.pokemons[int(team_slot_index)] = selected_pokemon

    player_adapter.update_player(player)

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

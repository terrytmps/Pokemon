from pokemon_app.data.repositories.player_repository import PlayerRepository


def test_menu_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Monstres de poche" in response.data
    assert b"Pikachu" in response.data


def test_buy_pokemon_success(client, app):
    with app.app_context():
        player_before = PlayerRepository().find_by_id(1)
        initial_money = player_before.money
        initial_pokemon_slot_0 = player_before.pokemons[0]

    response = client.post(
        "/buy_pokemon", json={"pokemon_shop_index": 0, "team_slot_index": 0}
    )

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["success"] is True
    assert "new_money" in json_data
    assert "pokemon" in json_data
    assert json_data["pokemon"]["name"] == "Chrysacier"

    with app.app_context():
        player_after = PlayerRepository().find_by_id(1)
        assert player_after.money < initial_money
        assert player_after.money == json_data["new_money"]
        assert player_after.pokemons[0] is not initial_pokemon_slot_0
        assert player_after.pokemons[0].name == "Chrysacier"


def test_buy_pokemon_insufficient_funds(client, app):
    from pokemon_app.core.factories.pokemon_factory import PokemonFactory

    with app.app_context():
        player = PlayerRepository().find_by_id(1)
        player.money = 10
        PlayerRepository().save(player)

        shop_pokemons = PokemonFactory.get_shop_pokemons()
        pokemon_price = shop_pokemons[8].price  # Evoli (15$)
        assert player.money < pokemon_price

    response = client.post(
        "/buy_pokemon", json={"pokemon_shop_index": 8, "team_slot_index": 0}
    )

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert json_data["message"] == "Fonds insuffisants."

    with app.app_context():
        player_after = PlayerRepository().find_by_id(1)
        assert player_after.money == 10


def test_buy_pokemon_invalid_index(client):
    response = client.post(
        "/buy_pokemon", json={"pokemon_shop_index": 999, "team_slot_index": 0}
    )

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["success"] is False
    assert json_data["message"] == "Indice de Pokémon invalide."


def test_404_error(client):
    response = client.get("/cette-page-n-existe-pas")
    assert response.status_code == 404
    assert b"la page que vous recherchez" in response.data

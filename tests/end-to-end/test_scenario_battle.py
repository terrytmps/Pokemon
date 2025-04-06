from pokemon_app.data.repositories.player_repository import PlayerRepository


def test_e2e_buy_evoli_battle_attack_forfeit(client, app):
    """
    Test E2E: Le joueur va au shop, achète Évoli dans le slot 1 (index 0),
    va au combat, lance la première attaque, puis abandonne.
    """
    with app.app_context():
        player_repo = PlayerRepository()
        player = player_repo.find_by_id(1)

        evoli_shop_index = 8
        evoli_price = 15
        evoli_name = "Évoli"

        initial_money = player.money
        initial_pokemon_slot_0 = player.pokemons[0]

        # --- 1. Enter the shop ---
        response_menu = client.get("/")
        assert response_menu.status_code == 200
        assert b"Monstres de poche" in response_menu.data

        # --- 2. Buy Pokémon ---
        response_buy = client.post(
            "/buy_pokemon",
            json={"pokemon_shop_index": evoli_shop_index, "team_slot_index": 0},
        )
        assert response_buy.status_code == 200
        buy_data = response_buy.get_json()
        assert buy_data["success"] is True
        assert "new_money" in buy_data
        assert buy_data["new_money"] == initial_money - evoli_price
        assert "pokemon" in buy_data
        assert buy_data["pokemon"]["name"] == evoli_name

        # Check if the Pokémon was added to the player's team
        player_after_buy = player_repo.find_by_id(1)
        assert player_after_buy.money == initial_money - evoli_price
        assert player_after_buy.pokemons[0].name == evoli_name
        assert player_after_buy.pokemons[0] is not initial_pokemon_slot_0
        assert player_after_buy.pokemons[1].name == "Tyranocif"

        # Check if the other Pokémon slots are None
        for i in range(2, len(player_after_buy.pokemons)):
            assert player_after_buy.pokemons[i] is None

        # --- 3. Go to battle ---
        response_game = client.get("/game")
        assert response_game.status_code == 200
        assert b"une action" in response_game.data

        # --- 4. Launch the first attack ---
        response_attack = client.post("/attack/0")
        assert response_attack.status_code == 200
        attack_data = response_attack.get_json()

        # Check if the attack was successful
        assert isinstance(attack_data, list)
        assert len(attack_data) >= 4
        assert isinstance(attack_data[0], bool)
        assert isinstance(attack_data[1], bool)
        assert isinstance(attack_data[2], dict)
        assert isinstance(attack_data[3], dict)
        assert "hp_current" in attack_data[2]
        assert "hp_current" in attack_data[3]

        response_log = client.get("/battle_log")
        assert response_log.status_code == 200
        log_data = response_log.get_json()
        assert isinstance(log_data, str)
        # because Salamèche's attack is before Evoli's attack
        assert "Salamèche" in log_data or "attaque" in log_data

        # --- 5. Forfeit the battle ---
        response_forfeit = client.post("/forfeit")
        assert response_forfeit.status_code == 200
        forfeit_data = response_forfeit.get_json()
        assert "redirect" in forfeit_data
        assert forfeit_data["redirect"] == "/"

        player_after_forfeit = player_repo.find_by_id(1)
        money_after_attack = player_after_buy.money
        expected_gain = 0
        assert player_after_forfeit.money == money_after_attack + expected_gain

from bs4 import BeautifulSoup


def test_e2e_shop_battle_rounds_forfeit(client, app):
    """
    Teste le scénario end-to-end : L'utilisateur va sur le shop, démarre un combat, lance sa première attaque puis
    abandonne le combat.
    """
    with app.app_context():
        # --- 1. Go to the shop ---
        response = client.get("/")
        assert response.status_code == 200
        assert b"Monstres de poche" in response.data
        assert b"Record:" in response.data

        # --- 2. Go to battle ---
        response = client.get("/game")
        assert response.status_code == 200
        assert b"une action" in response.data

        # --- 3. Launch the first attack ---
        response_attack_json = client.post("/attack/0")
        assert response_attack_json.status_code == 200

        attack_data = response_attack_json.get_json()

        # Check if the attack was successful
        assert isinstance(attack_data, list)
        assert len(attack_data) == 4
        player_state_json = attack_data[2]
        opponent_state_json = attack_data[3]

        assert "first_move" in player_state_json
        assert player_state_json["name"] == "Aquali"  # Pokemons player
        assert opponent_state_json["name"] == "Salamèche"  # Pokemons opponent
        assert player_state_json["first_move"]["name"] == "Hydrocanon"  # First move

        response_game_after_attack = client.get("/game")
        assert response_game_after_attack.status_code == 200

        # Check if the response contains the expected HTML elements
        soup = BeautifulSoup(response_game_after_attack.data, "html.parser")

        player_div = soup.find(id="pokemon-joueur")
        assert player_div is not None

        # Check if the player's Pokémon name is displayed correctly
        player_name_tag = player_div.find(id="pokemon_self_name")
        assert player_name_tag is not None
        assert player_name_tag.string.strip() == player_state_json["name"]  # "Aquali"

        # Check if the player's HP is displayed correctly
        player_hp_tag = player_div.find(id="pokemon_display_self_hp_text")
        assert player_hp_tag is not None, "Texte HP Pokémon joueur non trouvé"
        assert int(player_state_json["hp_current"]) <= int(
            player_state_json["hp_max"]
        ), "HP joueur non mis à jour après l'attaque"

        # Check if the player's first move button is displayed correctly
        attack_div = soup.find(id="display-parent-move")
        player_move1_button = attack_div.find(
            id="attaque_button0"
        )  # Cherche dans la div joueur
        assert player_move1_button is not None, "Bouton Attaque 0 non trouvé"
        assert (
            player_move1_button.get_text(strip=True)
            == player_state_json["first_move"]["name"]
        )  # "Hydrocanon"

        opponent_div = soup.find(id="pokemon-adversaire")
        assert opponent_div is not None, "Div Pokémon adversaire non trouvée"

        opponent_name_tag = opponent_div.find(id="pokemon_op_name")
        assert opponent_name_tag is not None, "Nom Pokémon adversaire non trouvé"
        assert (
            opponent_name_tag.string.strip() == opponent_state_json["name"]
        )  # "Salamèche"

        # Check if the opponent's HP is displayed correctly
        opponent_hp_tag = opponent_div.find(id="pokemon_display_op_hp_text")
        assert opponent_hp_tag is not None, "Texte HP Pokémon adversaire non trouvé"
        assert int(opponent_state_json["hp_current"]) <= int(
            opponent_state_json["hp_max"]
        ), "HP adversaire non mis à jour après l'attaque"

        # --- 4. Forfeit the battle ---
        response = client.post("/forfeit")
        assert response.status_code == 200

        data = response.get_json()
        assert isinstance(data, dict)
        assert "redirect" in data

        redirect_url = data["redirect"]
        assert redirect_url == "/"

        response = client.get(redirect_url)
        assert response.status_code == 200
        assert b"Monstres de poche" in response.data
        assert b"Record:" in response.data

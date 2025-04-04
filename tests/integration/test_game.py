import pytest
from flask import url_for
from models.Models.PlayerRepository import PlayerRepository
from service.GameService import get_current_battle


def test_game_page_loads(client):
    """Check if the game page loads correctly."""
    response = client.get("/game")
    assert response.status_code == 200
    assert b"une action" in response.data


def test_attack_pokemon(client, app):
    """Check if the attack action works correctly."""
    with app.app_context():
        client.get("/game")

        response = client.post("/attack/0")
        assert response.status_code == 200

        data = response.get_json()

        assert isinstance(data, list)
        assert len(data) >= 3

        is_first_player_turn = data[0]
        is_attack_successful = data[1]
        opponent_data = data[2]

        assert isinstance(is_first_player_turn, bool)
        assert isinstance(is_attack_successful, bool)
        assert isinstance(opponent_data, dict)
        assert "hp_current" in opponent_data
        assert "name" in opponent_data


def test_change_pokemon(client, app):
    """Check if the change pokemon action works correctly."""
    with app.app_context():
        client.get("/game")

        response = client.post("/change/1")
        assert response.status_code == 200

        data = response.get_json()

        assert isinstance(data, list)
        assert len(data) == 2

        opponent_pokemon = data[0]
        current_player_pokemon = data[1]

        assert isinstance(opponent_pokemon, dict)
        assert isinstance(current_player_pokemon, dict)

        assert "name" in current_player_pokemon
        assert "hp_current" in current_player_pokemon
        assert current_player_pokemon["hp_current"] >= 0


def test_forfeit_redirect(client):
    """Check if the forfeit action redirects correctly."""
    response = client.post("/game")
    assert response.status_code == 200

    response = client.post("/forfeit")
    assert response.status_code == 200
    data = response.get_json()
    assert "redirect" in data
    assert "/" in data["redirect"]


def test_is_winner(client, app):
    """Check if the is_winner action works correctly."""
    with app.app_context():
        client.get("/game")
        response = client.put("/is/winner")
        assert response.status_code == 200
        data = response.get_json()
        assert data is False


def test_battle_log(client, app):
    """Check if the battle log action works correctly."""
    with app.app_context():
        client.get("/game")
        response = client.get("/battle_log")
        assert response.status_code == 200
        data = response.get_json()
        # at the beginning, the battle log should be empty
        assert data == ""


@pytest.mark.parametrize(
    "strategy, expected_message",
    [
        ("random", "Stratégie changée en aléatoire."),
        ("highest_damage", "Stratégie changée en dégâts maximums."),
        ("invalid", "Stratégie invalide."),
    ],
)
def test_change_strategy(client, app, strategy, expected_message):
    """Teste le changement de stratégie IA pendant le combat."""
    with app.app_context():
        client.get("/game")

        response = client.post("/change_strategy", json={"strategy": strategy})
        data = response.get_json()

        if strategy == "invalid":
            assert response.status_code == 400
            assert "error" in data
        else:
            assert response.status_code == 200
            assert data["message"] == expected_message
            assert data["strategy"] == strategy

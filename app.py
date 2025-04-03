from flask import Flask, render_template
from models.Database import DatabaseSingleton
from models.factory.PlayerFactory import PlayerFactory

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_singleton = DatabaseSingleton.get_instance(app)
db = db_singleton.get_db()

from models.Models.PlayerRepository import PlayerRepository
from controllers.GameController import game_controller
from controllers.ShopController import shop_controller


# TODO : move this to a service
def initialize_database():
    if PlayerRepository.find_by_id(1) is not None:
        return

    else:
        player = PlayerFactory().create_player_1()
        player_id = PlayerRepository().save(player)


with app.app_context():
    # db.drop_all()
    db.create_all()
    initialize_database()

app.register_blueprint(game_controller)
app.register_blueprint(shop_controller)


# Gestion des erreurs 404 et 500
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)

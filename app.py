from flask import Flask, render_template
from pokemon_app.data.database import DatabaseSingleton

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_singleton = DatabaseSingleton.get_instance(app)
db = db_singleton.get_db()

from pokemon_app.api.game_routes import game_controller
from pokemon_app.api.shop_routes import shop_controller

from service.initialization_service import InitializationService

with app.app_context():
    db.create_all()
    initializer = InitializationService()
    initializer.seed_initial_data("prod")

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

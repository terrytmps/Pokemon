from flask import Flask, render_template, request
from models.Database import DatabaseSingleton
from controllers.game_controller import game_controller
from controllers.shop_controller import shop_controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_singleton = DatabaseSingleton.get_instance(app)
db = db_singleton.get_db()

with app.app_context():
    db.create_all()

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

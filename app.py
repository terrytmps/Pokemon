from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from controllers.game_controller import game_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

app.register_blueprint(game_controller)

# Gestion de la page d'erreur 404 (Page non trouvée)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

# Gestion de la page d'erreur 500 (Erreur interne du serveur)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)

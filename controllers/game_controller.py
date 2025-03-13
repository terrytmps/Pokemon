from flask import render_template, Blueprint
game_controller = Blueprint("game_controller", __name__)

@game_controller.route("/")
def game():
    return render_template("pages/game.html")

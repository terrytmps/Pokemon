from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("pages/game.html")


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

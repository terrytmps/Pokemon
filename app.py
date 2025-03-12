from flask import Flask, render_template, request
from models.Surveillance import Surveillance
from models.Mesure import Mesure
from models.Enums.MeasureType import MeasureType
from datetime import datetime

from service.MonitoringService import MonitoringService

app = Flask(__name__)
surveillance = Surveillance()


@app.route("/dashboard")
def dashboard():
    # Dans un prochain atelier nous allons récupérer les données réelles
    data = {
        "temperature_moyenne": 22,
        "alertes_actives": 2,
        "pieces_surveillees": 4,
        "dernier_releve": "10:30",
    }
    return render_template("pages/dashboard.html", data=data)


@app.route("/details")
def detail():
    return render_template("pages/details.html")


@app.route("/history")
def history():
    return render_template("pages/history.html")


@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route("/", methods=["GET", "POST"])
def index():
    monitoringService = MonitoringService()
    messages = []
    if request.method == "POST":

        messages = monitoringService.handle_form(request, surveillance)

    return render_template("pages/index.html", messages=messages)


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

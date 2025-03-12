from datetime import datetime

from models.Enums.MeasureType import MeasureType
from models.Mesure.Mesure import Mesure
from models.Mesure.MesureDureeInactivite import MesureDureeInactivite
from models.Mesure.MesureDureeSortie import MesureDureeSortie
from models.Mesure.MesureHeureSortie import MesureHeureSortie
from models.Mesure.MesureTemperature import MesureTemperature
from models.Enums.LevelAlert import LevelAlert


class MonitoringService:
    """
    Responsable de la logique métier

    """

    def __init__(self):
        pass

    def _get_mesure_temperature(self, request) -> Mesure:
        return MesureTemperature(
            value=float(request.form.get("temperature", 0)),
            timestamp=datetime.now(),
        )

    def _get_mesure_sortie(self, request) -> Mesure:
        return MesureHeureSortie(
            value=float(request.form.get("heure_sortie", 0)),
            timestamp=datetime.now(),
        )

    def _get_mesure_duree_sortie(self, request) -> Mesure:
        return MesureDureeSortie(
            value=float(request.form.get("duree_sortie", 0)),
            timestamp=datetime.now(),
        )

    def _get_mesure_duree_inactivite(self, request) -> Mesure:
        return MesureDureeInactivite(
            value=float(request.form.get("duree_inactivite", 0)),
            timestamp=datetime.now(),
        )

    def _handle_alert(self, surveillance, mesure) -> tuple:
        return surveillance.handleAlert(mesure).to_tuple()

    """
    S'occupe de toute la partie métier du logiciel
    """

    def handle_form(self, request, surveillance):
        messages = []
        try:
            messages.append(
                self._handle_alert(surveillance, self._get_mesure_temperature(request))
            )
            messages.append(
                self._handle_alert(surveillance, self._get_mesure_sortie(request))
            )
            messages.append(
                self._handle_alert(surveillance, self._get_mesure_duree_sortie(request))
            )
            messages.append(
                self._handle_alert(
                    surveillance, self._get_mesure_duree_inactivite(request)
                )
            )
        except ValueError:
            messages.append(
                (
                    LevelAlert.DANGER,
                    "Erreur : Veuillez entrer des valeurs numériques valides",
                )
            )
        return messages

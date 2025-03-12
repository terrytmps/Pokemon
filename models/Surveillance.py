from models.Alert import Alert
from models.Enums.MeasureType import MeasureType


class Surveillance:
    """
    Surveillance : Système global de surveillance
        • Gère les Alert
        • Analyse les Situation
        • Collecte les Mesures

    Attributs:
        seuil_temperature_inferieur
        seuil_temperature_superieur
        horaire_sortie_tard
        duree_sortie_prolongee
        durée_inactivite_prolongee
    """

    def __init__(self):
        self._seuil_temperature_inferieur = 10
        self._seuil_temperature_superieur = 25
        self._horaire_sortie_tard = 22
        self._duree_sortie_prolongee = 8
        self._duree_inactivite_prolongee = 2

    @property
    def seuil_temperature_inferieur(self):
        return self._seuil_temperature_inferieur

    @property
    def seuil_temperature_superieur(self):
        return self._seuil_temperature_superieur

    @property
    def horaire_sortie_tard(self):
        return self._horaire_sortie_tard

    @property
    def duree_sortie_prolongee(self):
        return self._duree_sortie_prolongee

    @property
    def duree_inactivite_prolongee(self):
        return self._duree_inactivite_prolongee

    def handleAlert(self, mesure):
        return mesure.validate_value()

    def monitorHome(self):
        pass

    def analyseSituation(self):
        pass

""" @pytest.fixture
def surveillance():
    return Surveillance()


@pytest.fixture
def fixed_timestamp():
    return datetime.now()


def create_mesure(mesure_type, value, timestamp):
    if mesure_type == MeasureType.TEMPERATURE:
        return MesureTemperature(value, timestamp)
    if mesure_type == MeasureType.HEURE_SORTIE:
        return MesureHeureSortie(value, timestamp)
    if mesure_type == MeasureType.DUREE_SORTIE:
        return MesureDureeSortie(value, timestamp)
    if mesure_type == MeasureType.DUREE_INACTIVITE:
        return MesureDureeInactivite(value, timestamp)
    else:
        raise ValueError(f"Aucune classe Mesure correspondante pour {mesure_type}")


class TestSurveillance:

    def test_seuils_par_defaut(self, surveillance):
        assert surveillance.seuil_temperature_inferieur == 10
        assert surveillance.seuil_temperature_superieur == 25
        assert surveillance.horaire_sortie_tard == 22
        assert surveillance.duree_sortie_prolongee == 8
        assert surveillance.duree_inactivite_prolongee == 2

    @pytest.mark.parametrize(
        "temperature, expected_message, expected_niveau",
        [
            (9, "Température trop basse!", LevelAlert.DANGER),
            (26, "Température trop élevée!", LevelAlert.DANGER),
            (15, "Température normale", LevelAlert.SUCCESS),
            (10, "Température normale", LevelAlert.SUCCESS),
            (25, "Température normale", LevelAlert.SUCCESS),
        ],
    )
    def test_handle_temperature_alert(
        self,
        surveillance,
        fixed_timestamp,
        temperature,
        expected_message,
        expected_niveau,
    ):
        mesure = create_mesure(MeasureType.TEMPERATURE, temperature, fixed_timestamp)
        alerte = surveillance.handleAlert(mesure)
        assert isinstance(alerte, Alert)
        assert alerte.message == expected_message
        assert alerte.niveau_gravite == expected_niveau

    @pytest.mark.parametrize(
        "heure, expected_message, expected_niveau",
        [
            (23, "Alerte : Sortie tardive!", LevelAlert.DANGER),
            (18, "Heure de sortie correcte", LevelAlert.SUCCESS),
            (22, "Heure de sortie correcte", LevelAlert.SUCCESS),
        ],
    )
    def test_handle_heure_sortie_alert(
        self, surveillance, fixed_timestamp, heure, expected_message, expected_niveau
    ):
        mesure = create_mesure(MeasureType.HEURE_SORTIE, heure, fixed_timestamp)
        alerte = surveillance.handleAlert(mesure)
        assert isinstance(alerte, Alert)
        assert alerte.message == expected_message
        assert alerte.niveau_gravite == expected_niveau

    @pytest.mark.parametrize(
        "duree, expected_message, expected_niveau",
        [
            (9, "Alerte : Sortie prolongée!", LevelAlert.DANGER),
            (7, "Durée de sortie correcte", LevelAlert.SUCCESS),
            (8, "Durée de sortie correcte", LevelAlert.SUCCESS),
        ],
    )
    def test_handle_duree_sortie_alert(
        self, surveillance, fixed_timestamp, duree, expected_message, expected_niveau
    ):
        mesure = create_mesure(MeasureType.DUREE_SORTIE, duree, fixed_timestamp)
        alerte = surveillance.handleAlert(mesure)
        assert isinstance(alerte, Alert)
        assert alerte.message == expected_message
        assert alerte.niveau_gravite == expected_niveau

    @pytest.mark.parametrize(
        "duree, expected_message, expected_niveau",
        [
            (3, "Alerte : Inactivité prolongée!", LevelAlert.DANGER),
            (1, "Durée d'inactivité correcte", LevelAlert.SUCCESS),
            (2, "Durée d'inactivité correcte", LevelAlert.SUCCESS),
        ],
    )
    def test_handle_duree_inactivite_alert(
        self, surveillance, fixed_timestamp, duree, expected_message, expected_niveau
    ):
        mesure = create_mesure(MeasureType.DUREE_INACTIVITE, duree, fixed_timestamp)
        alerte = surveillance.handleAlert(mesure)
        assert isinstance(alerte, Alert)
        assert alerte.message == expected_message
        assert alerte.niveau_gravite == expected_niveau """

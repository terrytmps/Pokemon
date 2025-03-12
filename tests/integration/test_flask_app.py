import unittest
from app import app


class Test_flask_app(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)  # Vérifie que la route charge bien
        self.assertIn(
            b"Accueil", response.data
        )  # Vérifie si "Accueil" est présent dans le HTML

    def test_dashboard_route(self):
        response = self.client.get("/dashboard")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tableau de bord", response.data)

    def test_details_route(self):
        response = self.client.get("/details")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Détail".encode("utf-8"), response.data)

    def test_history_route(self):
        response = self.client.get("/history")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Historique", response.data)

    def test_about_route(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn("À propos".encode("utf-8"), response.data)

    def test_post_request_index(self):
        response = self.client.post(
            "/",
            data={
                "temperature": "20",
                "heure_sortie": "21",
                "duree_sortie": "5",
                "duree_inactivite": "1",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Température normale".encode("utf-8"), response.data)


if __name__ == "__main__":
    unittest.main()

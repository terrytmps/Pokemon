from models.Notificateur import Notificateur


class NotificateurEmail(Notificateur):
    """
    Notificateur qui envoie des notifications par email.
    """

    def notifier(self, alerte, priorite: str):
        print(
            f"Envoi d'un email pour l'alerte: {alerte.message} avec priorité: {priorite}"
        )

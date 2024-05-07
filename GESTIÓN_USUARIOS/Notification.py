from abc import ABC, abstractmethod

class INotification(ABC):
    """
    Una interfaz para notificaciones de registro.

    Métodos:
        notify_registration(user): Un método abstracto para notificar el registro de un usuario.
    """

    @abstractmethod
    def notify_registration(self, user):
        """
        Un método abstracto para notificar el registro de un usuario.

        Args:
            user (User): El objeto de usuario que ha sido registrado.

        Returns:
            None
        """
        pass

from Notification import INotification

class ScreenNotifier(INotification):
    """
    Una clase para mostrar notificaciones de registro en la pantalla.

    Hereda De:
        INotification: Una interfaz para notificaciones.

    Métodos:
        notify_registration(user): Muestra una notificación de registro en la pantalla.
    """

    def notify_registration(self, user):
        """
        Muestra una notificación de registro en la pantalla.

        Args:
            user (User): El objeto de usuario que ha sido registrado.

        Returns:
            None
        """
        if user.user_type == "ocasional":
            print("Te has registrado exitosamente. Pronto tendrás acceso a nuestro catálogo web de productos de tecnología.")
        else:
            print("Te has registrado exitosamente.")
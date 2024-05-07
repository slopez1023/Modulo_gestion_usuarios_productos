from Notification import INotification

class EmailNotifier(INotification):
    """
    Una clase para enviar notificaciones de registro por correo electrónico.

    Hereda De:
        INotification: Una interfaz para notificaciones.

    Métodos:
        notify_registration(user): Envía una notificación de registro por correo electrónico.
    """

    def notify_registration(self, user):
        """
        Envía una notificación de registro por correo electrónico.

        Args:
            user (User): El objeto de usuario que ha sido registrado.

        Returns:
            None
        """
        print(f"Enviando correo de bienvenida a {user.email}")

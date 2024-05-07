from User import User
from Notification import INotification

class UserManager:
    """
    Una clase para gestionar usuarios en el sistema.

    Atributos:
        notifier (INotification): El objeto notificador utilizado para enviar notificaciones.
        users (dict): Un diccionario para almacenar usuarios, con el correo electrónico como clave.
    """

    def __init__(self, notifier: INotification):
        """
        Inicializa el UserManager con un notificador y un diccionario vacío de usuarios.

        Args:
            notifier (INotification): El objeto notificador utilizado para enviar notificaciones.
        """
        self.notifier = notifier
        self.users = {}

    def register_user(self, user: User):
        """
        Registra un nuevo usuario en el sistema.

        Args:
            user (User): El objeto de usuario a registrar.

        Raises:
            ValueError: Si el tipo de usuario no es 'ocasional' o 'mayorista'.

        Returns:
            User: El usuario registrado.
        """
        if user.user_type not in ["ocasional", "mayorista"]:
            raise ValueError("Tipo de usuario inválido. Debe ser 'ocasional' o 'mayorista'")

        self.users[user.email] = user

        self.notifier.notify_registration(user)

        return user

    def update_user(self, email, **kwargs):
        """
        Actualiza los atributos de un usuario existente.

        Args:
            email (str): El correo electrónico del usuario a actualizar.
            **kwargs: Argumentos de palabras clave arbitrarios que representan los atributos a actualizar.

        Raises:
            ValueError: Si el usuario no se encuentra en el sistema.

        Returns:
            User: El usuario actualizado.
        """
        if email not in self.users:
            raise ValueError("Usuario no encontrado")

        user = self.users[email]
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)

        return user

    def delete_user(self, email):
        """
        Elimina un usuario del sistema.

        Args:
            email (str): El correo electrónico del usuario a eliminar.

        Raises:
            ValueError: Si el usuario no se encuentra en el sistema.

        Returns:
            None
        """
        if email not in self.users:
            raise ValueError("Usuario no encontrado")

        del self.users[email]

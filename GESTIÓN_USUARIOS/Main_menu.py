from Product import Product
from User import User
from ScreenNotifier import ScreenNotifier
from UserManager import UserManager
from ProductManager import ProductManager
from VariacionProducto import VariacionProducto
from VariacionProducto import VariacionColor
from VariacionProducto import VariacionMaterial
from VariacionProducto import VariacionTamano

def main():
    """
    Función principal que ejecuta el programa.

    Permite al usuario registrar usuarios y agregar productos con sus respectivas variaciones.
    """
    user_manager = UserManager(ScreenNotifier())
    product_manager = ProductManager()

    while True:
        print("\nMenú de opciones:")
        print("1. Registrar usuario")
        print("2. Agregar producto")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            identificacion = input("Ingrese la identificación del usuario: ")
            direccion = input("Ingrese la dirección del usuario: ")
            telefono = input("Ingrese el teléfono del usuario: ")
            email = input("Ingrese el correo electrónico del usuario: ")
            user_type = input("Ingrese el tipo de usuario (ocasional o mayorista): ")

            try:
                user = user_manager.register_user(User(nombre, identificacion, direccion, telefono, email, user_type))
                print(f"Usuario registrado exitosamente como {user.user_type}.")
            except ValueError as e:
                print(e)

        elif opcion == 2:
            # Agregar producto
            sku = input("Ingrese el SKU del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))

            product = Product(sku, nombre, descripcion, precio)
            product_manager.add_product(product)

            print("Producto agregado exitosamente.")

            while True:
                print("\nSeleccione el tipo de variación:")
                print("1. Color")
                print("2. Material")
                print("3. Tamaño")
                print("4. Volver al menú principal")

                opcion_variacion = int(input("Seleccione una opción: "))

                if opcion_variacion == 1:
                    # Agregar variación de color
                    id_variacion = input("Ingrese el ID de la variación de color: ")
                    descripcion_variacion = input("Ingrese la descripción de la variación de color: ")
                    precio_variacion = float(input("Ingrese el precio de la variación de color: "))
                    color = input("Ingrese el color de la variación: ")

                    variacion = VariacionColor(id_variacion, sku, descripcion_variacion, precio_variacion, color, product.sku)
                    product_manager.add_product(variacion)

                elif opcion_variacion == 2:
                    # Agregar variación de material
                    id_variacion = input("Ingrese el ID de la variación de material: ")
                    descripcion_variacion = input("Ingrese la descripción de la variación de material: ")
                    precio_variacion = float(input("Ingrese el precio de la variación de material: "))
                    material = input("Ingrese el material de la variación: ")

                    variacion = VariacionMaterial(id_variacion, sku, descripcion_variacion, precio_variacion, material, product.sku)
                    product_manager.add_product(variacion)

                elif opcion_variacion == 3:
                    # Agregar variación de tamaño
                    id_variacion = input("Ingrese el ID de la variación de tamaño: ")
                    descripcion_variacion = input("Ingrese la descripción de la variación de tamaño: ")
                    precio_variacion = float(input("Ingrese el precio de la variación de tamaño: "))
                    tamano = input("Ingrese el tamaño de la variación: ")

                    variacion = VariacionTamano(id_variacion, sku, descripcion_variacion, precio_variacion, tamano, product.sku)
                    product_manager.add_product(variacion)

                elif opcion_variacion == 4:
                    break

                else:
                    print("Opción inválida. Inténtelo de nuevo.")

        elif opcion == 3:
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()

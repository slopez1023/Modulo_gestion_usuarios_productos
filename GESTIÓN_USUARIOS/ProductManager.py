from Product import Product

class ProductManager:
    """
    Una clase para gestionar productos en el sistema.

    Atributos:
        products (list): Una lista para almacenar objetos de Producto.
    """

    def __init__(self):
        """
        Inicializa el ProductManager con una lista vacía de productos.
        """
        self.products = []

    def add_product(self, product: Product):
        """
        Agrega un nuevo producto a la lista de productos.

        Args:
            product (Producto): El objeto de producto a agregar.

        Returns:
            None
        """
        self.products.append(product)

    def update_product(self, sku, **kwargs):
        """
        Actualiza los atributos de un producto identificado por su SKU.

        Args:
            sku (str): El SKU del producto a actualizar.
            **kwargs: Argumentos de palabras clave arbitrarios que representan los atributos
                a actualizar.

        Raises:
            ValueError: Si no se encuentra el producto con el SKU dado.

        Returns:
            None
        """
        product = next((p for p in self.products if p.sku == sku), None)
        if product is None:
            raise ValueError("Producto no encontrado")

        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)

    def delete_product(self, sku):
        """
        Elimina un producto de la lista de productos basado en su SKU.

        Args:
            sku (str): El SKU del producto a eliminar.

        Raises:
            ValueError: Si no se encuentra el producto con el SKU dado.

        Returns:
            None
        """
        product = next((p for p in self.products if p.sku == sku), None)
        if product is None:
            raise ValueError("Producto no encontrado")

        self.products.remove(product)
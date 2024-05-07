class VariacionProducto:
    """
    Una clase base para representar variaciones de productos.

    Métodos:
        __init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, id_producto_padre):
            Inicializa una variación de producto con los atributos especificados.
    """

    def __init__(self, id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, id_producto_padre):
        """
        Inicializa una variación de producto con los atributos especificados.

        Args:
            id_variacion_producto (int): El ID de la variación del producto.
            sku_variacion (str): El SKU de la variación del producto.
            descripcion_variacion (str): La descripción de la variación del producto.
            precio_variacion (float): El precio de la variación del producto.
            id_producto_padre (int): El ID del producto padre al que pertenece la variación.
        """
        self.id_variacion_producto = id_variacion_producto
        self.sku_variacion = sku_variacion
        self.descripcion_variacion = descripcion_variacion
        self.precio_variacion = precio_variacion
        self.id_producto_padre = id_producto_padre


class VariacionColor(VariacionProducto):
    """
    Una clase para representar variaciones de color de productos.

    Métodos:
        __init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, color, id_producto_padre):
            Inicializa una variación de color con los atributos especificados.
    """

    def __init__(self, id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, color, id_producto_padre):
        """
        Inicializa una variación de color con los atributos especificados.

        Args:
            id_variacion_producto (int): El ID de la variación del producto.
            sku_variacion (str): El SKU de la variación del producto.
            descripcion_variacion (str): La descripción de la variación del producto.
            precio_variacion (float): El precio de la variación del producto.
            color (str): El color de la variación del producto.
            id_producto_padre (int): El ID del producto padre al que pertenece la variación.
        """
        super().__init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, id_producto_padre)
        self.color_variacion = color


class VariacionMaterial(VariacionProducto):
    """
    Una clase para representar variaciones de material de productos.

    Métodos:
        __init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, material, id_producto_padre):
            Inicializa una variación de material con los atributos especificados.
    """

    def __init__(self, id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, material, id_producto_padre):
        """
        Inicializa una variación de material con los atributos especificados.

        Args:
            id_variacion_producto (int): El ID de la variación del producto.
            sku_variacion (str): El SKU de la variación del producto.
            descripcion_variacion (str): La descripción de la variación del producto.
            precio_variacion (float): El precio de la variación del producto.
            material (str): El material de la variación del producto.
            id_producto_padre (int): El ID del producto padre al que pertenece la variación.
        """
        super().__init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, id_producto_padre)
        self.material_variacion = material


class VariacionTamano(VariacionProducto):
    """
    Una clase para representar variaciones de tamaño de productos.

    Métodos:
        __init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, tamano, id_producto_padre):
            Inicializa una variación de tamaño con los atributos especificados.
    """

    def __init__(self, id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, tamano, id_producto_padre):
        """
        Inicializa una variación de tamaño con los atributos especificados.

        Args:
            id_variacion_producto (int): El ID de la variación del producto.
            sku_variacion (str): El SKU de la variación del producto.
            descripcion_variacion (str): La descripción de la variación del producto.
            precio_variacion (float): El precio de la variación del producto.
            tamano (str): El tamaño de la variación del producto.
            id_producto_padre (int): El ID del producto padre al que pertenece la variación.
        """
        super().__init__(id_variacion_producto, sku_variacion, descripcion_variacion, precio_variacion, id_producto_padre)
        self.tamano_variacion = tamano

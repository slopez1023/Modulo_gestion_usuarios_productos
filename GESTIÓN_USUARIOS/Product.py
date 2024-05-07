class Product:
    def __init__(self, sku, name, description, price, material=None, color=None, category=None, stock=0, images=None):
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.material = material
        self.color = color
        self.category = category
        self.stock = stock
        self.images = images

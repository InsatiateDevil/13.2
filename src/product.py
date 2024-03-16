class Product:
    name: str
    description: str
    price: int or float
    stock: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Продукт - {self.name}, описание - {self.description}, "
                f"цена - {self.price}, количество в наличие - {self.quantity}")

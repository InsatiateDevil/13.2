class Product:
    name: str
    description: str
    price: float
    stock: int

    products_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        self.products_list.append(self)

    @classmethod
    def init_new_product(cls, dict_with_prod, category):
        name = dict_with_prod['name']
        description = dict_with_prod['description']
        price = dict_with_prod['price']
        quantity = dict_with_prod['quantity']
        for product in Product.products_list:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return None
        category.add_product(cls(name, description, price, quantity))

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Новая цена не соответствует условиям')
        elif value < self.__price:
            confirm = input("Новая цена ниже текущей. Для подтверждения "
                            "введите 'y'")
            if confirm == 'y':
                self.__price = value
        else:
            self.__price = value

    def __repr__(self):
        return (f"Продукт - {self.name}, описание - {self.description}, "
                f"цена - {self.price}, количество в наличие - {self.quantity}|")

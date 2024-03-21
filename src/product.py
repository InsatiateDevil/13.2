class Product:
    """
    Класс продуктов
    внутри непосредственно класса только список продуктов - общий,
    то есть при инициализации каждого нового экземпляра класса ссылка на него
    будет ложиться так же и в этот список
    """
    products_list: list
    products_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.products_list.append(self)

    @classmethod
    def init_new_product(cls, dict_with_prod):
        """
        Класс метод для распаковки одного товара из словаря с данными о товаре.
        Если товар ранее с таким названием ранее находился в системе,
        то увеличивает его количество,
        иначе отправляет на добавление в указанную категорию
        :param dict_with_prod: словарь с данными о товаре
        :return: None
        """
        name = dict_with_prod['name']
        description = dict_with_prod['description']
        price = dict_with_prod['price']
        quantity = dict_with_prod['quantity']
        for product in Product.products_list:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """
        геттер для цены товара
        :return: цену товара
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для цены товара. Если введенная цена меньше нуля - дает фидбэк
        и цену не увеличивает. Если новая цена товара оказалась выше той, что
        у товара уже есть - запрашивает подтверждение на изменение
        в меньшую сторону(при подтверждение изменяет цену на новую)
        :param new_price: новая цена
        :return: None
        """
        if new_price <= 0:
            print('Новая цена не соответствует условиям')
        elif new_price < self.__price:
            confirm = input("Новая цена ниже текущей. Для подтверждения "
                            "введите 'y'")
            if confirm == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

    def __repr__(self):
        return (f"Продукт - {self.name}, описание - {self.description}, "
                f"цена - {self.price}, количество в наличие - {self.quantity}|")

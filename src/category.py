from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(products)

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products(self):
        list_of_products = []
        for product in self.__products:
            list_of_products.append(f"{product.name}, {product.price} руб. "
                                    f"Остаток: {product.quantity} шт.")
        return list_of_products

    def __repr__(self):
        return (f"Категория - {self.name}, описание - {self.description},"
                f" продукты - {self.__products}|")

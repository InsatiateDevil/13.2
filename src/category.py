from src.product import Product


class Category:
    """
    Класс категорий
    Непосредственно в классе находятся два счетчика - один считает количество
    категорий и увеличивается только при инициализации нового экземпляра
    класса, второй считает товары - увеличивается на длину списка отдаваемого
    при инициализации класса и в отдельном методе на добавление товара в категорию
    """
    category_count: int
    products_count: int

    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Конструктор класса Category
        :param name: имя категории
        :param description: описание категории
        :param products: содержит список
        экземпляров класса продукт(иначе говоря продукты)
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(products)

    def add_product(self, new_product: Product):
        """
        метод отвечающий за добавление нового продукта в текущую категорию
        и увеличивающий счетчик видов товара
        :param new_product: экземпляр класса продукты
        :return: None
        """
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products(self):
        """
        геттер для возврата списка описаний продуктов текущей категории
        :return: список с описанием продуктов
        """
        list_of_products = []
        for product in self.__products:
            list_of_products.append(f"{product.name}, {product.price} руб. "
                                    f"Остаток: {product.quantity} шт.")
        return list_of_products

    def __repr__(self):
        return (f"Категория - {self.name}, описание - {self.description},"
                f" продукты - {self.__products}|")

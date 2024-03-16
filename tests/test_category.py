import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def coll():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и "
                    "получение дополнительных функций для удобства жизни",
                    [Product("Samsung Galaxy C23 Ultra",
                             "256GB, Серый цвет, 200MP камера",
                             180000.0, 5),
                     Product(
                         "Iphone 15", "512GB, Gray space",
                         210000.0, 8),
                     Product("Xiaomi Redmi Note 11",
                             "1024GB, Синий",
                             31000.0, 14)])


def test_init(coll):
    assert coll.name == "Смартфоны"
    assert coll.description == ("Смартфоны, как средство не только "
                                "коммуникации, но и "
                                "получение дополнительных функций для "
                                "удобства жизни")
    assert coll.products[0].name == "Samsung Galaxy C23 Ultra"
    assert Category.category_count == 1
    assert Category.products == 3

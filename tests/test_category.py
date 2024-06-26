import pytest
from src.category import Category


def test_init(null, for_category):
    with pytest.raises(TypeError):
        Category('лол', 'дважды лол', ['какой-то', 'список'])
    assert for_category.name == "Смартфоны"
    assert for_category.description == ("Смартфоны, как средство не только "
                                        "коммуникации, но и "
                                        "получение дополнительных функций для "
                                        "удобства жизни")
    assert for_category.products[0].startswith(
        "Samsung Galaxy C23 Ultra") is True
    assert Category.category_count == 1
    assert Category.products_count == 2


def test_add_product(null, for_category, for_product_1):
    for_category.add_product(for_product_1)
    assert Category.products_count == 3
    assert for_category.products[2].startswith("Xiaomi Redmi Note 11") is True
    with pytest.raises(TypeError):
        for_category.add_product('лол')


def test_product_getter(for_category):
    products = ['Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                'Iphone 15, 210000.0 руб. Остаток: 8 шт.']
    assert for_category.products == products


def test_repr(for_category):
    print_repr = (
        'Category(Смартфоны, Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни, '
        '[Product(Samsung Galaxy C23 Ultra, '
        '256GB, Серый цвет, 200MP камера, 5), '
        'Product(Iphone 15, 512GB, Gray space, 8)])')
    assert repr(for_category) == print_repr


def test_str(for_category):
    print_str = "Смартфоны, количество продуктов: 13 шт."
    assert str(for_category) == print_str

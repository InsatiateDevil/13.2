import pytest
import os
from config import ROOT_DIR
from src.product import Product
from src.category import Category


@pytest.fixture
def for_load_json():
    return os.path.join(ROOT_DIR, 'src', 'products.json')


@pytest.fixture
def for_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и "
                    "получение дополнительных функций для удобства жизни",
                    [Product("Samsung Galaxy C23 Ultra",
                             "256GB, Серый цвет, 200MP камера",
                             180000.0, 5),
                     Product("Iphone 15", "512GB, Gray space",
                             210000.0, 8)])


@pytest.fixture
def for_product():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0, 14)


@pytest.fixture
def dict_with_product():
    return {'name': "Xiaomi Redmi Note 11",
            'description': "1024GB, Синий",
            'price': 31000.0,
            'quantity': 14}


@pytest.fixture
def null():
    Category.category_count = 0
    Category.products_count = 0
    Product.products_list = []

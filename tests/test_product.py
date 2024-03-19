import pytest
from src.category import Category
from src.product import Product


def test_init(for_product):
    for_test = for_product.products[0]
    assert for_test.name == "Xiaomi Redmi Note 11"
    assert for_test.description == "1024GB, Синий"
    assert for_test.price == 31000.0
    assert for_test.quantity == 14


def test_init_new_product(dict_with_product, for_category):
    assert len(for_category.products) == 2
    assert len(Product.products_list) == 2
    Product.init_new_product(dict_with_product, for_category)
    assert Product.products_list[2].quantity == 14
    assert len(for_category.products) == 3
    Product.init_new_product(dict_with_product, for_category)
    assert len(for_category.products) == 3
    assert Product.products_list[2].quantity == 28

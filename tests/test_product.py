import pytest
from src.category import Category
from src.product import Product


def test_init(for_product):
    assert for_product.name == "Xiaomi Redmi Note 11"
    assert for_product.description == "1024GB, Синий"
    assert for_product.price == 31000.0
    assert for_product.quantity == 14


def test_init_new_product(null, dict_with_product, for_category):
    assert len(for_category.products) == 2
    assert len(Product.products_list) == 2
    Product.init_new_product(dict_with_product, for_category)
    assert Product.products_list[2].quantity == 14
    assert len(for_category.products) == 3
    Product.init_new_product(dict_with_product, for_category)
    assert len(for_category.products) == 3
    assert Product.products_list[2].quantity == 28


def test_price_getter(for_product):
    assert for_product.price == 31000.0


def test_price_setter(for_product):
    for_product.price = 30000.0  # При вводе 'n'
    assert for_product.price == 31000.0
    for_product.price = 30000.0  # При вводе 'y'
    assert for_product.price == 30000.0

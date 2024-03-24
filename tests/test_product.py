import pytest
from src.category import Category
from src.product import Product


def test_init(for_product):
    assert for_product.name == "Xiaomi Redmi Note 11"
    assert for_product.description == "1024GB, Синий"
    assert for_product.price == 31000.0
    assert for_product.quantity == 14


def test_init_new_product(null, dict_with_product):
    assert len(Product.products_list) == 0
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 14
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 28
    dict_with_product['price'] = 35000.0
    Product.init_new_product(dict_with_product)
    assert Product.products_list[0].quantity == 42


def test_price_getter(for_product):
    assert for_product.price == 31000.0


def test_price_setter(for_product):
    for_product.price = 30000.0  # При вводе 'n'
    assert for_product.price == 31000.0
    for_product.price = 30000.0  # При вводе 'y'
    assert for_product.price == 30000.0
    for_product.price = 0.0
    assert for_product.price == 30000.0
    for_product.price = 32000.0
    assert for_product.price == 32000.0


def test_add(null, for_category):
    assert Product.products_list[0] + Product.products_list[1] == 2580000.0


def test_len(for_product):
    assert len(for_product) == 14


def test_str(for_product):
    str_product = "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(for_product) == str_product


def test_repr(for_product):
    repr_product = "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 14)"
    assert repr(for_product) == repr_product

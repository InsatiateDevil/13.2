import pytest
from src.category import Category
from src.product import Product


def test_init(coll):
    coll_for_test = coll.products[0]
    assert coll_for_test.name == "Samsung Galaxy C23 Ultra"
    assert coll_for_test.description == "256GB, Серый цвет, 200MP камера"
    assert coll_for_test.price == 180000.0
    assert coll_for_test.quantity == 5

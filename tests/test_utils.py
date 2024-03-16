import pytest
import os
from config import ROOT_DIR
from src.utils import load_json, unpacker


@pytest.fixture
def coll():
    PATH_TO_PRODUCTS = os.path.join(ROOT_DIR, 'src', 'products.json')
    return load_json(PATH_TO_PRODUCTS)


def test_load_json(coll):
    assert coll[1:] == [{
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться "
                       "просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }]


def test_unpacker(coll):
    assert unpacker(coll)[0][0].name == "Смартфоны"

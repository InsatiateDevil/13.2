from src.category import Category


def test_init(coll):
    assert coll.name == "Смартфоны"
    assert coll.description == ("Смартфоны, как средство не только "
                                "коммуникации, но и "
                                "получение дополнительных функций для "
                                "удобства жизни")
    assert coll.products[0].name == "Samsung Galaxy C23 Ultra"
    assert Category.category_count == 1
    assert Category.products == 3

from src.product_iterator import ProductIterator


def test_init(for_iterator):
    assert str(for_iterator.category) == ("Название категории,"
                                          " количество продуктов: 13 шт.")


def test_iter_and_next(for_iterator):
    for i in for_iterator:
        pass
    assert for_iterator.iter_index == 0


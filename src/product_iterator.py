
class ProductIterator:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.iter_index = len(self.category)
        return self

    def __next__(self):
        if self.iter_index == 0:
            raise StopIteration
        self.iter_index -= 1
        return self.category.products[self.iter_index]

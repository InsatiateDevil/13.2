from src.category import Category
from src.product import Product
from src.utils import load_json, unpacker
import os
from config import ROOT_DIR

PATH_TO_PRODUCTS = os.path.join(ROOT_DIR, 'src', 'products.json')


def main():
    category_list = []
    products_list = []
    for categ in load_json(PATH_TO_PRODUCTS):
        prod_from_cat = []
        for prod in categ.get('products'):
            product = Product(prod['name'], prod['description'],
                              prod['price'], prod['quantity'])
            prod_from_cat.append(product)
        category = Category(categ['name'], categ['description'], prod_from_cat)
        category_list.append(category)
        products_list.append(prod_from_cat)
    print(category_list)
    print(products_list)
    print()
    for i in category_list:
        print(i.products)
    Product.init_new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }, category_list[0])
    print(category_list[0].products)
    print(Category.products_count)
    for i in Product.products_list:
        print(i)


if __name__ == '__main__':
    main()

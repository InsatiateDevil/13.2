from utils import load_json, unpacker
import os
from config import ROOT_DIR

PATH_TO_PRODUCTS = os.path.join(ROOT_DIR, 'src', 'products.json')


def main():
    list_with_info = load_json(PATH_TO_PRODUCTS)
    category_list, products_list = unpacker(list_with_info)
    print(category_list)
    print(products_list)


if __name__ == '__main__':
    main()

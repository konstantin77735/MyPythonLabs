from typing import List
from datetime import datetime

class UtilizeList(OnlineStore):
    def __init__(self, name, utilize_list=None):
        super().__init__(name)
        self.utilize_list = utilize_list or []

    def add_products(self, product):
        self.utilize_list.append(product)

    def get_products_array(self, order):
        sorted_list = sorted(self.utilize_list, key=lambda x: getattr(x, order.lower()))
        return sorted_list

    def loop_through_products(self, products):
        for i, product in enumerate(products, 1):
            product.print_details(i)

    def print_utilize_list(self, order):
        products_list = self.get_products_array(order)
        self.loop_through_products(products_list)

    def size(self):
        return len(self.utilize_list)

    def get_store_name(self):
        return self.store_name

    def set_store_name(self, new_store_name):
        self.store_name = new_store_name

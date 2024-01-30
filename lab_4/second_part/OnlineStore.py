from datetime import datetime
from product_list import ProductList  # Assuming there is a ProductList class
from sales_list import SalesList  # Assuming there is a SalesList class
from utilize_list import UtilizeList  # Assuming there is a UtilizeList class

class OnlineStore:
    def __init__(self, name, owner, inn, domen, sales_list_of_store=None,
                 products_list_of_store=None, utilizable_products_list_of_store=None):
        self.name = name
        self.owner = owner
        self.inn = inn
        self.domen = domen
        self.products_list_of_store = products_list_of_store
        self.sales_list_of_store = sales_list_of_store
        self.utilizable_products_list_of_store = utilizable_products_list_of_store

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_inn(self):
        return self.inn

    def set_inn(self, new_inn):
        self.inn = new_inn

    def get_domen(self):
        return self.domen

    def set_domen(self, new_domen):
        self.domen = new_domen

    def get_products_list_of_store(self):
        return self.products_list_of_store

    def set_products_list_of_store(self, new_list):
        self.products_list_of_store = new_list

    def get_sales_list_of_store(self):
        return self.sales_list_of_store

    def set_sales_list_of_store(self, new_list):
        self.sales_list_of_store = new_list

    def print_sales(self, order):
        if self.sales_list_of_store is not None and len(self.sales_list_of_store) != 0:
            print("Список продаж (проданных товаров):\n")
            self.sales_list_of_store.print_products_list(order)
        else:
            print("Список продаж (уже проданных товаров) пуст.\n_____")

    def print_customers(self, order):
        if self.sales_list_of_store is not None and len(self.sales_list_of_store) != 0:
            print("Список покупателей:\n")
            self.sales_list_of_store.print_customers_list(order)
        else:
            print("Список покупателей пуст.\n_____")

    def print_countries(self, order):
        if self.sales_list_of_store is not None and len(self.sales_list_of_store) != 0:
            print("Список стран-производителей:\n")
            self.sales_list_of_store.print_countries_list(order)
        else:
            print("Список стран-производителей пуст.\n_____")

    def print_products(self, order):
        if self.products_list_of_store is not None and len(self.products_list_of_store) != 0:
            print("Список товаров:\n")
            self.products_list_of_store.print_products_list(order)
        else:
            print("Список товаров пуст.\n")

    def get_utilizable_products_list_of_store(self):
        return self.utilizable_products_list_of_store

    def set_utilizable_products_list_of_store(self, new_list):
        self.utilizable_products_list_of_store = new_list

    def print_utilizable_products(self, order):
        if self.utilizable_products_list_of_store is not None and len(self.utilizable_products_list_of_store) != 0:
            print("Список товаров:\n")
            self.utilizable_products_list_of_store.print_utilize_list(order)
        else:
            print("Список товаров пуст.\n")

    def print_full_info(self):
        print(f"Интернет-магазин: {self.get_name()}")
        print(f"Владелец: {self.get_owner()}")
        print(f"Инн: {self.get_inn()}")
        print(f"Домен: {self.get_domen()}")
        print("_______________")

        if self.sales_list_of_store is not None and len(self.sales_list_of_store) != 0:
            print("Список продаж (проданных товаров):\n")
            self.sales_list_of_store.print_products_list("По дате прибытия:")
        else:
            print("Список продаж (уже проданных товаров) пуст.\n_____")

        if self.products_list_of_store is not None and len(self.products_list_of_store) != 0:
            print("Список товаров:\n")
            self.products_list_of_store.print_products_list("По дате прибытия:")
        else:
            print("Список товаров пуст.\n")

from Products import Product  # Assuming there is a Product class

class ProductList(OnlineStore):
    def __init__(self, name, store_name=None, product_list=None):
        super().__init__(name)
        self.store_name = store_name
        self.product_list = product_list if product_list is not None else []

    def add_products(self, product):
        self.product_list.append(product)

    def get_products_array(self, order):
        sorted_list = self.product_list.copy()

        if order == "По дате прибытия":
            sorted_list.sort(key=lambda product: product.get_arrival_date())
        elif order == "По названию":
            sorted_list.sort(key=lambda product: product.get_name())
        # Добавьте другие варианты сортировки, если необходимо

        return sorted_list

    def loop_through_products(self, products):
        for i, product in enumerate(products, start=1):
            product.print_details(i)

    def print_products_list(self, order):
        sorted_products = self.get_products_array(order)
        self.loop_through_products(sorted_products)

    def size(self):
        return len(self.product_list)

    def get_store_name(self):
        return self.store_name

    def set_store_name(self, new_store_name):
        self.store_name = new_store_name

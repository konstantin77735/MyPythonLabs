from typing import List

class SalesList(OnlineStore):
    def __init__(self, name: str):
        super().__init__(name)
        self.sales_list = []

    def add_sales(self, sale: Sales):
        self.sales_list.append(sale)

    def get_sales_array(self, order: str) -> List[Sales]:
        sorted_list = sorted(self.sales_list, key=lambda x: getattr(x, order.lower()))

        return sorted_list

    def loop_through_products(self, sales: List[Sales], list_type: str):
        max_price = float('-inf')
        min_price = float('inf')
        buyer_with_max_price = None
        buyer_with_min_price = None

        for i, sale in enumerate(sales, start=1):
            if list_type == "Список покупателей":
                price = sale.get_retail_price()

                if price > max_price:
                    max_price = price
                    buyer_with_max_price = sale.get_customer_name()

                if price < min_price:
                    min_price = price
                    buyer_with_min_price = sale.get_customer_name()

                sale.print_customers()

            elif list_type == "Список стран-производителей":
                sale.print_countries()

            elif list_type == "Список продаж":
                sale.print_details(i)

        if buyer_with_max_price:
            print(f"Покупатель с самой большой ценой покупки: {buyer_with_max_price}")

        if buyer_with_min_price:
            print(f"Покупатель с самой низкой ценой покупки: {buyer_with_min_price}")

    def print_products_list(self, order: str):
        sales_list = self.get_sales_array(order)
        self.loop_through_products(sales_list, "Список продаж")

    def print_customers_list(self, order: str):
        customers_list = self.get_sales_array(order)
        self.loop_through_products(customers_list, "Список покупателей")

    def print_countries_list(self, order: str):
        countries_list = self.get_sales_array(order)
        self.loop_through_products(countries_list, "Список стран-производителей")

    def size(self):
        return len(self.sales_list)

    def get_store_name(self):
        return self.store_name

    def set_store_name(self, new_store_name):
        self.store_name = new_store_name

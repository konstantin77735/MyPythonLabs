from datetime import datetime

class Sales(Product):
    def __init__(self, name, country_of_origin, purchase_price, retail_price, discount, payment_type, purchase_amount,
                 arrival_date_string, sale_date_string, quantity, customer_name, purpose,
                 length, height, width):
        super().__init__(name, country_of_origin, purchase_price, retail_price, arrival_date_string, purpose)
        self.discount = discount
        self.payment_type = payment_type
        self.purchase_amount = purchase_amount
        self.sale_date = datetime.strptime(sale_date_string, "%d.%m.%Y").date()
        self.quantity = quantity
        self.customer_name = customer_name

        self.length = self.set_dimension(length)
        self.height = self.set_dimension(height)
        self.width = self.set_dimension(width)

    def set_dimension(self, dimension):
        if dimension < 0:
            raise ValueError("Отрицательное значение размера недопустимо")
        return dimension

    def get_payment_type(self):
        return self.payment_type

    def set_payment_type(self, payment_type):
        self.payment_type = payment_type

    def get_purchase_amount(self):
        return self.purchase_amount

    def set_purchase_amount(self, purchase_amount):
        self.purchase_amount = purchase_amount

    def get_sale_date(self):
        return self.sale_date

    def set_sale_date(self, sale_date_string):
        self.sale_date = datetime.strptime(sale_date_string, "%d.%m.%Y").date()

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, new_customer_name):
        self.customer_name = new_customer_name

    def print_details(self, product_number):
        print(f"{product_number} продажа. Детали о товаре:")
        print(f"Название товара: {self.get_name()}; Страна (производитель): {self.get_country_of_origin()}; "
              f"Категория товара: {self.get_purpose()};")
        print(f"Дата поступления: {self.get_arrival_date()}; Дата продажи: {self.get_sale_date()}; "
              f"Количество проданных: {self.get_quantity()};")

        print(f"{product_number} продажа. Детали об оплате:")
        print(f"Цена: {self.get_retail_price()} р; Скидка: {self.get_discount()}%; "
              f"В итоге оплачено: {self.get_discounted_price(self.discount)} р; "
              f"Способ оплаты: {self.get_payment_type()};")
        print(f"Покупатель: {self.get_customer_name()};")
        print("_____")

    def print_customers(self):
        print(f"Покупатель: {self.get_customer_name()};")
        print(f"Купил: {self.get_quantity()} шт. товара: {self.get_name()};")
        print(f"Общей стоимостью: {self.get_retail_price()} р;")
        print("_____")

    def print_countries(self):
        print(f"Товар: {self.get_name()};")
        print(f"Страна-производитель: {self.get_country_of_origin()};")
        print(f"Количество товара: {self.get_quantity()};")
        print("_____")

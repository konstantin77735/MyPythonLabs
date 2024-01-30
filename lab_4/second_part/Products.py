from datetime import datetime

class TooLowPriceException(Exception):
    def __init__(self, purchase_price, retail_price):
        self.purchase_price = purchase_price
        self.retail_price = retail_price

class Product(Discountable):
    def __init__(self, name, country_of_origin, purchase_price, retail_price, arrival_date_string, length, height, width):
        self.name = name
        self.country_of_origin = country_of_origin
        self.purchase_price = None  # Will be set in the setter method
        self.retail_price = None  # Will be set in the setter method
        self.arrival_date = datetime.strptime(arrival_date_string, "%d.%m.%Y").date()
        self.discount = 0
        self.length = None  # Will be set in the setter method
        self.height = None  # Will be set in the setter method
        self.width = None  # Will be set in the setter method

        self.set_length(length)
        self.set_height(height)
        self.set_width(width)

        self.set_retail_price(retail_price)
        self.set_purchase_price(purchase_price)

    def set_retail_price(self, retail_price):
        try:
            if retail_price < 0:
                raise ValueError("Розничная цена не может быть отрицательной.")
            if retail_price < self.purchase_price:
                raise TooLowPriceException(self.purchase_price, retail_price)
            self.retail_price = retail_price
        except TooLowPriceException as e:
            print("Ошибка: розничная цена ниже закупочной.")
            print("Закупочная цена:", e.purchase_price)
            print("Розничная цена:", e.retail_price)
            exit(1)

    def set_purchase_price(self, purchase_price):
        if purchase_price < 0:
            raise ValueError("Закупочная цена не может быть отрицательной.")
        self.purchase_price = purchase_price

    def set_length(self, length):
        if length < 0:
            raise ValueError("Отрицательное значение длины недопустимо")
        self.length = length

    def set_height(self, height):
        if height < 0:
            raise ValueError("Отрицательное значение высоты недопустимо")
        self.height = height

    def set_width(self, width):
        if width < 0:
            raise ValueError("Отрицательное значение ширины недопустимо")
        self.width = width

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_country_of_origin(self):
        return self.country_of_origin

    def set_country_of_origin(self, country_of_origin):
        self.country_of_origin = country_of_origin

    def get_retail_price(self):
        return self.retail_price

    def get_purchase_price(self):
        return self.purchase_price

    def get_arrival_date(self):
        return self.arrival_date

    def set_arrival_date(self, arrival_date_string):
        self.arrival_date = datetime.strptime(arrival_date_string, "%d.%m.%Y").date()

    def get_purpose(self):
        return self.purpose

    def set_purpose(self, purpose):
        self.purpose = purpose

    def print_details(self, product_number):
        print(f"{product_number} продажа. Детали о товаре:")
        print(f"Название товара: {self.get_name()}; Страна (производитель): {self.get_country_of_origin()};"
              f" Категория товара: {self.get_purpose()};")
        print(f"Длина: {self.get_length()} см; Высота: {self.get_height()} см; Ширина: {self.get_width()} см;")
        print(f"Дата поступления: {self.get_arrival_date()}; Цена: {self.get_retail_price()} р;")
        print(f"Скидка: {self.get_discount()}%; В итоге оплачено: {self.get_discounted_price(self.discount)} р;")

    def ask_discount(self):
        discount = int(input(f"Введите размер скидки (в процентах) для товара: {self.get_name()}, Категория: {self.get_purpose()}\n"
                             "Размер скидки не более 30%: "))
        self.set_discount(discount)
        print("_________")

    def get_discount(self):
        return self.discount

    def set_discount(self, new_discount):
        self.discount = new_discount

    def remove_discount(self):
        self.discount = 0

    def get_discounted_price(self, discount):
        return self.purchase_price - (self.purchase_price / 100 * discount)

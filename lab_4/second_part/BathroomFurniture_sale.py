from datetime import datetime, timedelta
import random

class BathroomFurnitureSale(Sales, Recyclable):
    def __init__(self, name, country_of_origin, purchase_price, retail_price, discount,
                 payment_type, purchase_amount, arrival_date_string, sale_date_string,
                 quantity, customer_name, purpose, length=None, height=None, width=None,
                 utilized=False):
        super().__init__(name, country_of_origin, purchase_price, retail_price, discount,
                         payment_type, purchase_amount, arrival_date_string, sale_date_string,
                         quantity, customer_name, purpose)
        self.payment_type = payment_type
        self.purchase_amount = purchase_amount
        self.sale_date = datetime.strptime(sale_date_string, "%d.%m.%Y").date()
        self.quantity = quantity
        self.customer_name = customer_name

        self.set_length(length)
        self.set_height(height)
        self.set_width(width)

        self.set_retail_price(retail_price)
        self.set_purchase_price(purchase_price)
        self.utilize(utilized)

    def set_length(self, length):
        if length is not None and length < 0:
            raise ValueError("Отрицательное значение длины недопустимо")
        self.length = length

    def set_height(self, height):
        if height is not None and height < 0:
            raise ValueError("Отрицательное значение высоты недопустимо")
        self.height = height

    def set_width(self, width):
        if width is not None and width < 0:
            raise ValueError("Отрицательное значение ширины недопустимо")
        self.width = width

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
        print(f"Высота: {self.get_height()} см; Ширина: {self.get_width()} см; Длина: {self.get_length()} см;")
        print(f"Дата поступления: {self.get_arrival_date().strftime('%d.%m.%Y')}; "
              f"Дата продажи: {self.get_sale_date().strftime('%d.%m.%Y')}; Количество проданных: {self.get_quantity()};")

        print(f"{product_number} продажа. Детали об оплате:")
        print(f"Розничная цена: {self.get_retail_price()} р; Скидка: {self.get_discount()}%; "
              f"В итоге оплачено: {self.get_discounted_price(self.discount)} р; Способ оплаты: {self.get_payment_type()};")
        print(f"Покупатель: {self.get_customer_name()};")
        print("_____")

    def ask_discount(self):
        discount = int(input(f"Введите размер скидки (в процентах) для товара: {self.get_name()}, Категория: {self.get_purpose()}\n"
                             "Размер скидки не более 15%: "))
        self.set_discount(discount)
        print("_________")

    def set_discount(self, discount):
        if discount <= 15:
            self.discount = discount
            print(f"Размер скидки установлен на {discount}%")
        else:
            random_discount = random.randint(0, 15)
            print(f"Нельзя установить скидку больше 15%.\n"
                  f"Будет установлена скидка, сгенерированная случайным образом, равная: {random_discount}%")
            self.discount = random_discount

    def remove_discount(self):
        self.discount = 0
        print("Скидка удалена")

    def get_recycled_price(self):
        return self.get_retail_price() * (0.7 + random.random() * 0.2)

    def get_new_price_info(self):
        recycled_price = self.get_recycled_price()
        expiration_date = datetime.now() + timedelta(days=30)
        return f"Цена товара после утилизации: {recycled_price:.2f} руб., действительна до {expiration_date.strftime('%c')}"

    def utilize(self, utilized):
        try:
            if utilized:
                raise DuplicateUtilizationException(self)
        except DuplicateUtilizationException as e:
            print(f"Ошибка: товар: {self.get_name()} уже утилизирован")
            self.utilized = True

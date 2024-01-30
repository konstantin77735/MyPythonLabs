from datetime import datetime
import random
from sales import Sales  # Assuming there is a Sales class

class LivingRoomFurnitureSale(Sales):
    def __init__(self, name, country_of_origin, purchase_price, retail_price,
                 discount, payment_type, purchase_amount, arrival_date_string,
                 sale_date_string, quantity, customer_name, purpose,
                 furniture_type, length, height, width, utilized):
        super().__init__(name, country_of_origin, purchase_price, retail_price,
                         discount, payment_type, purchase_amount, arrival_date_string,
                         sale_date_string, quantity, customer_name, purpose)
        self.furniture_type = furniture_type

        self.set_length(length)
        self.set_height(height)
        self.set_width(width)

        self.set_retail_price(retail_price)
        self.set_purchase_price(purchase_price)

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

    def get_furniture_type(self):
        return self.furniture_type

    def set_furniture_type(self, furniture_type):
        self.furniture_type = furniture_type

    def print_details(self, product_number):
        print(f"{product_number} продажа. Детали о товаре:")
        print(f"Название товара: {self.get_name()}; Страна (производитель): {self.get_country_of_origin()};"
              f" Категория товара: {self.get_purpose()};")
        print(f"Тип мебели: {self.get_furniture_type()};")
        print(f"Высота: {self.get_height()}см; Ширина: {self.get_width()}см; Длина: {self.get_length()}см;")
        print(f"Дата поступления: {self.get_arrival_date()}; Дата продажи: {self.get_sale_date()};"
              f" Количество проданных: {self.get_quantity()};")

        print(f"{product_number} продажа. Детали об оплате:")
        print(f"Цена: {self.get_retail_price()}р; Скидка: {self.get_discount()}%;"
              f" В итоге оплачено: {self.get_discounted_price(self.discount)}р; Способ оплаты: {self.get_payment_type()};")
        print(f"Покупатель: {self.get_customer_name()};")
        print("_____")

    def ask_discount(self):
        discount = int(input(f"Введите размер скидки (в процентах) для товара: {self.get_name()}, "
                             f"Категория: {self.get_purpose()}\n"
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

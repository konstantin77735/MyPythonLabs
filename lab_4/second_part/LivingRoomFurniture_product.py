from datetime import datetime
import random

class LivingRoomFurnitureProduct(Product):
    def __init__(self, name, country_of_origin, purchase_price, retail_price, arrival_date_string,
                 material, purpose, length, height, width):
        super().__init__(name, country_of_origin, purchase_price, retail_price, arrival_date_string)
        self.material = material
        self.purpose = purpose

        self.set_length(length)  # Используем сеттер для проверки значения
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

    def get_material(self):
        return self.material

    def set_material(self, material):
        self.material = material

    def print_details(self, product_number):
        print(f"Товар #{product_number};")
        print(f"Наименование: {self.get_name()};")
        print(f"Розничная цена: {self.get_retail_price()}р;")
        print(f"Страна производства: {self.get_country_of_origin()};")
        print(f"Дата поступления: {self.get_arrival_date().strftime('%dd.%mm.%Y')};")
        print(f"Материал: {self.get_material()};")
        print(f"Категория: {self.get_purpose()};")
        print(f"Скидка: {self.get_discount()}%:")
        print(f"Стоимость со скидкой: {self.get_discounted_price(self.get_discount())}р;")
        print("_____")

    def ask_discount(self):
        discount = int(input(f"Введите размер скидки (в процентах) для товара: {self.get_name()}, Категория: {self.get_purpose()}\n"
                             "Размер скидки не более 20%: "))
        if discount > 20:
            print("Скидка не может быть больше 20%!")
            discount = 20
        self.set_discount(discount)
        print("_________")

    def set_discount(self, discount):
        if discount <= 20:
            self.discount = discount
            print(f"Размер скидки установлен на {discount}%")
        else:
            random_discount = random.randint(0, 20)
            print(f"Нельзя установить скидку больше 20%.\n"
                  f"Будет установлена скидка, сгенерированная случайным образом, равная: {random_discount}%")
            self.discount = random_discount

    def remove_discount(self):
        self.discount = 0
        print("Скидка удалена")

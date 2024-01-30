from datetime import datetime, timedelta
import random

class BathroomFurnitureProduct(Product, Recyclable):
    def __init__(self, name, country_of_origin, purchase_price, retail_price,
                 arrival_date_string, material, purpose,
                 length=None, height=None, width=None, utilized=False):
        super().__init__(name, country_of_origin, purchase_price, retail_price, arrival_date_string)
        self.material = material
        self.purpose = purpose

        self.set_length(length)
        self.set_height(height)
        self.set_width(width)

        self.set_retail_price(retail_price)
        self.set_purchase_price(purchase_price)
        self.utilize(utilized)

    def get_material(self):
        return self.material

    def set_material(self, material):
        self.material = material

    def get_length(self):
        return self.length

    def set_length(self, length):
        if length is not None and length < 0:
            raise ValueError("Отрицательное значение длины недопустимо")
        self.length = length

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height is not None and height < 0:
            raise ValueError("Отрицательное значение высоты недопустимо")
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        if width is not None and width < 0:
            raise ValueError("Отрицательное значение ширины недопустимо")
        self.width = width

    def print_details(self, product_number):
        print(f"Товар #{product_number};")
        print(f"Наименование: {self.get_name()};")
        print(f"Розничная цена: {self.get_retail_price()}р;")
        print(f"Страна производства: {self.get_country_of_origin()};")
        print(f"Дата поступления: {self.get_arrival_date().strftime('%d.%m.%Y')};")
        print(f"Материал: {self.get_material()};")
        print(f"Категория: {self.get_purpose()};")
        print(f"Скидка: {self.get_discount()}%:")
        print(f"Стоимость со скидкой: {self.get_discounted_price(self.get_discount())}р;")
        if self.utilized:
            print("*Товар утилизируемый")
        print("_____")

    def ask_discount(self):
        discount = int(input(f"Введите размер скидки (в процентах) для товара: {self.get_name()}, Категория: {self.get_purpose()}\n"
                             "Размер скидки не более 20%: "))
        if discount > 20:
            print("Скидка не может быть больше 20%!")
            discount = 20
        self.set_discount(discount)
        print("_________")

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

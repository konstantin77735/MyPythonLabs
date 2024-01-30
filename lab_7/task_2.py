import random

class ColorPalette:
    def __init__(self):
        self.colors = {}

    def add_color(self, color):
        # Проверка на правильный формат шестнадцатеричного цвета
        if not self.is_valid_hex_color(color):
            print("Неверный формат цвета. Введите значение в формате #RRGGBB.")
            return

        # Генерация уникального ключа
        key = len(self.colors)
        self.colors[key] = color
        print(f"Цвет {color} добавлен с ключом {key}.")

    def generate_random_color(self):
        # Генерация случайного цвета в допустимых диапазонах
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.add_color(random_color)

    def find_dominant_color(self, element):
         # Проверяем, что переданный цвет имеет правильный формат
        if not (len(element) == 7 and element[0] == '#' and all(c in '0123456789ABCDEFabcdef' for c in element[1:])):
            raise ValueError("Некорректный формат шестнадцатеричного цвета")

        # Извлекаем компоненты цвета
        r = int(element[1:3], 16)
        g = int(element[3:5], 16)
        b = int(element[5:7], 16)

        # Определяем преобладающий цвет
        max_color = max(r, g, b)
        
        print(f"В цвете {element} преобладает:")
        if max_color == r:
            print("Красный")
        elif max_color == g:
            print("Зелёный")
        else:
            print("Синий")
        print("_____")
        
        # Спрашиваем пользователя, хочет ли он добавить цвет в палитру
        add_to_palette = input("Хотите добавить цвет в палитру? (да/нет): ").lower()

        if add_to_palette == 'да':
            self.add_color(element)
        elif add_to_palette == 'нет':
            print("Цвет не будет добавлен в палитру.")
        else:
            print("Некорректный ввод. Цвет не будет добавлен в палитру.")

    def is_valid_hex_color(self, color):
        # Проверка на правильный формат шестнадцатеричного цвета
        return isinstance(color, str) and len(color) == 7 and color[0] == '#' and all(c in '0123456789ABCDEFabcdef' for c in color[1:])

    def extract_hex_color(self, element):
        # Извлечение цвета из элемента
        # В реальном приложении здесь может быть сложная логика для определения цвета
        # Например, использование библиотеки для анализа изображений или цветовых палитур
        # В этом примере мы просто проверяем, что элемент является строкой и имеет длину 7 (формат #RRGGBB)
        return element if self.is_valid_hex_color(element) else None

if __name__ == "__main__":
    palette = ColorPalette()

    while True:
        print("1. Добавить цвет вручную")
        print("2. Генерировать случайный цвет")
        print("3. Определить преобладающий цвет и добавить его в словарь")
        print("4. Вывести текущую палитру")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            color_input = input("Введите цвет в формате #RRGGBB: ")
            palette.add_color(color_input)
        elif choice == '2':
            palette.generate_random_color()
        elif choice == '3':
            element = input("Введите элемент для определения преобладающего цвета: ")
            palette.find_dominant_color(element)
        elif choice == '4':
            print("Текущая палитра:")
            for key, color in palette.colors.items():
                print(f"{key}: {color}")
        elif choice == '5':
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 5.")

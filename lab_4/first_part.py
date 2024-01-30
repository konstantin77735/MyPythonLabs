# Часть 1. Задания с 1 по 5.

import re

def main():
    # реализация второго задания 3-ей лаб. работы
# в виде рекурсивной функции

# Например, если ввести: 5, 7, 11, 12, -1, то
#   -1 - отр. число, ввод отр. числа завершает исполнение программы
#   5 и 7 - это первая пара простых чисел
#   11 и 12 - это вторая пара простых чисел
#   Результат: кол-во пар простых чисел: 2

    def is_prime_recursive(n, i=2):
        if n < 2 or n&1 == 0:
            return False
        if i > int(n**0.5):
            return True
        return is_prime_recursive(n, i + 1)

    def count_consecutive_primes():
        previous_number = None
        current_number = int(input("Введите положительное целое число (для завершения введите отрицательное число): "))
        count = 0

        while current_number >= 0:
            if previous_number is not None and is_prime_recursive(previous_number) and is_prime_recursive(current_number):
                count += 1

            previous_number = current_number
            current_number = int(input("Введите положительное целое число (для завершения введите отрицательное число): "))

        return count;

    
    # 2. Обработка строки
    def process_string():
        user_input = input("Введите строку символов: ")
        processed_string = user_input.upper()  # Пример: преобразование строки в верхний регистр
        return processed_string

    # 3. Обработка текста
    def process_text():
        user_input = input("Введите текст из отдельных слов: ")
        words = user_input.split()  # Разделение введенного текста на слова
        processed_words = [word.capitalize() for word in words]  # Пример: преобразование каждого слова в заглавные буквы
        processed_text = ' '.join(processed_words)
        return processed_text

    # 4. Обработка регулярных выражения для поиска и преобразования текста;
    def process_regex():
        user_input = input("Введите текст для обработки с использованием регулярных выражений: ")
        pattern = input("Введите регулярное выражение для поиска: ")
        matches = re.findall(pattern, user_input)
        
        #pattern: Это регулярное выражение, переданное в качестве первого аргумента. Регулярное выражение используется для поиска совпадений в строке.
        #user_input: Это строка, в которой мы ищем совпадения с помощью регулярного выражения.
        #re.findall ищет все неперекрывающиеся совпадения с регулярным выражением в заданной строке. Он возвращает список всех найденных совпадений.

        processed_text = ' '.join(matches)
        #' '.join(matches) выполняет объединение элементов списка matches в одну строку, 
        # разделяя каждый элемент строкой пробела. В контексте функции process_regex, это используется для создания строки, 
        # содержащей все найденные совпадения, разделенные пробелами.
        
        return processed_text

    while True:
        # 5. Реализация заданий связанных со строками в виде вложенных функций
        choice = input("Меню:"+"\n"
                +"1. Задание из 3-ей лаб. работы: в виде рекурсии;" +"\n" 
                +"2. Строка;"+"\n"
                +"3. Текст;"+"\n"
                +"4. Регулярное выражение; "+"\n"
                +"Выберите задание (введите цифру):")
        if choice == '1':
            result = count_consecutive_primes()
            print("1. Кол-во пар подряд идущих простых чисел:", result)
            print("_____")
            
        elif choice == '2':
            result = process_string()
            print("2. Обработка строки: ", result)
            print("_____")
            
        elif choice == '3':
            result = process_text()
            print("3. Обработка текста: ", result)
            print("_____")
        elif choice == '4':
            result = process_regex()
            print("4. Обработка регулярных выражений для поиска и преобразования текста:", result)
            print("_____")
        else:
            print("Некорректный выбор.")
            print("_____")

   

# Пример использования
main()


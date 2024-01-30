# Например, если ввести: 5, 7, 11, 12, -1, то
#   -1 - отр. число, ввод отр. числа завершает исполнение программы
#   5 и 7 - это первая пара простых чисел
#   11 и 12 - это вторая пара простых чисел
#   Результат: кол-во пар простых чисел: 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes():
    previous_number = None
    current_number = int(input("Введите положительное целое число (для завершения введите отрицательное число): "))
    count = 0

    while current_number >= 0:
        if previous_number is not None and is_prime(previous_number) and is_prime(current_number):
            count += 1

        previous_number = current_number
        current_number = int(input("Введите положительное целое число (для завершения введите отрицательное число): "))

    return count

# Пример использования
result = count_consecutive_primes()
print("Количество пар подряд идущих простых чисел:", result)

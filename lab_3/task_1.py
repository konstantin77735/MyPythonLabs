#несколько совершенных чисел для примера: 6, 28, 496, 8128

def is_perfect(n):
    # Функция для проверки, является ли число совершенным
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

# нужно в последователньости посчитать СКОЛЬЦО отрицательных совершенных числе после нуля
# например, последовательность: 1,0,-28,28. Отр. соверш. число только -28, (число без минуса не считается),
# поэтому ответ 1

def count_negative_perfect_after_zero():
    found_zero = False
    count = 0

    while True:
        user_input = input("Введите число (для завершения введите 'Q'): ")
        
        #если ввели q, то завершаем программу
        if user_input.upper() == 'Q':
            break

        num = int(user_input)
        
        if num == 0:
            found_zero = True
        elif found_zero and num < 0 and is_perfect(abs(num)):
            count += 1

    return count

# Пример использования
result = count_negative_perfect_after_zero()

if result == 0:
    print("Количество отрицательных совершенных элементов после первого нуля равно нулю.")
else:
    print("Количество отрицательных совершенных элементов после первого нуля:", result)

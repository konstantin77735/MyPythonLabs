
def find_ratio(n, arr):
    if n <= 0:
        return "Неверное значение n"

    max_index = arr.index(max(arr)) # находит индекс макс. элемента в массиве

    positive_before_max = [num for num in arr[:max_index] if num > 0] # все пол. эл-ты до макс. элемента
    negative_after_max = [num for num in arr[max_index + 1 :] if num < 0] # все отр. эле-ты после макс. элемента

    sum_positive = sum(positive_before_max)
    sum_negative = sum(negative_after_max)

    if sum_positive == 0 or sum_negative == 0:
        return "Положительные или отрицательные элементы отсутствуют"

    ratio = sum_positive / sum_negative # отношение суммы пол. элментов к сумме отр. эл-тов
    return ratio

# Пример использования
n = int(input("Введите натуральное число n: "))

# получаем кортеж введёных символов ↓
arr = tuple(map(float, input("Введите вещественный массив из n элементов через пробел: ").split()))

result = find_ratio(n, arr)
print("Отношение суммы положительных элементов к сумме отрицательных элементов:", result)

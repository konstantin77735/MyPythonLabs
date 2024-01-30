def replace_elements(n, p, q, array):
    modified = False  # Флаг, показывающий, были ли произведены замены

    for i in range(n):
        if abs(array[i]) % p == q:
            array[i] = 0
            modified = True

    if not modified:
        print("Отсутствуют элементы для замены.")

    return array

# Пример использования
n = int(input("Введите натуральное число n: "))
p = int(input("Введите натуральное число p (p > q >= 0): "))
q = int(input("Введите натуральное число q (p > q >= 0): "))


#split разделяет массив по пробелу
#map применяет int к каждому элементу массива
#list создаёт список
array = list(map(int, input(f"Введите массив из {n} целых чисел через пробел: ").split()))

result = replace_elements(n, p, q, array)
print("Модифицированный массив:", result)

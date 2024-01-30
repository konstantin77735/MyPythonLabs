def insert_zero_before_value(n, arr, target_value):
    modified_array = []  # Создаем новый массив для сохранения результатов вставки
    found_target_value = False  # Флаг, показывающий, были ли найдены элементы с заданным значением

    for num in arr:
        modified_array.append(num)
        if num == target_value:
            modified_array.append(0)
            found_target_value = True

    if not found_target_value:
        print(f"Массив не содержит элементов со значением {target_value}.")

    return modified_array

# Пример использования
n = int(input("Введите натуральное число n: "))
array = list(map(int, input(f"Введите массив из {n} целых чисел через пробел: ").split()))
target_value = int(input("Введите значение элемента для вставки нуля перед ним: "))

result = insert_zero_before_value(n, array, target_value)
print("Модифицированный массив:", result)


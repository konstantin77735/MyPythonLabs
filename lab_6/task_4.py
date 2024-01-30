def generate_b_array(n, a):
    b = []

    while len(b) < n:
        min_element = min(a)
        max_element = max(a)

        b.append(min_element)
        a.remove(min_element)

        if len(b) < n:
            b.append(max_element)
            a.remove(max_element)

    return b

# Пример использования
n = int(input("Введите натуральное число n: "))
a = list(map(float, input(f"Введите вещественный массив из {n} элементов через пробел: ").split()))

result_b = generate_b_array(n, a)
print("Массив b:", result_b)

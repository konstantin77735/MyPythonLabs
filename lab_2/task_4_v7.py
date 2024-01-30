# Ввод номера семестра с клавиатуры
semester = int(input("Введите номер семестра: "))

# Используем оператор выбора if-elif-else для определения курса
if semester >= 1 and semester <= 2:
    course = 1
elif semester >= 3 and semester <= 4:
    course = 2
elif semester >= 5 and semester <= 6:
    course = 3
# Продолжайте добавлять условия для остальных курсов по аналогии

# Вывод результата
if 'course' in locals():
    print(f"Семестр {semester} относится к {course} курсу.")
else:
    print("Некорректный номер семестра. Пожалуйста, введите номер от 1 до 12.")

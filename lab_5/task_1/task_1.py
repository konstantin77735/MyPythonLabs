import os


# лаб. работы находятся в MyPythonLabs. 
# Если открыта эта папка, то нужно перейти в директорию "lab_5"
current_directory = os.getcwd()
if "lab_5" not in current_directory:
    current_directory = os.path.join(current_directory, "lab_5")


def remove_duplicates(input_file, output_file):
    unique_numbers = []

    with open(input_file, 'r') as f:
        # Читаем числа из файла и добавляем их в список (если они еще не встречались)
        for line in f:
            number = int(line.strip())
            if number not in unique_numbers:
                unique_numbers.append(number)

    with open(output_file, 'w') as g:
        # Записываем уникальные числа в новый файл
        for number in unique_numbers:
            g.write(str(number) + '\n')

# Пример использования
input_file_path = current_directory+"/task_1/input.txt"  # Путь к вашему исходному файлу
output_file_path = current_directory+"/task_1/output.txt"  # Путь к файлу с уникальными числами

# удалить дубликаты в файле
remove_duplicates(input_file_path, output_file_path)
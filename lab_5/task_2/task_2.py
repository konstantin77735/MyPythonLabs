import datetime
import os

# лаб. работы находятся в MyPythonLabs. 
# Если открыта эта папка, то нужно перейти в директорию "lab_5"
current_directory = os.getcwd()
if "lab_5" not in current_directory:
    current_directory = os.path.join(current_directory, "lab_5")



def find_books_by_author_and_year(filename, author, start_year):
    result_books = []
    current_year = datetime.datetime.now().year

    with open(filename, 'r',  encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            book_author = parts[0]
            book_title = parts[1]
            book_year = int(parts[2])

            if book_author == author and book_year >= start_year:
                result_books.append(book_title)

    return result_books

def find_last_edition_year(filename, book_title):
    with open(filename, 'r',  encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            current_title = parts[1]
            current_year = int(parts[2])

            if current_title == book_title:
                return current_year

    return None

def write_last_5_years_books(filename, output_filename):
    current_year = datetime.datetime.now().year
    last_5_years = range(current_year - 5, current_year + 1)

    with open(filename, 'r', encoding='utf-8') as f, open(output_filename, 'w',  encoding='utf-8') as output_file:
        for line in f:
            parts = line.strip().split(',')
            book_year = int(parts[2])

            if book_year in last_5_years:
                output_file.write(line)

# Пример использования
filename = current_directory+'/task_2/books.txt'  # Путь к вашему файлу с информацией о книгах
author_name = input("Введите фамилию автора: ") # Замените на нужного автора
start_year = 1960       # Начиная с какого года искать книги автора

books_by_author = find_books_by_author_and_year(filename, author_name, start_year)
print(f"Названия книг автора {author_name} после {start_year} года: {books_by_author}")

book_title_to_find = 'Информатика'  # Замените на нужное название книги
last_edition_year = find_last_edition_year(filename, book_title_to_find)
print(f"Год последнего издания книги '{book_title_to_find}': {last_edition_year}")

output_filename = current_directory+'/task_2/last_5_years_books.txt'
write_last_5_years_books(filename, output_filename)
print(f"Список книг, изданных за последние 5 лет, записан в файл {output_filename}")

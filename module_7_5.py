import os
import time


directory = '.'

directory_norm = os.path.normpath(directory)

count = 0

for dirpath, dirmanes, filenames in os.walk(directory_norm):
    for file in filenames:
        full_filenames = os.path.join(dirpath, file)
        filetime = os.path.getmtime(full_filenames)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(full_filenames)
        parent_file = os.path.dirname(full_filenames)
        count += 1
        print(f'Обнаружен файл: {file}, Путь: {full_filenames}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_file}')
print(count)
# Ввод размера файла в байтах
file_size_bytes = int(input("Введите размер файла в байтах: "))

# Вычисление количества полных килобайтов
full_kilobytes = file_size_bytes // 1024

print("Количество полных килобайтов:", full_kilobytes)

# Запрос текста от пользователя
my_string = input("Введите произвольный текст: ")

# Вывод длины строки
print("Длина строки:", len(my_string))

# Вывод строки в верхнем регистре
print("Строка в верхнем регистре:", my_string.upper())

# Вывод строки в нижнем регистре
print("Строка в нижнем регистре:", my_string.lower())

# Удаление пробелов из строки
my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)

# Вывод первого символа строки
print("Первый символ строки:", my_string[0])

# Вывод последнего символа строки
print("Последний символ строки:", my_string[-1])
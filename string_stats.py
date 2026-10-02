# Подсчитайте отдельно количество букв, цифр, пробелов и остальных символов во введённой строке.
# Выведите четыре результата. Регистр букв не имеет значения.
#
# Пример: для строки `Дом 42!` программа должна найти 3 буквы, 2 цифры, 1 пробел и 1 другой символ.

string = input("Введите строку для проверки: ")
count_letter = 0
count_num = 0
count_probel = 0
count_other = 0
for num in string:
    if num.isalpha():
        count_letter += 1
    elif num.isnumeric():
        count_num += 1
    elif " " in num:
        count_probel += 1
    else:
        count_other += 1

print(f"Найдено: {count_letter} букв, {count_num} цифр, {count_probel} пробелов, {count_other} друних символов") 

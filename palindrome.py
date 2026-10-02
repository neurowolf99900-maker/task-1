# Проверьте, читается ли введённая фраза одинаково слева направо и справа налево.
# При проверке игнорируйте регистр, пробелы, цифры и знаки препинания: учитывать нужно только буквы.
#
# Пример: 'А роза упала на лапу Азора!' — палиндром.

string = "А роза упала на лапу Азора!"
new_string = ""
for num in string:
    if num.isalpha():
        new_string += num.lower()
new_string_2 = new_string[::-1]
if new_string == new_string_2:
    print("палиндром: ")
print(new_string)
print(new_string_2)

# Сожмите строку, заменяя каждую непрерывную серию одинаковых символов самим символом и количеством повторов.
# Даже одиночный символ должен получить число 1.
#
# Пример: 'aaabbcaaaa' → 'a3b2c1a4'.

string = input("Введите строку для сжатия: ")
new_list = ""
count = 1
for num in range(len(string) - 1):
    if string[num] == string[num + 1]:
        count +=1
    else:
        new_list += string[num] + str(count)
        count = 1

new_list += string[-1] + str(count)
print(new_list)

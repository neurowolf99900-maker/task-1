# В строке могут встречаться целые неотрицательные числа, состоящие из нескольких цифр.
# Найдите сумму всех таких чисел. Соседние цифры относятся к одному числу.
#
# Пример: 'Заказ: 12 ручек, 3 блокнота и 105 скрепок' → 120.

string = input("Введите строку для подсчета: ")
count = 0
new_list = ""
for num in string:
    if num.isnumeric():
        new_list += num
        print(new_list)
    elif not num.isnumeric() and new_list == "":
        continue
    else: 
        count = int(new_list)
        
print(count)



# not num.isnumeric():
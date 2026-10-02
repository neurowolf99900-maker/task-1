# Напишите программу, которое получает математическое выражение и вычисляет ее результат.
# В выражении могут быть либо только операции суммирования, либо только операции умножения:
#
# Пример: для строки `1+2+3+4` программа должна посчитать 10.
# Пример: для строки `10*20*30*40` программа должна посчитать 240000.

expression = input("Введите выражение (сумму или произведение): ")
new_list = " "
if "+" in expression:
    new_list = expression.split("+")
    counter = 0
    for num in new_list:
        counter += int(num)
elif "*" in expression:
    counter = 1
    new_list = expression.split("*")
    for num in new_list:
        counter *= int(num)
print(counter)

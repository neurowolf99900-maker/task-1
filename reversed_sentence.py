# Выведите слова предложения в обратном порядке, не разворачивая символы внутри слов.
#
# Пример: 'Python делает задачи понятнее' → 'понятнее задачи делает Python'

sentence = "Python делает задачи понятнее"
sentence = sentence.split()
new_list = ""
new_list = sentence[::-1]
for num in new_list:
    print(num, end=" ")
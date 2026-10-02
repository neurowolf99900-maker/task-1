# Разверните каждое слово в предложении, не меняя порядок самих слов.
# В результате между словами должен быть один пробел.
#
# Пример: 'Python is fun' → 'nohtyP si nuf'.

sentence = "Python is fun" 
sentence = sentence.split()
new_list = ""
for num in sentence:
    print(num[::-1], end=" ")


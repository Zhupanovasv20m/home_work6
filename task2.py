# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)\


import random
my_list = [random.randint(0, 100) for _ in range (10)]
print(my_list)
minimum = int(input('Введите нижнюю границу: '))
maximum = int(input('Введите верхнюю границу: '))

print('В заданном диапазоне элементы находятся под следующими индексами:')
for i in range(0, len(my_list)):
    if my_list[i]>= minimum and my_list[i]<=maximum:
        print(i, end=' ')


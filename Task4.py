
from random import randint
my_list = []
n = int(input('Введите количество элементов в списке '))
for i in range(n):
      my_list.append(randint(-10,+10))
print('Исходный список ', my_list)
new_list=[my_list[i] for i in range(0,len(my_list)) if my_list.count(i) == 1]
print('Уникальный список',new_list)
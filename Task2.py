from random import randint
my_list = []
new_list =[]

n = int(input('Введите количество элементов в списке '))
for i in range(n):
      my_list.append(randint(-1000,+1000))
print('Исходный список ', my_list)
for i in range(0,len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])
print('Итоговый список ', new_list)

from itertools import count
from math import factorial
def gen_factor():
    for el in count(1):
        yield factorial(el)

generator = gen_factor()
x = 0
n=int(input('Введите до какого числа выводить факториалы: '))
for i in generator:
    if x == n:
        break
    else:
        x+=1
        print(f'Factorial {x} ={i}')
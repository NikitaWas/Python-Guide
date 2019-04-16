print('Занятие 3. Вычисления»')

print('Задача «Последняя цифра числа»')
x = str(input())
last_digit = int(x[-1]) # -1 -- 1 выводимые цифры
print(last_digit)

print('Задача «МКАД»')
v = int(input())
t = int(input())
print((v * t) % 109)

print('Задача «Дробная часть»')
x = float(input())
n = x % 1
print(round(n, 3))

print('Задача «Первая цифра после точки»')
x = float(input())
n = x % 1
v = str(n)
first_digit = int(v[2])
print(first_digit)

print('Задача «Конец уроков»')
x = int(input())
h = (x * 45 + (x // 2) * 5 + ((x + 1) // 2 - 1) * 15)
m = h % 60
print(h // 60 + 9, m)

print('Задача «Автопробег»')
n = int(input())
m = int(input())
v = n / 24
from math import *
t = ceil(m / v / 24)
print(t)

print('Задача «Стоимость покупки»') # Вариант-1
a = int(input())
b = int(input())
n = int(input())
x0 = a + b / 100
x = round(x0 * n, 2)
print(x)

print('Задача «Стоимость покупки»') # Вариант-2
a = int(input())
b = int(input())
n = int(input())
x = n * (100 * a + b)
print(x // 100, x % 100)
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

print('Задача «Разность времен»')
h0 = int(input())
m0 = int(input())
s0 = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())
A = h0 * 3600 + m0 * 60 + s0
B = h1 * 3600 + m1 * 60 + s1
S = abs(A - B)
print(S)

print('Задача «Улитка»')
h = int(input())
a = int(input())
b = int(input())
n = int((h - a - 1) // (a - b) + 2)
print(n)

print('Задача «Число десятков»')
x = int(input())
if x // 10 == 0:
    print(0)
else:
    n = int(x // 10)
    v = str(n)
    last_digit = int(v[-1])
    print(last_digit)

print('Задача «Сумма цифр»')
x = int(input())
v = str(x)
first_digit = int(v[0])
mean_digit = int(v[1])
last_digit = int(v[-1])
print(first_digit + mean_digit + last_digit)

print('Задача «Гипотенуза»')
a = int(input())
b = int(input())
c = a**2 + b**2
from math import *
print(sqrt(c))

print('Задача «Часы - 1»') # Вариант-1
h = int(input())
m = int(input())
s = int(input())
s1 = h * 3600 + m * 60 + s
u = 360 * s1 / 12 / 3600
print(u)

print('Задача «Часы - 1»') # Вариант-2
h = int(input())
m = int(input())
s = int(input())
h1 = h * 3600 * 360 / 12 / 3600
m1 = m * 60 * 360 / 12 / 3600
s1 = s * 360 / 12 / 3600
print(h1+m1+s1)

print('Задача «Часы - 2»')
m1 = float(input())
print(m1 % 30 * 12)

print('Задача «Часы - 3»')
f = float(input())
h = int(f // 30)
m = int(f % 30 * 2)
s = int(f % 0.5 * 120)
print(h, m, s)

print('Задача «Проценты»')
P = int(input())
X = int(input())
Y = int(input())
a = (P/100 * (100 * X + Y)) + (100 * X + Y)
print(round(a // 100, 2), round(a % 100, 2))
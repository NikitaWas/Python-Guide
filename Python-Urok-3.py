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
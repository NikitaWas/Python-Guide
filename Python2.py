print('Урок 2')
print('Условия')
print('Введите любое число')
x = int(input())
if x>5:
    print(x)
else:
    print(5)

x = int(input())
if x < 0:
    x = -x
print(-x)

x = int(input())
y = int(input())
if x > 0:
    if y > 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                   # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y > 0:               # x < 0, y > 0
        print("Вторая четверть")
    else:                   # x < 0, y < 0
        print("Третья четверть")

a = int(input())
b = int(input())
if a % 10 == 0 or b % 10 == 0:
    print('YES')
else:
    print('NO')

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif y > 0:
    print("Вторая четверть")
else:
    print("Третья четверть")

print('Задача «Минимум из двух чисел»')
print("Введите любое число")
x = int(input())
print("Введите любое число")
y = int(input())
if x < y:
    print(x)
else:
    print(y)

print('Задача «Знак числа»')
print("Введите любое число")
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

print('Задача «Шахматная доска»')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 == 0:
    if (x2 + y2) % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if (x2 + y2) % 2 != 0:
        print("YES")
    else:
        print("NO")

print('Задача «Високосный год»')
a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')



print("Задача «Минимум из трех чисел»")
a = int(input())
b = int(input())
c = int(input())
S = [a, b, c]
m = min(S)
print(m)

print("Задача «Сколько совпадает чисел»")
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b:
    if a == c:
        print(2)
    else:
        if c == b:
            print(2)
        else:
            print(0)
else:
    print(0)

print("Задача «Ход ладьи»")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2:
    print('YES')
else:
    if y1 == y2:
        print('YES')
    else:
        print('NO')

print("Задача «Ход короля»")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x2 - x1 <= 1 and x2 - x1 >= -1):
    if (y2 - y1 <= 1 and y2 - y1 >= -1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

print("Задача «Ход слона»")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print ("YES")
else:
    print ("NO")
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)
print(37 / 3)
print(37 // 3)
print(37 % 3)  


print('Как вас зовут?')
name = input()
print('Здравствуйте, ' + name + '!')

a = input()
b = input()
s = a + b
print(s)

first = 5
second = 7
print(first * second)


d = int(input())
e = int(input())
f = d + e
print(f)


print('Сумма трёх чисел')
# Можете ли вы изменить её, чтобы она складывала три числа?
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

print('Площадь прямоугольного треугольника')
# Числа b и h можно считывать так:
print('Введите число b')
b = int(input())
print('Введите число h')
h = int(input())
a = (1/2 * (b * h))
print(a)

print('Дележ яблок')
n = int(input())
k = int(input())
print(k // n)
print(k - n * (k // n))

print('Электронные часы')
a = int(input())
b = a//60%24
c = a%60
print(b,c)

print('Следующее и предыдущее')
n = int(input())

print ('The next number for the number '+str(n)+ ' is ' +str(n+1)+ '.')
print ('The previous number for the number '+str(n)+ ' is ' +str(n-1)+ '.')

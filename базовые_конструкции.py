# Наказание
natural_number = int(input())
text = str(input())
print(f'Я больше никогда не буду писать "{text}"!\n' * natural_number)


# Деловая колбаса
n = int(input())
m = int(input())
summ = n * m
print(summ // 2)


# Детский сад — штаны на лямках
name = input()
number = input()
print("Группа №" + str(number[0]) + ".")
print(str(number[2]) + ". " + str(name) + ".")
print("Шкафчик: " + str(number) + ".")
print("Кроватка: " + str(number[1]) + ".")


# Автоматизация игры
number = str(input())
print(f'{number[1]}{number[0]}{number[3]}{number[2]}')


# Условный оператор

#Красота спасёт мир
a = input()
c = list(a)
i = int(min(a)) + int(max(a))
c.remove(min(a)), c.remove(max(a))

if i == int(c[0]) * 2:
    print("YES")
else:
    print("NO")

#Музыкальный инструмент
a = int(input())
b = int(input())
c = int(input())

if c < b + a and b < c + a and a < b + c:
    print("YES")
else:
    print("NO")


# Властелин Чисел: Братство общей цифры
a = input()
b = input()
c = input()

if a[0] == b[0] == c[0]:
    print(a[0])
elif a[1] == b[1] == c[1]:
    print(a[1])

#Властелин Чисел: Две Башни
n = sorted(input())
i = n.count('0')
print(n[i] + n[0 if i else i + 1], n[-1] + n[-2])


#Циклы

#Считалочка - не решена
a = int(input()),
b = int(input()),
for i in range(a, b):
    print(i)

# Факториал
a = int(input())
factorial = 1
for i in range(1, a + 1):
    factorial *= i
print(factorial)

# Простая задача
n = int(input())
i = 2
result = 'YES'
if n > 1:
    while n % i:
        if i > n ** 0.5:
            break
        i += 1
    else:
        result = 'NO'
else:
    result = 'NO'
print(result)


#Вложенные циклы
# Таблица умножения - не решена
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        if j < x:
            print(i * j)
        else:
            print(i * j)

# Не таблица умножения
for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        print(f'{j} * {i} = {i * j}')

#На старт! Внимание! Марш!
for i in range(int(input())):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')
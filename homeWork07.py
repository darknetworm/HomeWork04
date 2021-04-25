result = 1


def fact(n):
    for i in range(1, n + 1):
        yield i


try:
    userNum = int(input('Введите число, до которого необходимо посчитать факториалы: '))
except ValueError:
    exit('Введеные данные не являются числом')
for el in fact(userNum):
    print(f'Факториал числа {el} равен {result * el}')
    result = result * el

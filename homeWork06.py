from itertools import count
from itertools import cycle

'''Генерируеи числа с указанного до +10 с помощью функции count'''
try:
    startNum = int(input('Введите целое число для начала генератора: '))
    print(f'Генерировать будем до числа {startNum + 10}')
except ValueError:
    exit('Введено неверное значение')

for x in count(startNum):
    if x > startNum + 10:
        break
    print(x)

'''Выводим элементы списка с помощью функции cycle, определенное пользователем количество раз'''
itemsList = [23, 'John', True, [1, 2, 3]]
countNum = 0
try:
    userCount = int(input('Введите количество повторов элементов: '))
except ValueError:
    exit('Введено неверное значение')
for item in cycle(itemsList):
    if countNum == userCount:
        break
    print(f'{countNum + 1}. {item}')
    countNum += 1

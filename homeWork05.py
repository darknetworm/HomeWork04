from functools import reduce

print('Произведение четных чисел в диапазоне от 100 до 1000 равно (очень большое число): ' + str(
    reduce((lambda x, y: x * y), [num for num in range(100, 1001) if num % 2 == 0])))

print('Список чисел в пределах от 20 до 240, кратных 20 или 21: ' + str(
    [num for num in range(20, 241) if (num % 20 == 0 or num % 21 == 0)]))

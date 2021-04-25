firstList = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

resultList = [el for el in firstList if firstList.count(el) == 1]
print(f'Первоначальный список: {firstList}')
print(f'Результирующий список: {resultList}')

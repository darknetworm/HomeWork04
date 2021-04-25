'''Проглядел, что список надо генерировать и взял список из ДЗ'''
firstList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
finalList = []


def readerList():
    for item in firstList:
        yield item


firstNum = next(readerList())
for num in readerList():
    if firstNum < num:
        finalList.append(num)
    firstNum = num

print('Исходный список: ' + str(firstList))
print('Результирующий список: ' + str(finalList))

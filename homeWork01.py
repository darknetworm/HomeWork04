import sys


def salary(workHrs, rateHrs, bonuses):
    return (workHrs * rateHrs) + bonuses


try:
    file, nameWrkr, workHr, rateHr, bonus = sys.argv
    print(sys.argv)
except:
    print('Введите аргументы в виде "имя" "выработка в часах" "ставка в час" "премия"')
    exit('Что-то пошло не так, возможно Вы не указали аргументы')

print(f'{nameWrkr.title()} получает заработную плату в размере {salary(int(workHr), int(rateHr), int(bonus))} Пиастров')

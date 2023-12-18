# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(9, -1, -1):
    younum = int(input("введите число: "))
    if younum == num:
        print("Верно!")
        break
    elif i == 0:
        print(
            f"Вы проиграли , загаданное число было {num}")
    elif younum > num:
        print(f"Меньше, попыток :{i}")
    else:
        print(f"Больше, попыток :{i}")





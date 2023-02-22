# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

number = int(input('Введите кол-во монеток: '))
eagles = 0
tails = 0
for i in range(0,number):
    monet_side = random.randint(0, 1)
    print(monet_side,end=" ")
    if monet_side == 0: eagles += 1
    else: tails += 1
print("\n",f"Минимум нужно перевернуть {eagles if eagles < tails else tails}")


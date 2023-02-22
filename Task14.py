# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


number = int(input('Введите натуральное число: '))

degree_of_two = 1
while degree_of_two <= number:
    print(degree_of_two, end=" ")
    degree_of_two *= 2


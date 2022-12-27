# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

number_n = int(input('Введите число N: '))
number_x = 1 

while number_x < number_n:
  if number_x % 2 == 0:
    print(number_x, end = ' ')
  number_x = number_x + 1
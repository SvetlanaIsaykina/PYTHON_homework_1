# Задача1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

number = int(input('Введите число: '))

if number == 1:
  print('Это понедельник')
elif number == 2:
  print('Это вторник')
elif number == 3:
  print('Это среда')
elif number == 4:
  print('Это четверг')
elif number == 5:
  print('Это пятница')
elif number == 6:
  print('Это суббота')
elif number == 7:
  print('Это воскресенье')
else:
  print('Нет такого дня')
# Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B
# имеют одинаковую четность».

A = input("Введите любое целое число A: ")
B = input("Введите любое целое число B: ")

try:
  A = int(A)
  B = int(B)

  if (int(A) % 2 == 0) == (int(B) % 2 == 0):
      print('Высказывание: Числа A и B имеют одинаковую четность - Истина')
  else:
      print('Высказывание: Числа A и B имеют одинаковую четность - Ложь')

except ValueError:
  print('Вы ввели не числа, запустите программу заново и введите числа')





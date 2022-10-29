# Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B
# имеют одинаковую четность».

A = input()
B = input()

try:
  tmp = float(A)
  tmp = float(B)
except ValueError:
  print('Это не число')

A = int(A)
B = int(B)

if (int(A) % 2 == 0) == (int(B) % 2 == 0):
    print('Истина')
else:
    print('Ложь')



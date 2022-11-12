#2. Описать функцию SortInc3(A, B, C), меняющую содержимое переменных A, B, C
#таким образом, чтобы их значения оказались упорядоченными по возрастанию (A,
#B, C — вещественные параметры, являющиеся одновременно входными и
#выходными). С помощью этой функции упорядочить по возрастанию два данных
#набора из трех чисел: (Ai, Bi, Ci) и (A2, B2, C2).

def SortInc3(A, B, C):
 lst = [A, B, C]
 #реализация пузырьковой системы. Она перебирает список
 # и на каждой итерации сравниваем элементы попарно.
 # При необходимости элементы меняются местами, чтобы
 # больший элемент отправлялся в конец списка.
 swapped = False
 for i in range(len(lst) - 1, 0, -1):
  for j in range(i):
   if lst[j] > lst[j + 1]:
    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    swapped = True
  if swapped:
   swapped = False
  else:
   break
 return lst

A = input("Введи целое число A: ")
B = input("Введи целое число B: ")
C = input("Введи целое число C: ")

while type(A) and type(B) and type(C) != int: # обработка исключений
 try:
  A = int(A)
  B = int(B)
  C = int(C)

 except ValueError:
  print("Неправильно ввели!")
  # повторный ввод
  A = input("Введи целое число A: ")
  B = input("Введи целое число B: ")
  C = input("Введи целое число C: ")

print('Цифры в порядке возрастания: ', *SortInc3(A,B,C))
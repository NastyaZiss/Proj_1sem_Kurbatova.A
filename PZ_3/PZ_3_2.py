# Дано целое число, лежащее в диапазоне 1-999. Вывести его строку- описание вида
# «четное двузначное число», «нечетное трехзначное число» и т. д.

num = input()

try:
  tmp = float(num)
except ValueError:
  print('Это не число')


num= int(num)
if num % 2 == 0:
    print('Четное', end=" ")
else:
    print('Нечетное', end=" ")
if len(str(num))==2:
    print('двухзначное')
elif len(str(num))==3:
    print('трехзначное')


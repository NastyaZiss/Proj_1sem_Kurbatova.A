# 1.В последовательности на n целых чисел найти и вывести:
# 1. минимальный среди положительных
# 2. элементы кратные пяти
# 3. их среднее арифметическое
import random
from statistics import mean
lst=[3,4]
n = int(input("Введите количество элементов в списке: n = "))
lst = [random.randint(-3, 30) for a in range(int(n))]
print('Наш список: ',lst)
print('1. минимальный среди положительных: ',min([a for a in lst if a>0]))
print('2. элементы кратные пяти: ',list([a for a in lst if a%5==0]))
print('3. их среднее арифметическое: ',sum(lst)/len(lst))

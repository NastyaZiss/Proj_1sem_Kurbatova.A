# 1. В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
import functools

matx=[[1,2,3,4,5],[3,7,8,9,10],[6,57,8,5,3],[2,4,56,7,1]]

n = int((input('Введите номер строки, нумерация строк начинается с единицы, ваш массив состоит из 4, больше 4 число не вводить: ')))
lst = [x for x in matx[n-1]]
print('Прозведение: ', functools.reduce(lambda a, b: a * b, lst))
print('Сумма: ', functools.reduce(lambda a, b: a + b, lst))
print('Ваша строка', matx[n - 1])



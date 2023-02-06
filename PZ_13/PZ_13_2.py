# 2. В матрице найти сумму элементов второй половины матрицы.
import math
import functools

matx=[[1,2,3,4,5],[3,7,8,9,10],[6,57,8,5,3],[2,4,56,7,1],[1,2,3,4,2]]

lenght = (math.ceil((len(matx))/2))
# print(lenght)
lst=[]

for i in range(-lenght,0):
    matx_el=matx[i]
    h = functools.reduce(lambda a, b: a + b, matx_el)
    lst.append(h)
    # print(i)


print('Сумма половины матрицы',sum(lst))

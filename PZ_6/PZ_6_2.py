#2. Дано число R и список A размера N. Найти элемент списка, который наиболее близок
# к числу R (то есть такой элемент AK, для которого величина |AK - R| является
# минимальной).

import random

A = []
min_search_list = []
R = input("Введите целое число R: ")
N = input("Введите размер списка(целое натуральное число): ")

while type(N) and type(R) != int: # обработка исключений
    try:
        N = int(N)
        R = int(R)
        # заполнение списка рандомными натуральными числами
        while len(A) < N:
            a = random.randint(1, 30)
            A.append(a)

        for i in A:
            min_search_list.append(i - R)

        min_num = min(min_search_list)
        #print(min_num)
        for i in A:
            if i - R == min_num:
                min_num = i
                break

        print("Элементы списка: ", *A)
        print("Элемент списка, который наиболее близок к числу R: ", min_num)

    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите размер списка(целое натуральное число): ")
        R = input("Введите целое число R: ")



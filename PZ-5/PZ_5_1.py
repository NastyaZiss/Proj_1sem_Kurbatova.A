#Составить функцию, которая напечатает сорок любых символов

sim = input("Введите символ: ")

def SortInc3(sim):
    return sim*40
    # list_si = []
    # for i in range(60, 60 + num):
    #         list_si.append(chr(i))
    #
    # return ''.join(list_si)

print("40 любых символов: ", end=" ")
print(SortInc3(sim))

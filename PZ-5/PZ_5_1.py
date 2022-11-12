#Составить функцию, которая напечатает сорок любых символов

def SortInc3(num):
    list_si = []
    for i in range(60,60 + num):
            list_si.append(chr(i))

    return ''.join(list_si)

print("40 любых символов: ", end=" ")
print(SortInc3(40))

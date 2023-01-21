# 2. Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить строку
# наименьшей длины.

d = 0
for i in open('stix.txt', encoding='UTF-8'):
 print(i, end='')
 for j in i:
    if j == '.' or j=='!' or j==',':
        d += 1
print(end='\n')

print('Количество знаков препинания : ', d, end='\n')

f1 = open('stix.txt', encoding='UTF-8')
list_lines = f1.readlines()  # список строк
list_len = []
# Создаю список с длинами строк
for line in list_lines:
    len_line = len(line)
    list_len.append(len_line)

# Нахожу минимальную длину
min_int = min(list_len)
# Нахожу индекс минимального длины
index_min = list_len.index(min_int)

# Теперь я вывожу строку с таким же индексом
print('Самая маленькая строка: ', list_lines[index_min])

f2 = open('result.txt', 'w', encoding='UTF-8')
# Добавила в второй файл
f2.writelines(str(list_lines[index_min]))
f2.close()



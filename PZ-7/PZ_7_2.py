# 2. Дана строка, содержащая полное имя файла. Выделить из этой строки название
# первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
# вывести символ «\».


# -> C:\Users\Настя\Desktop\algorutmi\PZ-7.doxc
# <- Users

# -> C:\PZ-7.doxc
# <- \

file_name = input("Введите имя файла: ")
list_file_name = file_name[3:].split("\\")
print(list_file_name)
if list_file_name[0].count(".") == 1:
    print("\\")
else:
    print(list_file_name[0])
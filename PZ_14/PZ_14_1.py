import re
# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл.

file = 'Dostoevsky.txt'
import re



with open(file, 'r', encoding='utf-8') as file:
 text = file.read()
 p = re.compile(r"После.*",re.M)
 print(p.findall(text))
 #reg_name = re.split(p, text)


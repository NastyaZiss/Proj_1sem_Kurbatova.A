# 2.Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
import  string

STR = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
print('Символы пунктуации: ', [a for a in STR if not a.isalpha()])

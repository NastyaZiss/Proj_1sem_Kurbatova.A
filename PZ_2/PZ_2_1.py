# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию
# деления нацело, для нахождения единиц — операцию взятия остатка от деления.

num = input("Введите целое двухзначное число: ")
# num любое двухзначное число

try:
    num = int(num)

    print("Правая цифра: ")
    print(num // 10)
    print("Левая цифра: ")
    print(num % 10)
    # вывод на экран левой и правой цифру
except ValueError:
    print("Вы ввели не число, запустите программу заново и введите число")
except TypeError:
    print("Вы ввели не число, запустите программу заново и введите число")



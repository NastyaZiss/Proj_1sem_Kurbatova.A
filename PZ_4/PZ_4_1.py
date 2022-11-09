# Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)

N = (input("Введите число, которое больше 0: "))
mult = 1.1
num = 1.1

try:
    N = int(N)
    while N > 0:
        num = num + 0.1
        mult = mult * num
        N = N - 1
    print("result: ", end=" ")
    print(mult)

except ValueError:
  print('Это не число. Запустите программу заново')



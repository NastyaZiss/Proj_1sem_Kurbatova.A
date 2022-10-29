# Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)

N = int(input("Введите число, которое больше 0"))
mult = 1.1
num = 1.1

try:
  tmp = float(N)
except ValueError:
  print('Это не число. Запустите программу заново')


while N > 0:
    print(num)
    num = num + 0.1
    mult = mult * num
    N = N - 1
    print(N)

print("result: ", end=" ")
print(mult)
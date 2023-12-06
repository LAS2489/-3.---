num =int (input("Введите количество чисел: "))

cnt = 0

for i in range(1, num + 1):
    num1 = int(input("Введите целое число: "))
    if num1 == 0:
        cnt += 1

print('Количество чисел равных нулю = ',cnt)
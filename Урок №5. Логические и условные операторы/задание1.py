number = int(input())
if (number < 0) and (number % 2 == 0):
    print('отрицательное четное число') 
elif number == 0:
    print('нулевое число')
elif (number > 0) and (number % 2 == 0):
    print('Положительное четное число')        
else:
    print('Нечетное число')
a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))

for i in range(a,b + 1):
    
        if i % 2 == 0:
            print(i, end=' ')
        
if a > b:
    print(f'Ошибка: 1-e число должно быть меньше 2-го ')  
    print(f'Повторите ввод ')
    
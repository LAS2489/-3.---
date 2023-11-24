min_amount = float(input())
Maik_amount = float(input())
Ivan_amount = float(input()) 

if (Maik_amount >= min_amount) and (Ivan_amount >= min_amount):
    print(2)
elif (Maik_amount >= min_amount) and (Ivan_amount < min_amount):
    print('Maik')
elif (Maik_amount < min_amount) and (Ivan_amount >= min_amount):
     print('Ivan')
elif Maik_amount + Ivan_amount >= min_amount:
     print(1)
else:
     print(0)
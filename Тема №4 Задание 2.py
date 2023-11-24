number =int(input())
dozens = number // 10 % 10
print(dozens)
units = number % 10
print(units)
hundreds = number // 100 % 10
print(hundreds) 
thousands = number // 1000 % 10
print(thousands)
tens_of_thousands = number // 10000
print(tens_of_thousands)

res = dozens ** units * hundreds / (tens_of_thousands - thousands)
print(res) 
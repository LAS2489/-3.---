word = input('Введите слово маленькими английскими буквами: ')
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 
vowels = a + e + i + o + u + y
consonants = len(word) - vowels
print('Гласных букв в слове: ',vowels, 'a', 'cогласных: ',consonants)

if (a == 0) or (e == 0) or (i == 0):
  print('False')
elif (o == 0) or (u == 0) or (y == 0):
  print('False')

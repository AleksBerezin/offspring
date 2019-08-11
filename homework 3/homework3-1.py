from string import ascii_lowercase
RUalphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def checkENG(s):
    return set(ascii_lowercase)-set(s.lower()) == set([])
string = input('Enter String in English: ')
if(checkENG(string)==True):
    print('This is a pangram')
else:
    print('This is not a pangram')

def checkRU(s):
     return set(RUalphabet)-set(s.lower()) == set([])
stringRU = input('Введите текст на русском: ')
if(checkRU(stringRU)==True):
    print('Это Панграмма')
else:
    print('Это не Панграмма')

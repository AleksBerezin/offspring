from string import ascii_lowercase
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def check_eng(s):
    return set(ascii_lowercase)-set(s.lower()) == set([])
string_eng = input('Enter String in English: ')
if(check_eng(string_eng)==True):
    print('This is a pangram')
else:
    print('This is not a pangram')

def check_ru(s):
     return set(alphabet_ru)-set(s.lower()) == set([])
string_ru = input('Введите текст на русском: ')
if(check_ru(string_ru)==True):
    print('Это Панграмма')
else:
    print('Это не Панграмма')

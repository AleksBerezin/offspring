print ('''Предлагаю сыграть в "Поле чудес".
Тебе нужно угадать загаданное слово.
Надеюсь, ты готов(а)?!''')

def hidden_word(s: str):
    unique_letter_in_s = set([i.lower() for i in s])
    already_said_letter = set()
    result_to_show = list('_' * len(s))
    print('Начинаем играть: {}'.format(' '.join(result_to_show)))
    while True:
        input_letter = input('Введите букву: ').lower()

        if input_letter in already_said_letter:
            print('Такую букву уже называли!')
            continue
        if input_letter in unique_letter_in_s:
            for index, letter in enumerate(s):
                if input_letter == letter.lower():
                    result_to_show[index] = input_letter
            if '_' not in result_to_show:
                print('Поздравляю, слово отгадано! {}'.format(' '.join(result_to_show)))
                break
            else:
                already_said_letter.add(input_letter)
                print('Есть такая буква! {}'.format(' '.join(result_to_show)))
                continue
        if input_letter not in unique_letter_in_s:
            already_said_letter.add(input_letter)
            print('Нет такой буквы!')
            continue
def main():
    hidden_word('python')

if __name__ == '__main__':
    main()

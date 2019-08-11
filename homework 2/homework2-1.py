questions_and_answers = {
    'Which color do you like more: green or yellow?': ['green', 'yellow'],
    'Which programming language do you prefer: java or python': ['java', 'python'],
    'Which city do you like more: moscow, london or tokyo': ['moscow', 'london', 'tokyo']
                        }

def questions(dict_):
   
    for question in dict_.keys():
        while True:
            input_ = input(question + '\n')
            if input_.lower() in dict_[question]:
                print('Ok, move next!')
                break
            else:
                print('{} there is no such option in the proposed. Choose again'.format(input_))
    print('Thank you for your answers. Good bye!')

def main(a: dict):
    questions(a)

if __name__ == '__main__':
    main(questions_and_answers)

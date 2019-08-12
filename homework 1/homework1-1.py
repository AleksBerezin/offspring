print('Hello, my name is Aleks. I just started learning Python. I need your help.')
print('What is your name?')
print()
name = input ()
print()
print("Nice to meet you, ",name,"!")
print('I need to check out my first assignment. I hope you help me')
print("Well, let's start")
print()

correct_answer = 4
while True:
    print('What will be the given expression: 2 * 2')
    guess = input ()
    i = int (guess)
    if i == correct_answer:
        print('Congratulations, you did it!')
        break
    else:
        print("Oh, you were wrong. Let's try again: 2 * 2")
print()
print("We turn to the second question")
print()
correct_answertwo = 3
while True:
    print("Let's complicate a bit: (3 + (2 * 5)) - 10 = ?")
    guess = input ()
    i = int (guess)
    if i == correct_answertwo:
        print('Looks like you are a genius! We can move on to the next question')
        break
    else:
        print('Try once more')
print()
print('And the third question')
print()

correct_answerthird = 12
while True:
    print('What do you answer in this case: the square root of 144?')
    guess = input ()
    i = int (guess)
    if i == correct_answerthird:
        print('Exactly - a genius! Thanks for your time! See you later!')
        break
    else:
        print("I believe in you, do not rush. Let's try again")

import random

# list of words
words = ['act', 'apple', 'orange', 'see', 'solid']

# word choice
word = random.choice(words)

# first time loop (set to True as default)
first_time = True

# player answer (answer will store in answer, but only right answer)
answer = ''

# dash display (total dash = word length)
dash_display = ''

# how many letter player need to be fill
left_dash = ''

# guess word by player
guess_word = ''

# letter index
current_letter_index = 0

for i in range(0, len(word)):
    dash_display += '_'

left_dash = [dash_display]

print(word)

print(dash_display)

while word != answer:
    guess_letter = input('Please enter your answer letter: ')
    guess_letter = guess_letter.lower()

    if (guess_letter == word[current_letter_index]):
        # create left dash
        left_dash = list(['_'*(len(word) - (current_letter_index + 1))])

        # set guess word
        guess_word += guess_letter

        # set the answer
        answer = f'{guess_word}{left_dash[0]}'

        # show the current incomplete answer to player
        print(answer)

        # set current letter index
        current_letter_index += 1
    else:

        print('Wrong!')

        if (first_time == True):
            first_time = False
            print('Your current status: ' + left_dash[0])
        else:
            print('Your current status: ' + answer)

print(f'Your answer is {answer} and it is right!')

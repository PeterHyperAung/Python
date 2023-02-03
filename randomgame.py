from random import choice

# options that computer and player can choose
options = ['rock', 'paper', 'scissors']

# computer random choice
computer_choice = choice(options)

# player choice from input (make sure to lower the letter)
player_choice = input('What is your choice? Rock, Paper, Scissors :').lower()

if player_choice not in options:
    print('Out of options')
else:
    if player_choice == computer_choice:
        print('Tie!')
    else:
        if player_choice == "rock":
            if computer_choice == "paper":
                print("You lost ,computer's " + computer_choice +
                      "covers player's " + player_choice)
            elif computer_choice == "scissors":
                print('You win, player ' + player_choice +
                      "beat computer's " + computer_choice)
        if player_choice == "paper":
            if computer_choice == "scissors":
                print("You lost ,computer's " + computer_choice +
                      "cuts player's " + player_choice)
            elif computer_choice == "rock":
                print("You win, player " + player_choice +
                      "cover computer's " + computer_choice)
        if player_choice == "scissors":
            if computer_choice == "rock":
                print("You lost , computer's " + computer_choice +
                      "beats player's " + player_choice)
            elif computer_choice == "paper":
                print('You win, player ' + player_choice +
                      "cut computer's " + computer_choice)

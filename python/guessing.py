#!/usr/bin/python3

number_of_guesses = 0
computers_number = 2029
prompt = 'What is your guess? '
while True:
    players_guess = input(prompt)
    number_of_guesses = number_of_guesses + 1
    if computers_number == int(players_guess):
        print('Correct!')
        print('you guessed ' + str(number_of_guesses) + ' times')
        break
    elif computers_number > int(players_guess):
         print('Too low')
    else:
         print('Too high')
    print('you guessed ' + str(number_of_guesses) + ' times')


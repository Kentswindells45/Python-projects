secret_number = 9
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:
    number_guess = int(input('Guess any number 1-9:\n'))
    guess_counter += 1
    if number_guess == secret_number:
        print('Congrats!!! YOU WON')
        break
else:
    print('Sorry You failed')

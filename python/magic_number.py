import random

magic_number = random.randint(1, 100)

guess = None

while magic_number != guess:
    guess = int(input('Please enter guess: '))
    if guess == magic_number:
        print(f'Congratulations! The magic number is {magic_number}!')
        solved = True
    elif guess > magic_number:
        print(f'The magic number is smaller, than {guess}!')
    else:
        print(f'The magic number is larger, than {guess}!')

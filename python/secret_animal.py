name = input('Please enter your name: ')
height = int(input('Please enter your height (in cm): '))
colour = input('Please enter your favourite colour: ')
secret = input('Please enter your secret spirit animal: ')

print(f'Hi {name}! Your height is {height}cms and your favourite colour is {colour}.\nCan you guess the top secret, national security risk spirit animal you just entered?')
guess = None
hint = ''
for i in range(len(secret)):
    if i == 0 or i == len(secret)-1:
        hint = hint + secret[i]
    else:
        hint = hint + '*'
while guess != secret:
    guess = input(f'Guess spirit animal ({hint}): ')
print(f'Congratulations! Your spirit animal is {secret}!')
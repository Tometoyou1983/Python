import os, random
os.system('cls')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
#    assert guess in ('heads','tails'), 'guess has to be either heads or tails'
toss = random.randint(0,1)
if toss == 0:
    toss = 'heads'
else:
    toss = 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')


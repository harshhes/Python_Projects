import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number betweeen 1 and {x} : '))
        if guess < random_number:
            print('Sorry, Try again. Too Low.')
        elif guess > random_number:
            print('Sorry, Try again.Too High.')

    print(f'Wohooo, Congratulations. You have guessed the number {random_number} correctly!')        

guess(20)

import random

from numpy import roll

min_int = 1
max_int = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the Dices...")
    print("The values are:\n")
    print(random.randint(min_int,max_int))
    print(random.randint(min_int,max_int))
    roll_again = input("Want to roll the dices again? Type 'yes' or 'y':\n ")
    if roll_again not in ['yes', 'y']:
        print("Invalid input!!")
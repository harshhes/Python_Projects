import random
chances=1

while(chances<=10):
    choice = ('Rock', 'Paper', 'Scissor')
    comp_choice = random.choice(choice)
    user = input("Enter your choice: \n R:Rock\n P:Paper\n S:Scissor\n ")
    n = user.upper()

    if n == 'R' or n == 'P' or n == 'S':
        if comp_choice == 'Rock' and n == 'R':
            print(f"Match Draw!! ,Computer's choice was {comp_choice}")
        elif comp_choice == 'Rock' and n == 'P':
            print(f"YAY YOU WON!!,Computer's choice was {comp_choice}")
        elif comp_choice == 'Rock' and n == 'S':
            print(f"OOPS YOU LOSE!! ,Computer's choice was {comp_choice}")
        elif comp_choice == 'Paper' and n == 'R':
            print(f"OOPS YOU LOSE!! ,Computer's choice was {comp_choice}")
        elif comp_choice == 'Paper' and n == 'P':
            print(f"Match Draw!! ,Computer's choice was {comp_choice}")
        elif comp_choice == 'Paper' and n == 'S':
            print(f"YAY YOU WON!! ,Computer's choice was {comp_choice}")
        elif comp_choice == 'Scissor' and n == 'R':
            print(f"YAY YOU WON!! ,Computer's choice was {comp_choice}")
        elif comp_choice == "Scissor" and n == 'P':
            print(f"OOPS YOU LOSE!! ,Computer's choice was {comp_choice}")   
        elif comp_choice == 'Scissor' and n == 'S':
            print(f"Match Draw!! ,Computer's choice was {comp_choice}")
        chances = chances + 1
    else:
        print("Invalid Input,Try Again\n")
        continue

print("\nGAME OVER!!!")   
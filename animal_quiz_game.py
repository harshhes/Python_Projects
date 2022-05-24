print("Loading the quiz game on animals..")


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt =0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Yoho, Correct Answer!!")
            score += 1
            still_guessing= False
        else:
            if attempt < 2:
                guess = input("Sorry, Wrong Answer. Try again!")
            attempt += 1
    if attempt == 3:
        print("The correct answer is ",answer)

print("Here is the first Question. All the best!")
score = 0
guess1 = input("1. Is Penguin a bird or a mammal?")
check_guess(guess1, 'bird')
guess2 = input("2. Tiger is a herbivore or a carnivore?")
check_guess(guess2, 'Carnivore')
guess3 = input("3. Which is the largest animal?")
check_guess(guess3, 'Blue Whale')

print("Your total score is ", score)
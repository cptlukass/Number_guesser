from random import randint


def guess_the_number():
    """Pick the random number from 1 to 100 and give user the clues to let him guess it.

    :return: information that user guessed the number.
    """
    computer_number = randint(1, 101)
    guess_num = ""
    while guess_num != computer_number:
        try:
            user_num = input("Guess the number: ")
            guess_num = int(user_num)
            if guess_num < computer_number:
                print("Too small!")
            elif guess_num > computer_number:
                print("Too big!")
            else:
                return "You win!"
        except ValueError:
            print("It's not a number!")


print(guess_the_number())

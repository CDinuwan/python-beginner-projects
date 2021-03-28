import random


def guess(x):
    random_number = random.randint(1, x)
    guess_num = ""
    while random_number != guess_num:
        guess_num = int(input("Guess number between 1 and 10: "))
        if guess_num < random_number:
            print("Sorry, Guess again too low")
        elif guess_num > random_number:
            print("Sorry, Guess again too high")
        else:
            print("Congratulation you guess the correct number")


guess(10)

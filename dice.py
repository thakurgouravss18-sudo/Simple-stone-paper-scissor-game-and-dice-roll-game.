import random
def play_dice():
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", user_roll)
    print("Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("You win!")
    elif user_roll < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")

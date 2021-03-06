import random

# The computer will guess the number and you can direct the correct number.
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?? "
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")


# This can be any value of your choose since the computer is making the guess:
computer_guess(10)  # 1-100

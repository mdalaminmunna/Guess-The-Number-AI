import random

def ai_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} your number? (h for High/l for Low/c for Correct): ")

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"You guessed the number {guess}!")

ai_guess(100)

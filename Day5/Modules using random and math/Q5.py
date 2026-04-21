import random
import math
secret_number = random.randint(1, 50)
attempts = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
print("You have 5 attempts to guess it.\n")
for i in range(1, attempts + 1):
    guess = int(input(f"Attempt {i}: Enter your guess: "))
    difference = math.fabs(secret_number - guess)
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break
    else:
        print(f"Your guess is {difference} away from the correct number.")
        
        if guess < secret_number:
            print("Try a higher number.\n")
        else:
            print("Try a lower number.\n")

else:
    print(f"😢 You've used all attempts. The correct number was {secret_number}.")

import random
random_number = random.randint(0,100)
guesses = -1
while guesses != random_number:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)
    if guess < random_number:
        print(" too low, try again.")
    elif guess > random_number:
        print("too high, try again.")
print("Congratulations! You guessed the number {random_number} correctly!")

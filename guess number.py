import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
         
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_number()


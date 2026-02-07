import random

secret = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if attempts >= max_attempts:
        print("Game Over! The number was", secret)
        break

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed in {attempts} attemots.")
        break
    
    print("Attempts left:", max_attempts - attempts)


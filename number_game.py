import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nGuess the number between 1 and 100")

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
            print(f"Correct! You guessed in {attempts} attempts.")
            break

        print("Attempts left:", max_attempts - attempts)


while True:
    play_game()
    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing!")
        break
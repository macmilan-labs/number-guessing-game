import random

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("enter 1, 2, or 3: ")

    if choice == '1':
        return 50, 10
    elif choice == '2':
        return 100, 7
    else:
        return 200, 5

def play_game(max_number, max_attempts):
    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_number}")

    while True:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_input)

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
    max_number, max_attepmts = choose_difficulty()
    play_game(max_number, max_attepmts)

    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing!")
        break
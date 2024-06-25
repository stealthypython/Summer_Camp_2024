secret_word = "python"
wrong = 0
correct = 0

while True:
    guess = input("Guess the secret word: ").lower()  
    if guess == secret_word:
        print("You guessed the secret word!")
        break
    else:
        print("Sorry, that was not the secret word! Try again.")

        # Letter Guessing Phase
        while wrong < len(secret_word):
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif guess in secret_word:
                count = secret_word.count(guess)  # Simplified counting
                correct += count
                print(f"Correct guess! '{guess}' appears {count} time(s).")
                if correct == len(secret_word):
                    print(f"You got it! The word is: {secret_word}")
                    break
            else:
                print("Incorrect letter. Try again.")
                wrong += 1
                if wrong == len(secret_word):
                    print(f"Oh no! You ran out of guesses. The word was: {secret_word}")
                    break

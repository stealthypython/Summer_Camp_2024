
secret_word = "python"
wrong = 0
correct = 0
while True:
      guess = input("Guess the secret word.")
      if guess == secret_word:
        print("You guessed the secret word!")
        break
      else:
        print("Sorry,that was not the secret word! Try again.")
      secret_word = input("Word to guess: ").lower()
      while wrong < len(secret_word):
        guess = input("Guess a letter.")
      if guess == secret_word:
                      print("You guessed the word!")
                      break
      elif len(guess) != 1:
              print("Single letter expected")  
elif guess in secret_word:
count = 0
for letter in secret_word:
  if letter == guess:
    count = count + 1
    correct += 1
    print("Correct guess", guess "shows",count, "times!")
    if correct = len(secret_word):
 print("All letters guessed! The word is:"secret_word")
    break
  else:
  print("Wrong.. try again!")
  wrong += 1
  if wrong == len(secret_word):
    print("Oh no! You are out of guesses! The word was: "secret_word)

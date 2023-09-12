name = "paradee"
trial = 5
correct_name = []

while True:
    guess = input("Guess letter: ")
    if guess in name:
        correct_name.append(guess)
        if set(name) == set(correct_name):
          print("Done")
          break
        print(f"Correct, trial: {trial}")
    else:
        trial -= 1
        if trial == 0:
          print("Die")
          break
        print(f"Don't have letter {guess}. trial: {trial}")

